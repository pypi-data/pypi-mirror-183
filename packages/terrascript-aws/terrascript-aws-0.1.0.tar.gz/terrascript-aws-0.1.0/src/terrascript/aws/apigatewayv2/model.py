from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_apigatewayv2_model", namespace="aws_apigatewayv2")
class Model(core.Resource):

    api_id: Union[str, core.StringOut] = core.attr(str)

    content_type: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    schema: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: Union[str, core.StringOut],
        content_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        schema: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Model.Args(
                api_id=api_id,
                content_type=content_type,
                name=name,
                schema=schema,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: Union[str, core.StringOut] = core.arg()

        content_type: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        schema: Union[str, core.StringOut] = core.arg()
