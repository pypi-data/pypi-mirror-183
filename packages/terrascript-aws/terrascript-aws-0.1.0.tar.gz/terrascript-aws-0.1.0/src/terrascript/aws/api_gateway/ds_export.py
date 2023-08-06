from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_api_gateway_export", namespace="aws_api_gateway")
class DsExport(core.Data):

    accepts: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    body: Union[str, core.StringOut] = core.attr(str, computed=True)

    content_disposition: Union[str, core.StringOut] = core.attr(str, computed=True)

    content_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    export_type: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    stage_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        export_type: Union[str, core.StringOut],
        rest_api_id: Union[str, core.StringOut],
        stage_name: Union[str, core.StringOut],
        accepts: Optional[Union[str, core.StringOut]] = None,
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsExport.Args(
                export_type=export_type,
                rest_api_id=rest_api_id,
                stage_name=stage_name,
                accepts=accepts,
                parameters=parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accepts: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        export_type: Union[str, core.StringOut] = core.arg()

        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        rest_api_id: Union[str, core.StringOut] = core.arg()

        stage_name: Union[str, core.StringOut] = core.arg()
