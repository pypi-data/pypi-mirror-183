from typing import List, Optional, Union

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


@core.data(type="aws_cloudhsm_v2_cluster", namespace="aws_cloudhsm")
class DsV2Cluster(core.Data):

    cluster_certificates: Union[
        List[ClusterCertificates], core.ArrayOut[ClusterCertificates]
    ] = core.attr(ClusterCertificates, computed=True, kind=core.Kind.array)

    cluster_id: Union[str, core.StringOut] = core.attr(str)

    cluster_state: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cluster_id: Union[str, core.StringOut],
        cluster_state: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsV2Cluster.Args(
                cluster_id=cluster_id,
                cluster_state=cluster_state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_id: Union[str, core.StringOut] = core.arg()

        cluster_state: Optional[Union[str, core.StringOut]] = core.arg(default=None)
