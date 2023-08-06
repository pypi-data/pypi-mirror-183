from __future__ import annotations

import os
from fractions import Fraction
from functools import partial
from threading import Lock

import numpy as np
import tensorrt
import torch
import torch.nn.functional as F
import vapoursynth as vs
from functorch.compile import memory_efficient_fusion
from torch_tensorrt.fx import LowerSetting
from torch_tensorrt.fx.lower import Lowerer
from torch_tensorrt.fx.utils import LowerPrecision

__version__ = '3.1.0'

package_dir = os.path.dirname(os.path.realpath(__file__))


@torch.inference_mode()
def RIFE(
    clip: vs.VideoNode,
    device_index: int | None = None,
    num_streams: int = 3,
    nvfuser: bool = False,
    cuda_graphs: bool = False,
    trt: bool = False,
    trt_max_workspace_size: int = 1 << 30,
    trt_cache_path: str = package_dir,
    model: str = '4.6',
    factor_num: int = 2,
    factor_den: int = 1,
    fps_num: int | None = None,
    fps_den: int | None = None,
    scale: float = 1.0,
    ensemble: bool = False,
    sc: bool = True,
    sc_threshold: float | None = None,
) -> vs.VideoNode:
    """Real-Time Intermediate Flow Estimation for Video Frame Interpolation

    :param clip:                    Clip to process. Only RGBH and RGBS formats are supported.
                                    RGBH performs inference in FP16 mode while RGBS performs inference in FP32 mode.
    :param device_index:            Device ordinal of the GPU.
    :param num_streams:             Number of CUDA streams to enqueue the kernels.
    :param nvfuser:                 Enable fusion through nvFuser. Not allowed in TensorRT. (experimental)
    :param cuda_graphs:             Use CUDA Graphs to remove CPU overhead associated with launching CUDA kernels
                                    sequentially. Not allowed in TensorRT. Not supported for '4.0' and '4.1' models.
    :param trt:                     Use TensorRT for high-performance inference.
                                    Not supported for '4.0' and '4.1' models.
    :param trt_max_workspace_size:  Maximum workspace size for TensorRT engine.
    :param trt_cache_path:          Path for TensorRT engine file. Engine will be cached when it's built for the first
                                    time. Note each engine is created for specific settings such as model path/name,
                                    precision, workspace etc, and specific GPUs and it's not portable.
    :param model:                   Model version to use. Must be '4.0', '4.1', '4.2', '4.3', '4.4', '4.5', or '4.6'.
    :param factor_num:              Numerator of factor for target frame rate.
                                    For example `factor_num=5, factor_den=2` will multiply the frame rate by 2.5.
    :param factor_den:              Denominator of factor for target frame rate.
    :param fps_num:                 Numerator of target frame rate. Override `factor_num` and `factor_den` if specified.
    :param fps_den:                 Denominator of target frame rate.
    :param scale:                   Control the process resolution for optical flow model. Try scale=0.5 for 4K video.
                                    Must be 0.25, 0.5, 1.0, 2.0, or 4.0.
    :param ensemble:                Smooth predictions in areas where the estimation is uncertain.
    :param sc:                      Avoid interpolating frames over scene changes.
    :param sc_threshold:            Threshold for scene change detection. Must be between 0.0 and 1.0.
                                    Leave it None if the clip already has _SceneChangeNext properly set.
    """
    if not isinstance(clip, vs.VideoNode):
        raise vs.Error('RIFE: this is not a clip')

    if clip.format.id not in [vs.RGBH, vs.RGBS]:
        raise vs.Error('RIFE: only RGBH and RGBS formats are supported')

    if clip.num_frames < 2:
        raise vs.Error("RIFE: clip's number of frames must be at least 2")

    if not torch.cuda.is_available():
        raise vs.Error('RIFE: CUDA is not available')

    if num_streams < 1:
        raise vs.Error('RIFE: num_streams must be at least 1')

    if num_streams > vs.core.num_threads:
        raise vs.Error('RIFE: setting num_streams greater than `core.num_threads` is useless')

    if trt:
        if nvfuser:
            raise vs.Error('RIFE: nvfuser and trt are mutually exclusive')

        if cuda_graphs:
            raise vs.Error('RIFE: cuda_graphs and trt are mutually exclusive')

    if model not in ['4.0', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6']:
        raise vs.Error("RIFE: model must be '4.0', '4.1', '4.2', '4.3', '4.4', '4.5', or '4.6'")

    if factor_num < 1:
        raise vs.Error('RIFE: factor_num must be at least 1')

    if factor_den < 1:
        raise vs.Error('RIFE: factor_den must be at least 1')

    if fps_num is not None and fps_num < 1:
        raise vs.Error('RIFE: fps_num must be at least 1')

    if fps_den is not None and fps_den < 1:
        raise vs.Error('RIFE: fps_den must be at least 1')

    if fps_num is not None and fps_den is not None and clip.fps == 0:
        raise vs.Error('RIFE: clip does not have a valid frame rate and hence fps_num and fps_den cannot be used')

    if scale not in [0.25, 0.5, 1.0, 2.0, 4.0]:
        raise vs.Error('RIFE: scale must be 0.25, 0.5, 1.0, 2.0, or 4.0')

    if os.path.getsize(os.path.join(package_dir, 'flownet_v4.0.pkl')) == 0:
        raise vs.Error("RIFE: model files have not been downloaded. run 'python -m vsrife' first")

    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.benchmark = True

    fp16 = clip.format.bits_per_sample == 16
    if fp16:
        torch.set_default_tensor_type(torch.HalfTensor)

    device = torch.device('cuda', device_index)

    stream = [torch.cuda.Stream(device=device) for _ in range(num_streams)]
    stream_lock = [Lock() for _ in range(num_streams)]

    match model:
        case '4.0':
            from .IFNet_HDv3_v4_0 import IFNet
        case '4.1':
            from .IFNet_HDv3_v4_1 import IFNet
        case '4.2':
            from .IFNet_HDv3_v4_2 import IFNet
        case '4.3':
            from .IFNet_HDv3_v4_3 import IFNet
        case '4.4':
            from .IFNet_HDv3_v4_4 import IFNet
        case '4.5':
            from .IFNet_HDv3_v4_5 import IFNet
        case '4.6':
            from .IFNet_HDv3_v4_6 import IFNet

    model_name = f'flownet_v{model}.pkl'

    checkpoint = torch.load(os.path.join(package_dir, model_name), map_location='cpu')
    checkpoint = {k.replace('module.', ''): v for k, v in checkpoint.items() if 'module.' in k}

    flownet = IFNet(scale, ensemble)
    flownet.load_state_dict(checkpoint, strict=False)
    flownet.eval().to(device, memory_format=torch.channels_last)

    w = clip.width
    h = clip.height
    tmp = max(128, int(128 / scale))
    pw = ((w - 1) // tmp + 1) * tmp
    ph = ((h - 1) // tmp + 1) * tmp
    padding = (0, pw - w, 0, ph - h)

    if nvfuser:
        flownet = memory_efficient_fusion(flownet)

    if cuda_graphs:
        graph: list[torch.cuda.CUDAGraph] = []
        static_img0: list[torch.Tensor] = []
        static_img1: list[torch.Tensor] = []
        static_timestep: list[torch.Tensor] = []
        static_output: list[torch.Tensor] = []

        for i in range(num_streams):
            static_img0.append(torch.empty(1, 3, ph, pw, device=device, memory_format=torch.channels_last))
            static_img1.append(torch.empty(1, 3, ph, pw, device=device, memory_format=torch.channels_last))
            static_timestep.append(torch.empty(1, 1, ph, pw, device=device, memory_format=torch.channels_last))

            torch.cuda.synchronize(device=device)
            stream[i].wait_stream(torch.cuda.current_stream(device=device))
            with torch.cuda.stream(stream[i]):
                flownet(static_img0[i], static_img1[i], static_timestep[i])
            torch.cuda.current_stream(device=device).wait_stream(stream[i])
            torch.cuda.synchronize(device=device)

            graph.append(torch.cuda.CUDAGraph())
            with torch.cuda.graph(graph[i], stream=stream[i]):
                static_output.append(flownet(static_img0[i], static_img1[i], static_timestep[i]))
    elif trt:
        device_name = torch.cuda.get_device_name(device)
        trt_version = tensorrt.__version__
        dimensions = f'{pw}x{ph}'
        precision = 'fp16' if fp16 else 'fp32'
        trt_engine_path = os.path.join(
            os.path.realpath(trt_cache_path),
            (
                f'{model_name}'
                + f'_{device_name}'
                + f'_trt-{trt_version}'
                + f'_{dimensions}'
                + f'_{precision}'
                + f'_workspace-{trt_max_workspace_size}'
                + f'_scale-{scale}'
                + f'_ensemble-{ensemble}'
                + '.pt'
            ),
        )

        if not os.path.isfile(trt_engine_path):
            lower_setting = LowerSetting(
                lower_precision=LowerPrecision.FP16 if fp16 else LowerPrecision.FP32,
                min_acc_module_size=1,
                max_workspace_size=trt_max_workspace_size,
                dynamic_batch=False,
                tactic_sources=1 << int(tensorrt.TacticSource.EDGE_MASK_CONVOLUTIONS)
                | 1 << int(tensorrt.TacticSource.JIT_CONVOLUTIONS),
            )
            lowerer = Lowerer.create(lower_setting=lower_setting)
            flownet = lowerer(
                flownet,
                [
                    torch.empty(1, 3, ph, pw, device=device, memory_format=torch.channels_last),
                    torch.empty(1, 3, ph, pw, device=device, memory_format=torch.channels_last),
                    torch.empty(1, 1, ph, pw, device=device, memory_format=torch.channels_last),
                ],
            )
            torch.save(flownet, trt_engine_path)

        del flownet
        torch.cuda.empty_cache()
        flownet = [torch.load(trt_engine_path) for _ in range(num_streams)]

    if fps_num is not None and fps_den is not None:
        factor = Fraction(fps_num, fps_den) / clip.fps
        factor_num, factor_den = factor.as_integer_ratio()

    if sc_threshold is not None:
        clip = sc_detect(clip, sc_threshold)

    index = -1
    index_lock = Lock()

    def frame_adjuster(n: int, clip: vs.VideoNode) -> vs.VideoNode:
        return clip[n * factor_den // factor_num]

    @torch.inference_mode()
    def inference(n: int, f: list[vs.VideoFrame]) -> vs.VideoFrame:
        remainder = n * factor_den % factor_num

        if remainder == 0 or (sc and f[0].props.get('_SceneChangeNext')):
            return f[0]

        nonlocal index
        with index_lock:
            index = (index + 1) % num_streams
            local_index = index

        with stream_lock[local_index], torch.cuda.stream(stream[local_index]):
            img0 = frame_to_tensor(f[0], device)
            img1 = frame_to_tensor(f[1], device)
            img0 = F.pad(img0, padding)
            img1 = F.pad(img1, padding)

            timestep = torch.full((1, 1, img0.shape[2], img0.shape[3]), remainder / factor_num, device=device)
            timestep = timestep.to(memory_format=torch.channels_last)

            if cuda_graphs:
                static_img0[local_index].copy_(img0)
                static_img1[local_index].copy_(img1)
                static_timestep[local_index].copy_(timestep)
                graph[local_index].replay()
                output = static_output[local_index]
            elif trt:
                output = flownet[local_index](img0, img1, timestep)
            else:
                output = flownet(img0, img1, timestep)

            return tensor_to_frame(output[:, :, :h, :w], f[0].copy())

    format_clip = clip.std.BlankClip(
        length=clip.num_frames * factor_num // factor_den,
        fpsnum=clip.fps.numerator * factor_num,
        fpsden=clip.fps.denominator * factor_den,
    )

    clip0 = format_clip.std.FrameEval(partial(frame_adjuster, clip=clip), clip_src=clip)
    clip1 = clip.std.DuplicateFrames(frames=clip.num_frames - 1).std.Trim(first=1)
    clip1 = format_clip.std.FrameEval(partial(frame_adjuster, clip=clip1), clip_src=clip1)
    return clip0.std.FrameEval(lambda n: clip0.std.ModifyFrame([clip0, clip1], inference), clip_src=[clip0, clip1])


def sc_detect(clip: vs.VideoNode, threshold: float) -> vs.VideoNode:
    def copy_property(n: int, f: list[vs.VideoFrame]) -> vs.VideoFrame:
        fout = f[0].copy()
        fout.props['_SceneChangePrev'] = f[1].props['_SceneChangePrev']
        fout.props['_SceneChangeNext'] = f[1].props['_SceneChangeNext']
        return fout

    sc_clip = clip.resize.Bicubic(format=vs.GRAY8, matrix_s='709').misc.SCDetect(threshold)
    return clip.std.FrameEval(lambda n: clip.std.ModifyFrame([clip, sc_clip], copy_property), clip_src=[clip, sc_clip])


def frame_to_tensor(frame: vs.VideoFrame, device: torch.device) -> torch.Tensor:
    array = np.stack([np.asarray(frame[plane]) for plane in range(frame.format.num_planes)])
    return torch.from_numpy(array).unsqueeze(0).to(device, memory_format=torch.channels_last)


def tensor_to_frame(tensor: torch.Tensor, frame: vs.VideoFrame) -> vs.VideoFrame:
    array = tensor.squeeze(0).detach().cpu().numpy()
    for plane in range(frame.format.num_planes):
        np.copyto(np.asarray(frame[plane]), array[plane, :, :])
    return frame
