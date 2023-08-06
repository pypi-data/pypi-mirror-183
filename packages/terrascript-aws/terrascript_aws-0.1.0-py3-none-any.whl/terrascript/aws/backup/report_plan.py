from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ReportDeliveryChannel(core.Schema):

    formats: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    s3_bucket_name: Union[str, core.StringOut] = core.attr(str)

    s3_key_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_bucket_name: Union[str, core.StringOut],
        formats: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        s3_key_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ReportDeliveryChannel.Args(
                s3_bucket_name=s3_bucket_name,
                formats=formats,
                s3_key_prefix=s3_key_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        formats: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        s3_bucket_name: Union[str, core.StringOut] = core.arg()

        s3_key_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ReportSetting(core.Schema):

    framework_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    number_of_frameworks: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    report_template: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        report_template: Union[str, core.StringOut],
        framework_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        number_of_frameworks: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ReportSetting.Args(
                report_template=report_template,
                framework_arns=framework_arns,
                number_of_frameworks=number_of_frameworks,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        framework_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        number_of_frameworks: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        report_template: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_backup_report_plan", namespace="aws_backup")
class ReportPlan(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    creation_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    deployment_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    report_delivery_channel: ReportDeliveryChannel = core.attr(ReportDeliveryChannel)

    report_setting: ReportSetting = core.attr(ReportSetting)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        report_delivery_channel: ReportDeliveryChannel,
        report_setting: ReportSetting,
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReportPlan.Args(
                name=name,
                report_delivery_channel=report_delivery_channel,
                report_setting=report_setting,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        report_delivery_channel: ReportDeliveryChannel = core.arg()

        report_setting: ReportSetting = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
