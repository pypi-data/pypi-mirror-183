from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lambda_provisioned_concurrency_config", namespace="aws_lambda")
class ProvisionedConcurrencyConfig(core.Resource):

    function_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    provisioned_concurrent_executions: Union[int, core.IntOut] = core.attr(int)

    qualifier: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        function_name: Union[str, core.StringOut],
        provisioned_concurrent_executions: Union[int, core.IntOut],
        qualifier: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProvisionedConcurrencyConfig.Args(
                function_name=function_name,
                provisioned_concurrent_executions=provisioned_concurrent_executions,
                qualifier=qualifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        function_name: Union[str, core.StringOut] = core.arg()

        provisioned_concurrent_executions: Union[int, core.IntOut] = core.arg()

        qualifier: Union[str, core.StringOut] = core.arg()
