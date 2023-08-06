from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Oidc(core.Schema):

    issuer: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        issuer: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Oidc.Args(
                issuer=issuer,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        issuer: Union[str, core.StringOut] = core.arg()


@core.schema
class Identity(core.Schema):

    oidc: Union[List[Oidc], core.ArrayOut[Oidc]] = core.attr(
        Oidc, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        oidc: Union[List[Oidc], core.ArrayOut[Oidc]],
    ):
        super().__init__(
            args=Identity.Args(
                oidc=oidc,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        oidc: Union[List[Oidc], core.ArrayOut[Oidc]] = core.arg()


@core.schema
class KubernetesNetworkConfig(core.Schema):

    ip_family: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_ipv4_cidr: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        ip_family: Union[str, core.StringOut],
        service_ipv4_cidr: Union[str, core.StringOut],
    ):
        super().__init__(
            args=KubernetesNetworkConfig.Args(
                ip_family=ip_family,
                service_ipv4_cidr=service_ipv4_cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip_family: Union[str, core.StringOut] = core.arg()

        service_ipv4_cidr: Union[str, core.StringOut] = core.arg()


@core.schema
class CertificateAuthority(core.Schema):

    data: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        data: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CertificateAuthority.Args(
                data=data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data: Union[str, core.StringOut] = core.arg()


@core.schema
class VpcConfig(core.Schema):

    cluster_security_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint_private_access: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    endpoint_public_access: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    public_access_cidrs: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cluster_security_group_id: Union[str, core.StringOut],
        endpoint_private_access: Union[bool, core.BoolOut],
        endpoint_public_access: Union[bool, core.BoolOut],
        public_access_cidrs: Union[List[str], core.ArrayOut[core.StringOut]],
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpcConfig.Args(
                cluster_security_group_id=cluster_security_group_id,
                endpoint_private_access=endpoint_private_access,
                endpoint_public_access=endpoint_public_access,
                public_access_cidrs=public_access_cidrs,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_security_group_id: Union[str, core.StringOut] = core.arg()

        endpoint_private_access: Union[bool, core.BoolOut] = core.arg()

        endpoint_public_access: Union[bool, core.BoolOut] = core.arg()

        public_access_cidrs: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_eks_cluster", namespace="aws_eks")
class DsCluster(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_authority: Union[
        List[CertificateAuthority], core.ArrayOut[CertificateAuthority]
    ] = core.attr(CertificateAuthority, computed=True, kind=core.Kind.array)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled_cluster_log_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity: Union[List[Identity], core.ArrayOut[Identity]] = core.attr(
        Identity, computed=True, kind=core.Kind.array
    )

    kubernetes_network_config: Union[
        List[KubernetesNetworkConfig], core.ArrayOut[KubernetesNetworkConfig]
    ] = core.attr(KubernetesNetworkConfig, computed=True, kind=core.Kind.array)

    name: Union[str, core.StringOut] = core.attr(str)

    platform_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_config: Union[List[VpcConfig], core.ArrayOut[VpcConfig]] = core.attr(
        VpcConfig, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCluster.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
