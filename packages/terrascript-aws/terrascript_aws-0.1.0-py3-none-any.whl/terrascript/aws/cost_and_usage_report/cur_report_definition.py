from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cur_report_definition", namespace="aws_cost_and_usage_report")
class CurReportDefinition(core.Resource):

    additional_artifacts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    additional_schema_elements: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    compression: Union[str, core.StringOut] = core.attr(str)

    format: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    refresh_closed_reports: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    report_name: Union[str, core.StringOut] = core.attr(str)

    report_versioning: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_bucket: Union[str, core.StringOut] = core.attr(str)

    s3_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_region: Union[str, core.StringOut] = core.attr(str)

    time_unit: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        additional_schema_elements: Union[List[str], core.ArrayOut[core.StringOut]],
        compression: Union[str, core.StringOut],
        format: Union[str, core.StringOut],
        report_name: Union[str, core.StringOut],
        s3_bucket: Union[str, core.StringOut],
        s3_region: Union[str, core.StringOut],
        time_unit: Union[str, core.StringOut],
        additional_artifacts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        refresh_closed_reports: Optional[Union[bool, core.BoolOut]] = None,
        report_versioning: Optional[Union[str, core.StringOut]] = None,
        s3_prefix: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CurReportDefinition.Args(
                additional_schema_elements=additional_schema_elements,
                compression=compression,
                format=format,
                report_name=report_name,
                s3_bucket=s3_bucket,
                s3_region=s3_region,
                time_unit=time_unit,
                additional_artifacts=additional_artifacts,
                refresh_closed_reports=refresh_closed_reports,
                report_versioning=report_versioning,
                s3_prefix=s3_prefix,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        additional_artifacts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        additional_schema_elements: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        compression: Union[str, core.StringOut] = core.arg()

        format: Union[str, core.StringOut] = core.arg()

        refresh_closed_reports: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        report_name: Union[str, core.StringOut] = core.arg()

        report_versioning: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_bucket: Union[str, core.StringOut] = core.arg()

        s3_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_region: Union[str, core.StringOut] = core.arg()

        time_unit: Union[str, core.StringOut] = core.arg()
