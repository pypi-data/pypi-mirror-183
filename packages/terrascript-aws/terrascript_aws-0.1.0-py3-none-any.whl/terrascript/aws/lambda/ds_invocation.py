from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_lambda_invocation", namespace="aws_lambda")
class DsInvocation(core.Data):

    function_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    input: Union[str, core.StringOut] = core.attr(str)

    qualifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    result: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        function_name: Union[str, core.StringOut],
        input: Union[str, core.StringOut],
        qualifier: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsInvocation.Args(
                function_name=function_name,
                input=input,
                qualifier=qualifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_name: Union[str, core.StringOut] = core.arg()

        input: Union[str, core.StringOut] = core.arg()

        qualifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)
