from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_connect_instance", namespace="aws_connect")
class Instance(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_resolve_best_voices_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    contact_flow_logs_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    contact_lens_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    directory_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    early_media_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity_management_type: Union[str, core.StringOut] = core.attr(str)

    inbound_calls_enabled: Union[bool, core.BoolOut] = core.attr(bool)

    instance_alias: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    outbound_calls_enabled: Union[bool, core.BoolOut] = core.attr(bool)

    service_role: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        identity_management_type: Union[str, core.StringOut],
        inbound_calls_enabled: Union[bool, core.BoolOut],
        outbound_calls_enabled: Union[bool, core.BoolOut],
        auto_resolve_best_voices_enabled: Optional[Union[bool, core.BoolOut]] = None,
        contact_flow_logs_enabled: Optional[Union[bool, core.BoolOut]] = None,
        contact_lens_enabled: Optional[Union[bool, core.BoolOut]] = None,
        directory_id: Optional[Union[str, core.StringOut]] = None,
        early_media_enabled: Optional[Union[bool, core.BoolOut]] = None,
        instance_alias: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Instance.Args(
                identity_management_type=identity_management_type,
                inbound_calls_enabled=inbound_calls_enabled,
                outbound_calls_enabled=outbound_calls_enabled,
                auto_resolve_best_voices_enabled=auto_resolve_best_voices_enabled,
                contact_flow_logs_enabled=contact_flow_logs_enabled,
                contact_lens_enabled=contact_lens_enabled,
                directory_id=directory_id,
                early_media_enabled=early_media_enabled,
                instance_alias=instance_alias,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_resolve_best_voices_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        contact_flow_logs_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        contact_lens_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        directory_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        early_media_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        identity_management_type: Union[str, core.StringOut] = core.arg()

        inbound_calls_enabled: Union[bool, core.BoolOut] = core.arg()

        instance_alias: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        outbound_calls_enabled: Union[bool, core.BoolOut] = core.arg()
