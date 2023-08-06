from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_connect_lambda_function_association", namespace="aws_connect")
class LambdaFunctionAssociation(core.Resource):
    """
    (Required) Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifie
    r.
    """

    function_arn: Union[str, core.StringOut] = core.attr(str)

    """
    The Amazon Connect instance ID and Lambda Function ARN separated by a comma (`,`).
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The identifier of the Amazon Connect instance. You can find the instanceId in the ARN of
    the instance.
    """
    instance_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        function_arn: Union[str, core.StringOut],
        instance_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LambdaFunctionAssociation.Args(
                function_arn=function_arn,
                instance_id=instance_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        function_arn: Union[str, core.StringOut] = core.arg()

        instance_id: Union[str, core.StringOut] = core.arg()
