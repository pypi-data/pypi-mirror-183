from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class S3Destination(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str)

    encryption_disabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    encryption_key: Union[str, core.StringOut] = core.attr(str)

    packaging: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        encryption_key: Union[str, core.StringOut],
        encryption_disabled: Optional[Union[bool, core.BoolOut]] = None,
        packaging: Optional[Union[str, core.StringOut]] = None,
        path: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3Destination.Args(
                bucket=bucket,
                encryption_key=encryption_key,
                encryption_disabled=encryption_disabled,
                packaging=packaging,
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        encryption_disabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        encryption_key: Union[str, core.StringOut] = core.arg()

        packaging: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        path: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ExportConfig(core.Schema):

    s3_destination: Optional[S3Destination] = core.attr(S3Destination, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        s3_destination: Optional[S3Destination] = None,
    ):
        super().__init__(
            args=ExportConfig.Args(
                type=type,
                s3_destination=s3_destination,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_destination: Optional[S3Destination] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_codebuild_report_group", namespace="aws_codebuild")
class ReportGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created: Union[str, core.StringOut] = core.attr(str, computed=True)

    delete_reports: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    export_config: ExportConfig = core.attr(ExportConfig)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        export_config: ExportConfig,
        name: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        delete_reports: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReportGroup.Args(
                export_config=export_config,
                name=name,
                type=type,
                delete_reports=delete_reports,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delete_reports: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        export_config: ExportConfig = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Union[str, core.StringOut] = core.arg()
