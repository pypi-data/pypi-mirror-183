from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_connect_instance", namespace="aws_connect")
class DsInstance(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_resolve_best_voices_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    contact_flow_logs_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    contact_lens_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    early_media_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity_management_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    inbound_calls_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    instance_alias: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    instance_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    outbound_calls_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    service_role: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        instance_alias: Optional[Union[str, core.StringOut]] = None,
        instance_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsInstance.Args(
                instance_alias=instance_alias,
                instance_id=instance_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_alias: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
