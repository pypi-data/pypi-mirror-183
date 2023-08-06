from typing import Union

import terrascript.core as core


@core.data(type="aws_lambda_alias", namespace="aws_lambda")
class DsAlias(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    function_name: Union[str, core.StringOut] = core.attr(str)

    function_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    invoke_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        function_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsAlias.Args(
                function_name=function_name,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_name: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()
