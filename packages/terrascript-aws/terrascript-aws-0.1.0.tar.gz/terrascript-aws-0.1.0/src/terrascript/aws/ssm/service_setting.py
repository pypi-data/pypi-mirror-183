from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ssm_service_setting", namespace="aws_ssm")
class ServiceSetting(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    setting_id: Union[str, core.StringOut] = core.attr(str)

    setting_value: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        setting_id: Union[str, core.StringOut],
        setting_value: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceSetting.Args(
                setting_id=setting_id,
                setting_value=setting_value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        setting_id: Union[str, core.StringOut] = core.arg()

        setting_value: Union[str, core.StringOut] = core.arg()
