from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_servicequotas_service_quota", namespace="aws_servicequotas")
class ServiceQuota(core.Resource):

    adjustable: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_value: Union[float, core.FloatOut] = core.attr(float, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    quota_code: Union[str, core.StringOut] = core.attr(str)

    quota_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    request_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    request_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_code: Union[str, core.StringOut] = core.attr(str)

    service_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    value: Union[float, core.FloatOut] = core.attr(float)

    def __init__(
        self,
        resource_name: str,
        *,
        quota_code: Union[str, core.StringOut],
        service_code: Union[str, core.StringOut],
        value: Union[float, core.FloatOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceQuota.Args(
                quota_code=quota_code,
                service_code=service_code,
                value=value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        quota_code: Union[str, core.StringOut] = core.arg()

        service_code: Union[str, core.StringOut] = core.arg()

        value: Union[float, core.FloatOut] = core.arg()
