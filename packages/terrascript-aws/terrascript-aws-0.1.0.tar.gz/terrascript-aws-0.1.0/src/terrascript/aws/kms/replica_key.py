from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_kms_replica_key", namespace="aws_kms")
class ReplicaKey(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    bypass_policy_lockout_safety_check: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    deletion_window_in_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_rotation_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    key_spec: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_usage: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    primary_key_arn: Union[str, core.StringOut] = core.attr(str)

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
        primary_key_arn: Union[str, core.StringOut],
        bypass_policy_lockout_safety_check: Optional[Union[bool, core.BoolOut]] = None,
        deletion_window_in_days: Optional[Union[int, core.IntOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicaKey.Args(
                primary_key_arn=primary_key_arn,
                bypass_policy_lockout_safety_check=bypass_policy_lockout_safety_check,
                deletion_window_in_days=deletion_window_in_days,
                description=description,
                enabled=enabled,
                policy=policy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bypass_policy_lockout_safety_check: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        deletion_window_in_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        primary_key_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
