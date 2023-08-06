from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_placement_group", namespace="aws_ec2")
class PlacementGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    partition_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    placement_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    spread_level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    strategy: Union[str, core.StringOut] = core.attr(str)

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
        name: Union[str, core.StringOut],
        strategy: Union[str, core.StringOut],
        partition_count: Optional[Union[int, core.IntOut]] = None,
        spread_level: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PlacementGroup.Args(
                name=name,
                strategy=strategy,
                partition_count=partition_count,
                spread_level=spread_level,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        partition_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        spread_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        strategy: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
