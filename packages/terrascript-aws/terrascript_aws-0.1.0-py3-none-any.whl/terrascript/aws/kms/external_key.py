from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_kms_external_key", namespace="aws_kms")
class ExternalKey(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    bypass_policy_lockout_safety_check: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    deletion_window_in_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    expiration_model: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_material_base64: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    key_state: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_usage: Union[str, core.StringOut] = core.attr(str, computed=True)

    multi_region: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    valid_to: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bypass_policy_lockout_safety_check: Optional[Union[bool, core.BoolOut]] = None,
        deletion_window_in_days: Optional[Union[int, core.IntOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        key_material_base64: Optional[Union[str, core.StringOut]] = None,
        multi_region: Optional[Union[bool, core.BoolOut]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        valid_to: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ExternalKey.Args(
                bypass_policy_lockout_safety_check=bypass_policy_lockout_safety_check,
                deletion_window_in_days=deletion_window_in_days,
                description=description,
                enabled=enabled,
                key_material_base64=key_material_base64,
                multi_region=multi_region,
                policy=policy,
                tags=tags,
                tags_all=tags_all,
                valid_to=valid_to,
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

        key_material_base64: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        multi_region: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        valid_to: Optional[Union[str, core.StringOut]] = core.arg(default=None)
