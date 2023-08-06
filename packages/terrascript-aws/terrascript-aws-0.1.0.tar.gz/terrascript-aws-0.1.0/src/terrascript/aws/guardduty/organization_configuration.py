from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class S3Logs(core.Schema):

    auto_enable: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        auto_enable: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=S3Logs.Args(
                auto_enable=auto_enable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_enable: Union[bool, core.BoolOut] = core.arg()


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

    auto_enable: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        auto_enable: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=EbsVolumes.Args(
                auto_enable=auto_enable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_enable: Union[bool, core.BoolOut] = core.arg()


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


@core.resource(type="aws_guardduty_organization_configuration", namespace="aws_guardduty")
class OrganizationConfiguration(core.Resource):

    auto_enable: Union[bool, core.BoolOut] = core.attr(bool)

    datasources: Optional[Datasources] = core.attr(Datasources, default=None, computed=True)

    detector_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        auto_enable: Union[bool, core.BoolOut],
        detector_id: Union[str, core.StringOut],
        datasources: Optional[Datasources] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationConfiguration.Args(
                auto_enable=auto_enable,
                detector_id=detector_id,
                datasources=datasources,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_enable: Union[bool, core.BoolOut] = core.arg()

        datasources: Optional[Datasources] = core.arg(default=None)

        detector_id: Union[str, core.StringOut] = core.arg()
