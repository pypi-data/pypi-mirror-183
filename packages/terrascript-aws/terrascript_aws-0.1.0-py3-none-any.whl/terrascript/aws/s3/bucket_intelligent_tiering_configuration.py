from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Filter(core.Schema):

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        prefix: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Filter.Args(
                prefix=prefix,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class Tiering(core.Schema):

    access_tier: Union[str, core.StringOut] = core.attr(str)

    days: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        access_tier: Union[str, core.StringOut],
        days: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Tiering.Args(
                access_tier=access_tier,
                days=days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_tier: Union[str, core.StringOut] = core.arg()

        days: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_s3_bucket_intelligent_tiering_configuration", namespace="aws_s3")
class BucketIntelligentTieringConfiguration(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    filter: Optional[Filter] = core.attr(Filter, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tiering: Union[List[Tiering], core.ArrayOut[Tiering]] = core.attr(Tiering, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        tiering: Union[List[Tiering], core.ArrayOut[Tiering]],
        filter: Optional[Filter] = None,
        status: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketIntelligentTieringConfiguration.Args(
                bucket=bucket,
                name=name,
                tiering=tiering,
                filter=filter,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        filter: Optional[Filter] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tiering: Union[List[Tiering], core.ArrayOut[Tiering]] = core.arg()
