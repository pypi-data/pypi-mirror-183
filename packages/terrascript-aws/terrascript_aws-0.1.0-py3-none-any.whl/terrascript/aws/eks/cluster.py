from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Provider(core.Schema):

    key_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Provider.Args(
                key_arn=key_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class EncryptionConfig(core.Schema):

    provider: Provider = core.attr(Provider)

    resources: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        provider: Provider,
        resources: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=EncryptionConfig.Args(
                provider=provider,
                resources=resources,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        provider: Provider = core.arg()

        resources: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


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

    ip_family: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    service_ipv4_cidr: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        ip_family: Optional[Union[str, core.StringOut]] = None,
        service_ipv4_cidr: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=KubernetesNetworkConfig.Args(
                ip_family=ip_family,
                service_ipv4_cidr=service_ipv4_cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip_family: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_ipv4_cidr: Optional[Union[str, core.StringOut]] = core.arg(default=None)


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

    endpoint_private_access: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    endpoint_public_access: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    public_access_cidrs: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cluster_security_group_id: Union[str, core.StringOut],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_id: Union[str, core.StringOut],
        endpoint_private_access: Optional[Union[bool, core.BoolOut]] = None,
        endpoint_public_access: Optional[Union[bool, core.BoolOut]] = None,
        public_access_cidrs: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=VpcConfig.Args(
                cluster_security_group_id=cluster_security_group_id,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
                endpoint_private_access=endpoint_private_access,
                endpoint_public_access=endpoint_public_access,
                public_access_cidrs=public_access_cidrs,
                security_group_ids=security_group_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_security_group_id: Union[str, core.StringOut] = core.arg()

        endpoint_private_access: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        endpoint_public_access: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        public_access_cidrs: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_eks_cluster", namespace="aws_eks")
class Cluster(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_authority: Union[
        List[CertificateAuthority], core.ArrayOut[CertificateAuthority]
    ] = core.attr(CertificateAuthority, computed=True, kind=core.Kind.array)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled_cluster_log_types: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    encryption_config: Optional[EncryptionConfig] = core.attr(EncryptionConfig, default=None)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity: Union[List[Identity], core.ArrayOut[Identity]] = core.attr(
        Identity, computed=True, kind=core.Kind.array
    )

    kubernetes_network_config: Optional[KubernetesNetworkConfig] = core.attr(
        KubernetesNetworkConfig, default=None, computed=True
    )

    name: Union[str, core.StringOut] = core.attr(str)

    platform_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    vpc_config: VpcConfig = core.attr(VpcConfig)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        vpc_config: VpcConfig,
        enabled_cluster_log_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        encryption_config: Optional[EncryptionConfig] = None,
        kubernetes_network_config: Optional[KubernetesNetworkConfig] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        version: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                name=name,
                role_arn=role_arn,
                vpc_config=vpc_config,
                enabled_cluster_log_types=enabled_cluster_log_types,
                encryption_config=encryption_config,
                kubernetes_network_config=kubernetes_network_config,
                tags=tags,
                tags_all=tags_all,
                version=version,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        enabled_cluster_log_types: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        encryption_config: Optional[EncryptionConfig] = core.arg(default=None)

        kubernetes_network_config: Optional[KubernetesNetworkConfig] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_config: VpcConfig = core.arg()
