from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lambda_invocation", namespace="aws_lambda")
class Invocation(core.Resource):

    function_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    input: Union[str, core.StringOut] = core.attr(str)

    qualifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    result: Union[str, core.StringOut] = core.attr(str, computed=True)

    triggers: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        function_name: Union[str, core.StringOut],
        input: Union[str, core.StringOut],
        qualifier: Optional[Union[str, core.StringOut]] = None,
        triggers: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Invocation.Args(
                function_name=function_name,
                input=input,
                qualifier=qualifier,
                triggers=triggers,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        function_name: Union[str, core.StringOut] = core.arg()

        input: Union[str, core.StringOut] = core.arg()

        qualifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        triggers: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
