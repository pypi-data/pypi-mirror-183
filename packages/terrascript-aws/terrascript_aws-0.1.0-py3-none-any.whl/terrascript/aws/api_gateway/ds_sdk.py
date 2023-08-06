from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_api_gateway_sdk", namespace="aws_api_gateway")
class DsSdk(core.Data):

    body: Union[str, core.StringOut] = core.attr(str, computed=True)

    content_disposition: Union[str, core.StringOut] = core.attr(str, computed=True)

    content_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    sdk_type: Union[str, core.StringOut] = core.attr(str)

    stage_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        rest_api_id: Union[str, core.StringOut],
        sdk_type: Union[str, core.StringOut],
        stage_name: Union[str, core.StringOut],
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSdk.Args(
                rest_api_id=rest_api_id,
                sdk_type=sdk_type,
                stage_name=stage_name,
                parameters=parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        rest_api_id: Union[str, core.StringOut] = core.arg()

        sdk_type: Union[str, core.StringOut] = core.arg()

        stage_name: Union[str, core.StringOut] = core.arg()
