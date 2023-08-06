from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_api_gateway_usage_plan_key", namespace="aws_api_gateway")
class UsagePlanKey(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_id: Union[str, core.StringOut] = core.attr(str)

    key_type: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    usage_plan_id: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        key_id: Union[str, core.StringOut],
        key_type: Union[str, core.StringOut],
        usage_plan_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UsagePlanKey.Args(
                key_id=key_id,
                key_type=key_type,
                usage_plan_id=usage_plan_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key_id: Union[str, core.StringOut] = core.arg()

        key_type: Union[str, core.StringOut] = core.arg()

        usage_plan_id: Union[str, core.StringOut] = core.arg()
