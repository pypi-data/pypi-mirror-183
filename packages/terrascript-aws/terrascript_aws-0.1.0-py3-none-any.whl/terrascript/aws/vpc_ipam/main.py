from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class OperatingRegions(core.Schema):

    region_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        region_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OperatingRegions.Args(
                region_name=region_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region_name: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_vpc_ipam", namespace="aws_vpc_ipam")
class Main(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cascade: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    operating_regions: Union[List[OperatingRegions], core.ArrayOut[OperatingRegions]] = core.attr(
        OperatingRegions, kind=core.Kind.array
    )

    private_default_scope_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_default_scope_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    scope_count: Union[int, core.IntOut] = core.attr(int, computed=True)

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
        operating_regions: Union[List[OperatingRegions], core.ArrayOut[OperatingRegions]],
        cascade: Optional[Union[bool, core.BoolOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Main.Args(
                operating_regions=operating_regions,
                cascade=cascade,
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
        cascade: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        operating_regions: Union[
            List[OperatingRegions], core.ArrayOut[OperatingRegions]
        ] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
