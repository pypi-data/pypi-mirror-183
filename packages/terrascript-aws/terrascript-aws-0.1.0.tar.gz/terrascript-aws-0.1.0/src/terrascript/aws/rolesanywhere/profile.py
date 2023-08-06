from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_rolesanywhere_profile", namespace="aws_rolesanywhere")
class Profile(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    duration_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    managed_policy_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    require_instance_properties: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    role_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    session_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        role_arns: Union[List[str], core.ArrayOut[core.StringOut]],
        duration_seconds: Optional[Union[int, core.IntOut]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        managed_policy_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        require_instance_properties: Optional[Union[bool, core.BoolOut]] = None,
        session_policy: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Profile.Args(
                name=name,
                role_arns=role_arns,
                duration_seconds=duration_seconds,
                enabled=enabled,
                managed_policy_arns=managed_policy_arns,
                require_instance_properties=require_instance_properties,
                session_policy=session_policy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        duration_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        managed_policy_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        require_instance_properties: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        role_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        session_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
