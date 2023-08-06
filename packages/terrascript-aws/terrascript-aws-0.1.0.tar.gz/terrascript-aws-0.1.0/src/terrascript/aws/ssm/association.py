from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Targets(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Targets.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class OutputLocation(core.Schema):

    s3_bucket_name: Union[str, core.StringOut] = core.attr(str)

    s3_key_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_bucket_name: Union[str, core.StringOut],
        s3_key_prefix: Optional[Union[str, core.StringOut]] = None,
        s3_region: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=OutputLocation.Args(
                s3_bucket_name=s3_bucket_name,
                s3_key_prefix=s3_key_prefix,
                s3_region=s3_region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_bucket_name: Union[str, core.StringOut] = core.arg()

        s3_key_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_ssm_association", namespace="aws_ssm")
class Association(core.Resource):

    apply_only_at_cron_interval: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    association_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    association_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    automation_target_parameter_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    compliance_severity: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    document_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_concurrency: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_errors: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    output_location: Optional[OutputLocation] = core.attr(OutputLocation, default=None)

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    schedule_expression: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    targets: Optional[Union[List[Targets], core.ArrayOut[Targets]]] = core.attr(
        Targets, default=None, computed=True, kind=core.Kind.array
    )

    wait_for_success_timeout_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        apply_only_at_cron_interval: Optional[Union[bool, core.BoolOut]] = None,
        association_name: Optional[Union[str, core.StringOut]] = None,
        automation_target_parameter_name: Optional[Union[str, core.StringOut]] = None,
        compliance_severity: Optional[Union[str, core.StringOut]] = None,
        document_version: Optional[Union[str, core.StringOut]] = None,
        instance_id: Optional[Union[str, core.StringOut]] = None,
        max_concurrency: Optional[Union[str, core.StringOut]] = None,
        max_errors: Optional[Union[str, core.StringOut]] = None,
        output_location: Optional[OutputLocation] = None,
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        schedule_expression: Optional[Union[str, core.StringOut]] = None,
        targets: Optional[Union[List[Targets], core.ArrayOut[Targets]]] = None,
        wait_for_success_timeout_seconds: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Association.Args(
                name=name,
                apply_only_at_cron_interval=apply_only_at_cron_interval,
                association_name=association_name,
                automation_target_parameter_name=automation_target_parameter_name,
                compliance_severity=compliance_severity,
                document_version=document_version,
                instance_id=instance_id,
                max_concurrency=max_concurrency,
                max_errors=max_errors,
                output_location=output_location,
                parameters=parameters,
                schedule_expression=schedule_expression,
                targets=targets,
                wait_for_success_timeout_seconds=wait_for_success_timeout_seconds,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        apply_only_at_cron_interval: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        association_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        automation_target_parameter_name: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        compliance_severity: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        document_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_concurrency: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_errors: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        output_location: Optional[OutputLocation] = core.arg(default=None)

        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        schedule_expression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        targets: Optional[Union[List[Targets], core.ArrayOut[Targets]]] = core.arg(default=None)

        wait_for_success_timeout_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)
