from typing import List, Union

import terrascript.core as core


@core.data(type="aws_cur_report_definition", namespace="aws_cost_and_usage_report")
class DsCurReportDefinition(core.Data):

    additional_artifacts: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    additional_schema_elements: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    compression: Union[str, core.StringOut] = core.attr(str, computed=True)

    format: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    refresh_closed_reports: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    report_name: Union[str, core.StringOut] = core.attr(str)

    report_versioning: Union[str, core.StringOut] = core.attr(str, computed=True)

    s3_bucket: Union[str, core.StringOut] = core.attr(str, computed=True)

    s3_prefix: Union[str, core.StringOut] = core.attr(str, computed=True)

    s3_region: Union[str, core.StringOut] = core.attr(str, computed=True)

    time_unit: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        report_name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsCurReportDefinition.Args(
                report_name=report_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        report_name: Union[str, core.StringOut] = core.arg()
