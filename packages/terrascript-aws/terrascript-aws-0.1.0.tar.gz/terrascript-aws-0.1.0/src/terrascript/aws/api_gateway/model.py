from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_api_gateway_model", namespace="aws_api_gateway")
class Model(core.Resource):

    content_type: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    schema: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        content_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        rest_api_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        schema: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Model.Args(
                content_type=content_type,
                name=name,
                rest_api_id=rest_api_id,
                description=description,
                schema=schema,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content_type: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        rest_api_id: Union[str, core.StringOut] = core.arg()

        schema: Optional[Union[str, core.StringOut]] = core.arg(default=None)
