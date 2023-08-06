from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_apigatewayv2_export", namespace="aws_apigatewayv2")
class DsExport(core.Data):

    api_id: Union[str, core.StringOut] = core.attr(str)

    body: Union[str, core.StringOut] = core.attr(str, computed=True)

    export_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    include_extensions: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    output_type: Union[str, core.StringOut] = core.attr(str)

    specification: Union[str, core.StringOut] = core.attr(str)

    stage_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        api_id: Union[str, core.StringOut],
        output_type: Union[str, core.StringOut],
        specification: Union[str, core.StringOut],
        export_version: Optional[Union[str, core.StringOut]] = None,
        include_extensions: Optional[Union[bool, core.BoolOut]] = None,
        stage_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsExport.Args(
                api_id=api_id,
                output_type=output_type,
                specification=specification,
                export_version=export_version,
                include_extensions=include_extensions,
                stage_name=stage_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_id: Union[str, core.StringOut] = core.arg()

        export_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        include_extensions: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        output_type: Union[str, core.StringOut] = core.arg()

        specification: Union[str, core.StringOut] = core.arg()

        stage_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
