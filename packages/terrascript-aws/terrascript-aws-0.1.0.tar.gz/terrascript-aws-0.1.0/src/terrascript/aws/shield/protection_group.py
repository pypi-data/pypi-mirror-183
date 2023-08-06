from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_shield_protection_group", namespace="aws_shield")
class ProtectionGroup(core.Resource):

    aggregation: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    members: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    pattern: Union[str, core.StringOut] = core.attr(str)

    protection_group_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    protection_group_id: Union[str, core.StringOut] = core.attr(str)

    resource_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        aggregation: Union[str, core.StringOut],
        pattern: Union[str, core.StringOut],
        protection_group_id: Union[str, core.StringOut],
        members: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        resource_type: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProtectionGroup.Args(
                aggregation=aggregation,
                pattern=pattern,
                protection_group_id=protection_group_id,
                members=members,
                resource_type=resource_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aggregation: Union[str, core.StringOut] = core.arg()

        members: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        pattern: Union[str, core.StringOut] = core.arg()

        protection_group_id: Union[str, core.StringOut] = core.arg()

        resource_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
