from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Audio(core.Schema):

    audio_packing_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bit_rate: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    channels: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    codec: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sample_rate: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        audio_packing_mode: Optional[Union[str, core.StringOut]] = None,
        bit_rate: Optional[Union[str, core.StringOut]] = None,
        channels: Optional[Union[str, core.StringOut]] = None,
        codec: Optional[Union[str, core.StringOut]] = None,
        sample_rate: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Audio.Args(
                audio_packing_mode=audio_packing_mode,
                bit_rate=bit_rate,
                channels=channels,
                codec=codec,
                sample_rate=sample_rate,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        audio_packing_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bit_rate: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        channels: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        codec: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sample_rate: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Video(core.Schema):

    aspect_ratio: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bit_rate: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    codec: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    display_aspect_ratio: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    fixed_gop: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    frame_rate: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    keyframes_max_dist: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_frame_rate: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    max_height: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_width: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    padding_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resolution: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sizing_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        aspect_ratio: Optional[Union[str, core.StringOut]] = None,
        bit_rate: Optional[Union[str, core.StringOut]] = None,
        codec: Optional[Union[str, core.StringOut]] = None,
        display_aspect_ratio: Optional[Union[str, core.StringOut]] = None,
        fixed_gop: Optional[Union[str, core.StringOut]] = None,
        frame_rate: Optional[Union[str, core.StringOut]] = None,
        keyframes_max_dist: Optional[Union[str, core.StringOut]] = None,
        max_frame_rate: Optional[Union[str, core.StringOut]] = None,
        max_height: Optional[Union[str, core.StringOut]] = None,
        max_width: Optional[Union[str, core.StringOut]] = None,
        padding_policy: Optional[Union[str, core.StringOut]] = None,
        resolution: Optional[Union[str, core.StringOut]] = None,
        sizing_policy: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Video.Args(
                aspect_ratio=aspect_ratio,
                bit_rate=bit_rate,
                codec=codec,
                display_aspect_ratio=display_aspect_ratio,
                fixed_gop=fixed_gop,
                frame_rate=frame_rate,
                keyframes_max_dist=keyframes_max_dist,
                max_frame_rate=max_frame_rate,
                max_height=max_height,
                max_width=max_width,
                padding_policy=padding_policy,
                resolution=resolution,
                sizing_policy=sizing_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aspect_ratio: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bit_rate: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        codec: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        display_aspect_ratio: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        fixed_gop: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        frame_rate: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        keyframes_max_dist: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_frame_rate: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_height: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_width: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        padding_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resolution: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sizing_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Thumbnails(core.Schema):

    aspect_ratio: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    interval: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_height: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_width: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    padding_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resolution: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sizing_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        aspect_ratio: Optional[Union[str, core.StringOut]] = None,
        format: Optional[Union[str, core.StringOut]] = None,
        interval: Optional[Union[str, core.StringOut]] = None,
        max_height: Optional[Union[str, core.StringOut]] = None,
        max_width: Optional[Union[str, core.StringOut]] = None,
        padding_policy: Optional[Union[str, core.StringOut]] = None,
        resolution: Optional[Union[str, core.StringOut]] = None,
        sizing_policy: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Thumbnails.Args(
                aspect_ratio=aspect_ratio,
                format=format,
                interval=interval,
                max_height=max_height,
                max_width=max_width,
                padding_policy=padding_policy,
                resolution=resolution,
                sizing_policy=sizing_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aspect_ratio: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        interval: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_height: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_width: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        padding_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resolution: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sizing_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AudioCodecOptions(core.Schema):

    bit_depth: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    bit_order: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    profile: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    signed: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        bit_depth: Optional[Union[str, core.StringOut]] = None,
        bit_order: Optional[Union[str, core.StringOut]] = None,
        profile: Optional[Union[str, core.StringOut]] = None,
        signed: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AudioCodecOptions.Args(
                bit_depth=bit_depth,
                bit_order=bit_order,
                profile=profile,
                signed=signed,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bit_depth: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bit_order: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        profile: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        signed: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class VideoWatermarks(core.Schema):

    horizontal_align: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    horizontal_offset: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_height: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_width: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    opacity: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sizing_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    target: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vertical_align: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vertical_offset: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        horizontal_align: Optional[Union[str, core.StringOut]] = None,
        horizontal_offset: Optional[Union[str, core.StringOut]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        max_height: Optional[Union[str, core.StringOut]] = None,
        max_width: Optional[Union[str, core.StringOut]] = None,
        opacity: Optional[Union[str, core.StringOut]] = None,
        sizing_policy: Optional[Union[str, core.StringOut]] = None,
        target: Optional[Union[str, core.StringOut]] = None,
        vertical_align: Optional[Union[str, core.StringOut]] = None,
        vertical_offset: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=VideoWatermarks.Args(
                horizontal_align=horizontal_align,
                horizontal_offset=horizontal_offset,
                id=id,
                max_height=max_height,
                max_width=max_width,
                opacity=opacity,
                sizing_policy=sizing_policy,
                target=target,
                vertical_align=vertical_align,
                vertical_offset=vertical_offset,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        horizontal_align: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        horizontal_offset: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_height: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_width: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        opacity: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sizing_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vertical_align: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vertical_offset: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_elastictranscoder_preset", namespace="aws_elastictranscoder")
class Preset(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    audio: Optional[Audio] = core.attr(Audio, default=None)

    audio_codec_options: Optional[AudioCodecOptions] = core.attr(
        AudioCodecOptions, default=None, computed=True
    )

    container: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    thumbnails: Optional[Thumbnails] = core.attr(Thumbnails, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    video: Optional[Video] = core.attr(Video, default=None)

    video_codec_options: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    video_watermarks: Optional[
        Union[List[VideoWatermarks], core.ArrayOut[VideoWatermarks]]
    ] = core.attr(VideoWatermarks, default=None, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        container: Union[str, core.StringOut],
        audio: Optional[Audio] = None,
        audio_codec_options: Optional[AudioCodecOptions] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        thumbnails: Optional[Thumbnails] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        video: Optional[Video] = None,
        video_codec_options: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        video_watermarks: Optional[
            Union[List[VideoWatermarks], core.ArrayOut[VideoWatermarks]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Preset.Args(
                container=container,
                audio=audio,
                audio_codec_options=audio_codec_options,
                description=description,
                name=name,
                thumbnails=thumbnails,
                type=type,
                video=video,
                video_codec_options=video_codec_options,
                video_watermarks=video_watermarks,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        audio: Optional[Audio] = core.arg(default=None)

        audio_codec_options: Optional[AudioCodecOptions] = core.arg(default=None)

        container: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        thumbnails: Optional[Thumbnails] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        video: Optional[Video] = core.arg(default=None)

        video_codec_options: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        video_watermarks: Optional[
            Union[List[VideoWatermarks], core.ArrayOut[VideoWatermarks]]
        ] = core.arg(default=None)
