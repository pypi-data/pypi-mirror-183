from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class S3Logs(core.Schema):

    enable: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        enable: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=S3Logs.Args(
                enable=enable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable: Union[bool, core.BoolOut] = core.arg()


@core.schema
class AuditLogs(core.Schema):

    enable: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        enable: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=AuditLogs.Args(
                enable=enable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable: Union[bool, core.BoolOut] = core.arg()


@core.schema
class Kubernetes(core.Schema):

    audit_logs: AuditLogs = core.attr(AuditLogs)

    def __init__(
        self,
        *,
        audit_logs: AuditLogs,
    ):
        super().__init__(
            args=Kubernetes.Args(
                audit_logs=audit_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        audit_logs: AuditLogs = core.arg()


@core.schema
class EbsVolumes(core.Schema):

    enable: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        enable: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=EbsVolumes.Args(
                enable=enable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable: Union[bool, core.BoolOut] = core.arg()


@core.schema
class ScanEc2InstanceWithFindings(core.Schema):

    ebs_volumes: EbsVolumes = core.attr(EbsVolumes)

    def __init__(
        self,
        *,
        ebs_volumes: EbsVolumes,
    ):
        super().__init__(
            args=ScanEc2InstanceWithFindings.Args(
                ebs_volumes=ebs_volumes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ebs_volumes: EbsVolumes = core.arg()


@core.schema
class MalwareProtection(core.Schema):

    scan_ec2_instance_with_findings: ScanEc2InstanceWithFindings = core.attr(
        ScanEc2InstanceWithFindings
    )

    def __init__(
        self,
        *,
        scan_ec2_instance_with_findings: ScanEc2InstanceWithFindings,
    ):
        super().__init__(
            args=MalwareProtection.Args(
                scan_ec2_instance_with_findings=scan_ec2_instance_with_findings,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        scan_ec2_instance_with_findings: ScanEc2InstanceWithFindings = core.arg()


@core.schema
class Datasources(core.Schema):

    kubernetes: Optional[Kubernetes] = core.attr(Kubernetes, default=None, computed=True)

    malware_protection: Optional[MalwareProtection] = core.attr(
        MalwareProtection, default=None, computed=True
    )

    s3_logs: Optional[S3Logs] = core.attr(S3Logs, default=None, computed=True)

    def __init__(
        self,
        *,
        kubernetes: Optional[Kubernetes] = None,
        malware_protection: Optional[MalwareProtection] = None,
        s3_logs: Optional[S3Logs] = None,
    ):
        super().__init__(
            args=Datasources.Args(
                kubernetes=kubernetes,
                malware_protection=malware_protection,
                s3_logs=s3_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kubernetes: Optional[Kubernetes] = core.arg(default=None)

        malware_protection: Optional[MalwareProtection] = core.arg(default=None)

        s3_logs: Optional[S3Logs] = core.arg(default=None)


@core.resource(type="aws_guardduty_detector", namespace="aws_guardduty")
class Detector(core.Resource):

    account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    datasources: Optional[Datasources] = core.attr(Datasources, default=None, computed=True)

    enable: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    finding_publishing_frequency: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        datasources: Optional[Datasources] = None,
        enable: Optional[Union[bool, core.BoolOut]] = None,
        finding_publishing_frequency: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Detector.Args(
                datasources=datasources,
                enable=enable,
                finding_publishing_frequency=finding_publishing_frequency,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        datasources: Optional[Datasources] = core.arg(default=None)

        enable: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        finding_publishing_frequency: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
