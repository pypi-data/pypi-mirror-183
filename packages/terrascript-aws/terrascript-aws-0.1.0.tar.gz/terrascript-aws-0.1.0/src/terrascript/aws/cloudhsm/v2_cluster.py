from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ClusterCertificates(core.Schema):

    aws_hardware_certificate: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_certificate: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_csr: Union[str, core.StringOut] = core.attr(str, computed=True)

    hsm_certificate: Union[str, core.StringOut] = core.attr(str, computed=True)

    manufacturer_hardware_certificate: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        aws_hardware_certificate: Union[str, core.StringOut],
        cluster_certificate: Union[str, core.StringOut],
        cluster_csr: Union[str, core.StringOut],
        hsm_certificate: Union[str, core.StringOut],
        manufacturer_hardware_certificate: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ClusterCertificates.Args(
                aws_hardware_certificate=aws_hardware_certificate,
                cluster_certificate=cluster_certificate,
                cluster_csr=cluster_csr,
                hsm_certificate=hsm_certificate,
                manufacturer_hardware_certificate=manufacturer_hardware_certificate,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_hardware_certificate: Union[str, core.StringOut] = core.arg()

        cluster_certificate: Union[str, core.StringOut] = core.arg()

        cluster_csr: Union[str, core.StringOut] = core.arg()

        hsm_certificate: Union[str, core.StringOut] = core.arg()

        manufacturer_hardware_certificate: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_cloudhsm_v2_cluster", namespace="aws_cloudhsm")
class V2Cluster(core.Resource):

    cluster_certificates: Union[
        List[ClusterCertificates], core.ArrayOut[ClusterCertificates]
    ] = core.attr(ClusterCertificates, computed=True, kind=core.Kind.array)

    cluster_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_state: Union[str, core.StringOut] = core.attr(str, computed=True)

    hsm_type: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_backup_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        hsm_type: Union[str, core.StringOut],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        source_backup_identifier: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=V2Cluster.Args(
                hsm_type=hsm_type,
                subnet_ids=subnet_ids,
                source_backup_identifier=source_backup_identifier,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        hsm_type: Union[str, core.StringOut] = core.arg()

        source_backup_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
