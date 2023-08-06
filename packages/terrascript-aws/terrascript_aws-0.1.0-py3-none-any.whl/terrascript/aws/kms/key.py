from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_kms_key", namespace="aws_kms")
class Key(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    bypass_policy_lockout_safety_check: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    customer_master_key_spec: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    deletion_window_in_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    enable_key_rotation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    is_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_usage: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    multi_region: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

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
        bypass_policy_lockout_safety_check: Optional[Union[bool, core.BoolOut]] = None,
        customer_master_key_spec: Optional[Union[str, core.StringOut]] = None,
        deletion_window_in_days: Optional[Union[int, core.IntOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        enable_key_rotation: Optional[Union[bool, core.BoolOut]] = None,
        is_enabled: Optional[Union[bool, core.BoolOut]] = None,
        key_usage: Optional[Union[str, core.StringOut]] = None,
        multi_region: Optional[Union[bool, core.BoolOut]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Key.Args(
                bypass_policy_lockout_safety_check=bypass_policy_lockout_safety_check,
                customer_master_key_spec=customer_master_key_spec,
                deletion_window_in_days=deletion_window_in_days,
                description=description,
                enable_key_rotation=enable_key_rotation,
                is_enabled=is_enabled,
                key_usage=key_usage,
                multi_region=multi_region,
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

        customer_master_key_spec: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        deletion_window_in_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable_key_rotation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        is_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        key_usage: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        multi_region: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
