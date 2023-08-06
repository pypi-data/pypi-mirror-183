from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_servicequotas_service_quota", namespace="aws_servicequotas")
class DsServiceQuota(core.Data):

    adjustable: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_value: Union[float, core.FloatOut] = core.attr(float, computed=True)

    global_quota: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    quota_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    quota_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    service_code: Union[str, core.StringOut] = core.attr(str)

    service_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    value: Union[float, core.FloatOut] = core.attr(float, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        service_code: Union[str, core.StringOut],
        quota_code: Optional[Union[str, core.StringOut]] = None,
        quota_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsServiceQuota.Args(
                service_code=service_code,
                quota_code=quota_code,
                quota_name=quota_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        quota_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        quota_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_code: Union[str, core.StringOut] = core.arg()
