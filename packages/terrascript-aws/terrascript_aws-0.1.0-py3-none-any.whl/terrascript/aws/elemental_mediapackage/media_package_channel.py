from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class IngestEndpoints(core.Schema):

    password: Union[str, core.StringOut] = core.attr(str, computed=True)

    url: Union[str, core.StringOut] = core.attr(str, computed=True)

    username: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        password: Union[str, core.StringOut],
        url: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
    ):
        super().__init__(
            args=IngestEndpoints.Args(
                password=password,
                url=url,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: Union[str, core.StringOut] = core.arg()

        url: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class HlsIngest(core.Schema):

    ingest_endpoints: Union[List[IngestEndpoints], core.ArrayOut[IngestEndpoints]] = core.attr(
        IngestEndpoints, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        ingest_endpoints: Union[List[IngestEndpoints], core.ArrayOut[IngestEndpoints]],
    ):
        super().__init__(
            args=HlsIngest.Args(
                ingest_endpoints=ingest_endpoints,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ingest_endpoints: Union[List[IngestEndpoints], core.ArrayOut[IngestEndpoints]] = core.arg()


@core.resource(type="aws_media_package_channel", namespace="aws_elemental_mediapackage")
class MediaPackageChannel(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    channel_id: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    hls_ingest: Union[List[HlsIngest], core.ArrayOut[HlsIngest]] = core.attr(
        HlsIngest, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        channel_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MediaPackageChannel.Args(
                channel_id=channel_id,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        channel_id: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
