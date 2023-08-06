from typing import Union

import terrascript.core as core


@core.data(type="aws_connect_lambda_function_association", namespace="aws_connect")
class DsLambdaFunctionAssociation(core.Data):
    """
    (Required) Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifie
    r.
    """

    function_arn: Union[str, core.StringOut] = core.attr(str)

    """
    AWS Region.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The identifier of the Amazon Connect instance. You can find the instanceId in the ARN of
    the instance.
    """
    instance_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        function_arn: Union[str, core.StringOut],
        instance_id: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsLambdaFunctionAssociation.Args(
                function_arn=function_arn,
                instance_id=instance_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_arn: Union[str, core.StringOut] = core.arg()

        instance_id: Union[str, core.StringOut] = core.arg()
