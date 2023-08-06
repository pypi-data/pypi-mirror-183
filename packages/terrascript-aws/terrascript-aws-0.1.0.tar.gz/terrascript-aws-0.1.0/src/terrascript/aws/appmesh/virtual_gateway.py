from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AccessLogFile(core.Schema):

    path: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        path: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AccessLogFile.Args(
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        path: Union[str, core.StringOut] = core.arg()


@core.schema
class AccessLog(core.Schema):

    file: Optional[AccessLogFile] = core.attr(AccessLogFile, default=None)

    def __init__(
        self,
        *,
        file: Optional[AccessLogFile] = None,
    ):
        super().__init__(
            args=AccessLog.Args(
                file=file,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file: Optional[AccessLogFile] = core.arg(default=None)


@core.schema
class Logging(core.Schema):

    access_log: Optional[AccessLog] = core.attr(AccessLog, default=None)

    def __init__(
        self,
        *,
        access_log: Optional[AccessLog] = None,
    ):
        super().__init__(
            args=Logging.Args(
                access_log=access_log,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_log: Optional[AccessLog] = core.arg(default=None)


@core.schema
class ClientPolicyTlsCertificateFile(core.Schema):

    certificate_chain: Union[str, core.StringOut] = core.attr(str)

    private_key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        certificate_chain: Union[str, core.StringOut],
        private_key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ClientPolicyTlsCertificateFile.Args(
                certificate_chain=certificate_chain,
                private_key=private_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_chain: Union[str, core.StringOut] = core.arg()

        private_key: Union[str, core.StringOut] = core.arg()


@core.schema
class Sds(core.Schema):

    secret_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        secret_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Sds.Args(
                secret_name=secret_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        secret_name: Union[str, core.StringOut] = core.arg()


@core.schema
class ClientPolicyTlsCertificate(core.Schema):

    file: Optional[ClientPolicyTlsCertificateFile] = core.attr(
        ClientPolicyTlsCertificateFile, default=None
    )

    sds: Optional[Sds] = core.attr(Sds, default=None)

    def __init__(
        self,
        *,
        file: Optional[ClientPolicyTlsCertificateFile] = None,
        sds: Optional[Sds] = None,
    ):
        super().__init__(
            args=ClientPolicyTlsCertificate.Args(
                file=file,
                sds=sds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file: Optional[ClientPolicyTlsCertificateFile] = core.arg(default=None)

        sds: Optional[Sds] = core.arg(default=None)


@core.schema
class ClientPolicyTlsValidationTrustFile(core.Schema):

    certificate_chain: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        certificate_chain: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ClientPolicyTlsValidationTrustFile.Args(
                certificate_chain=certificate_chain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_chain: Union[str, core.StringOut] = core.arg()


@core.schema
class ClientPolicyTlsValidationTrustAcm(core.Schema):

    certificate_authority_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        certificate_authority_arns: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=ClientPolicyTlsValidationTrustAcm.Args(
                certificate_authority_arns=certificate_authority_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_authority_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class ClientPolicyTlsValidationTrust(core.Schema):

    acm: Optional[ClientPolicyTlsValidationTrustAcm] = core.attr(
        ClientPolicyTlsValidationTrustAcm, default=None
    )

    file: Optional[ClientPolicyTlsValidationTrustFile] = core.attr(
        ClientPolicyTlsValidationTrustFile, default=None
    )

    sds: Optional[Sds] = core.attr(Sds, default=None)

    def __init__(
        self,
        *,
        acm: Optional[ClientPolicyTlsValidationTrustAcm] = None,
        file: Optional[ClientPolicyTlsValidationTrustFile] = None,
        sds: Optional[Sds] = None,
    ):
        super().__init__(
            args=ClientPolicyTlsValidationTrust.Args(
                acm=acm,
                file=file,
                sds=sds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acm: Optional[ClientPolicyTlsValidationTrustAcm] = core.arg(default=None)

        file: Optional[ClientPolicyTlsValidationTrustFile] = core.arg(default=None)

        sds: Optional[Sds] = core.arg(default=None)


@core.schema
class Match(core.Schema):

    exact: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        exact: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Match.Args(
                exact=exact,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exact: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class SubjectAlternativeNames(core.Schema):

    match: Match = core.attr(Match)

    def __init__(
        self,
        *,
        match: Match,
    ):
        super().__init__(
            args=SubjectAlternativeNames.Args(
                match=match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        match: Match = core.arg()


@core.schema
class ClientPolicyTlsValidation(core.Schema):

    subject_alternative_names: Optional[SubjectAlternativeNames] = core.attr(
        SubjectAlternativeNames, default=None
    )

    trust: ClientPolicyTlsValidationTrust = core.attr(ClientPolicyTlsValidationTrust)

    def __init__(
        self,
        *,
        trust: ClientPolicyTlsValidationTrust,
        subject_alternative_names: Optional[SubjectAlternativeNames] = None,
    ):
        super().__init__(
            args=ClientPolicyTlsValidation.Args(
                trust=trust,
                subject_alternative_names=subject_alternative_names,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subject_alternative_names: Optional[SubjectAlternativeNames] = core.arg(default=None)

        trust: ClientPolicyTlsValidationTrust = core.arg()


@core.schema
class ClientPolicyTls(core.Schema):

    certificate: Optional[ClientPolicyTlsCertificate] = core.attr(
        ClientPolicyTlsCertificate, default=None
    )

    enforce: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ports: Optional[Union[List[int], core.ArrayOut[core.IntOut]]] = core.attr(
        int, default=None, kind=core.Kind.array
    )

    validation: ClientPolicyTlsValidation = core.attr(ClientPolicyTlsValidation)

    def __init__(
        self,
        *,
        validation: ClientPolicyTlsValidation,
        certificate: Optional[ClientPolicyTlsCertificate] = None,
        enforce: Optional[Union[bool, core.BoolOut]] = None,
        ports: Optional[Union[List[int], core.ArrayOut[core.IntOut]]] = None,
    ):
        super().__init__(
            args=ClientPolicyTls.Args(
                validation=validation,
                certificate=certificate,
                enforce=enforce,
                ports=ports,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate: Optional[ClientPolicyTlsCertificate] = core.arg(default=None)

        enforce: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ports: Optional[Union[List[int], core.ArrayOut[core.IntOut]]] = core.arg(default=None)

        validation: ClientPolicyTlsValidation = core.arg()


@core.schema
class ClientPolicy(core.Schema):

    tls: Optional[ClientPolicyTls] = core.attr(ClientPolicyTls, default=None)

    def __init__(
        self,
        *,
        tls: Optional[ClientPolicyTls] = None,
    ):
        super().__init__(
            args=ClientPolicy.Args(
                tls=tls,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tls: Optional[ClientPolicyTls] = core.arg(default=None)


@core.schema
class BackendDefaults(core.Schema):

    client_policy: Optional[ClientPolicy] = core.attr(ClientPolicy, default=None)

    def __init__(
        self,
        *,
        client_policy: Optional[ClientPolicy] = None,
    ):
        super().__init__(
            args=BackendDefaults.Args(
                client_policy=client_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_policy: Optional[ClientPolicy] = core.arg(default=None)


@core.schema
class ListenerTlsCertificateAcm(core.Schema):

    certificate_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        certificate_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ListenerTlsCertificateAcm.Args(
                certificate_arn=certificate_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class ListenerTlsCertificate(core.Schema):

    acm: Optional[ListenerTlsCertificateAcm] = core.attr(ListenerTlsCertificateAcm, default=None)

    file: Optional[ClientPolicyTlsCertificateFile] = core.attr(
        ClientPolicyTlsCertificateFile, default=None
    )

    sds: Optional[Sds] = core.attr(Sds, default=None)

    def __init__(
        self,
        *,
        acm: Optional[ListenerTlsCertificateAcm] = None,
        file: Optional[ClientPolicyTlsCertificateFile] = None,
        sds: Optional[Sds] = None,
    ):
        super().__init__(
            args=ListenerTlsCertificate.Args(
                acm=acm,
                file=file,
                sds=sds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acm: Optional[ListenerTlsCertificateAcm] = core.arg(default=None)

        file: Optional[ClientPolicyTlsCertificateFile] = core.arg(default=None)

        sds: Optional[Sds] = core.arg(default=None)


@core.schema
class ListenerTlsValidationTrust(core.Schema):

    file: Optional[ClientPolicyTlsValidationTrustFile] = core.attr(
        ClientPolicyTlsValidationTrustFile, default=None
    )

    sds: Optional[Sds] = core.attr(Sds, default=None)

    def __init__(
        self,
        *,
        file: Optional[ClientPolicyTlsValidationTrustFile] = None,
        sds: Optional[Sds] = None,
    ):
        super().__init__(
            args=ListenerTlsValidationTrust.Args(
                file=file,
                sds=sds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file: Optional[ClientPolicyTlsValidationTrustFile] = core.arg(default=None)

        sds: Optional[Sds] = core.arg(default=None)


@core.schema
class ListenerTlsValidation(core.Schema):

    subject_alternative_names: Optional[SubjectAlternativeNames] = core.attr(
        SubjectAlternativeNames, default=None
    )

    trust: ListenerTlsValidationTrust = core.attr(ListenerTlsValidationTrust)

    def __init__(
        self,
        *,
        trust: ListenerTlsValidationTrust,
        subject_alternative_names: Optional[SubjectAlternativeNames] = None,
    ):
        super().__init__(
            args=ListenerTlsValidation.Args(
                trust=trust,
                subject_alternative_names=subject_alternative_names,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subject_alternative_names: Optional[SubjectAlternativeNames] = core.arg(default=None)

        trust: ListenerTlsValidationTrust = core.arg()


@core.schema
class ListenerTls(core.Schema):

    certificate: ListenerTlsCertificate = core.attr(ListenerTlsCertificate)

    mode: Union[str, core.StringOut] = core.attr(str)

    validation: Optional[ListenerTlsValidation] = core.attr(ListenerTlsValidation, default=None)

    def __init__(
        self,
        *,
        certificate: ListenerTlsCertificate,
        mode: Union[str, core.StringOut],
        validation: Optional[ListenerTlsValidation] = None,
    ):
        super().__init__(
            args=ListenerTls.Args(
                certificate=certificate,
                mode=mode,
                validation=validation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate: ListenerTlsCertificate = core.arg()

        mode: Union[str, core.StringOut] = core.arg()

        validation: Optional[ListenerTlsValidation] = core.arg(default=None)


@core.schema
class Grpc(core.Schema):

    max_requests: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        max_requests: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Grpc.Args(
                max_requests=max_requests,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_requests: Union[int, core.IntOut] = core.arg()


@core.schema
class Http(core.Schema):

    max_connections: Union[int, core.IntOut] = core.attr(int)

    max_pending_requests: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max_connections: Union[int, core.IntOut],
        max_pending_requests: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Http.Args(
                max_connections=max_connections,
                max_pending_requests=max_pending_requests,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_connections: Union[int, core.IntOut] = core.arg()

        max_pending_requests: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class Http2(core.Schema):

    max_requests: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        max_requests: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Http2.Args(
                max_requests=max_requests,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_requests: Union[int, core.IntOut] = core.arg()


@core.schema
class ConnectionPool(core.Schema):

    grpc: Optional[Grpc] = core.attr(Grpc, default=None)

    http: Optional[Http] = core.attr(Http, default=None)

    http2: Optional[Http2] = core.attr(Http2, default=None)

    def __init__(
        self,
        *,
        grpc: Optional[Grpc] = None,
        http: Optional[Http] = None,
        http2: Optional[Http2] = None,
    ):
        super().__init__(
            args=ConnectionPool.Args(
                grpc=grpc,
                http=http,
                http2=http2,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grpc: Optional[Grpc] = core.arg(default=None)

        http: Optional[Http] = core.arg(default=None)

        http2: Optional[Http2] = core.arg(default=None)


@core.schema
class HealthCheck(core.Schema):

    healthy_threshold: Union[int, core.IntOut] = core.attr(int)

    interval_millis: Union[int, core.IntOut] = core.attr(int)

    path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    protocol: Union[str, core.StringOut] = core.attr(str)

    timeout_millis: Union[int, core.IntOut] = core.attr(int)

    unhealthy_threshold: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        healthy_threshold: Union[int, core.IntOut],
        interval_millis: Union[int, core.IntOut],
        protocol: Union[str, core.StringOut],
        timeout_millis: Union[int, core.IntOut],
        unhealthy_threshold: Union[int, core.IntOut],
        path: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=HealthCheck.Args(
                healthy_threshold=healthy_threshold,
                interval_millis=interval_millis,
                protocol=protocol,
                timeout_millis=timeout_millis,
                unhealthy_threshold=unhealthy_threshold,
                path=path,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        healthy_threshold: Union[int, core.IntOut] = core.arg()

        interval_millis: Union[int, core.IntOut] = core.arg()

        path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        protocol: Union[str, core.StringOut] = core.arg()

        timeout_millis: Union[int, core.IntOut] = core.arg()

        unhealthy_threshold: Union[int, core.IntOut] = core.arg()


@core.schema
class PortMapping(core.Schema):

    port: Union[int, core.IntOut] = core.attr(int)

    protocol: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        port: Union[int, core.IntOut],
        protocol: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PortMapping.Args(
                port=port,
                protocol=protocol,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        port: Union[int, core.IntOut] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()


@core.schema
class Listener(core.Schema):

    connection_pool: Optional[ConnectionPool] = core.attr(ConnectionPool, default=None)

    health_check: Optional[HealthCheck] = core.attr(HealthCheck, default=None)

    port_mapping: PortMapping = core.attr(PortMapping)

    tls: Optional[ListenerTls] = core.attr(ListenerTls, default=None)

    def __init__(
        self,
        *,
        port_mapping: PortMapping,
        connection_pool: Optional[ConnectionPool] = None,
        health_check: Optional[HealthCheck] = None,
        tls: Optional[ListenerTls] = None,
    ):
        super().__init__(
            args=Listener.Args(
                port_mapping=port_mapping,
                connection_pool=connection_pool,
                health_check=health_check,
                tls=tls,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_pool: Optional[ConnectionPool] = core.arg(default=None)

        health_check: Optional[HealthCheck] = core.arg(default=None)

        port_mapping: PortMapping = core.arg()

        tls: Optional[ListenerTls] = core.arg(default=None)


@core.schema
class Spec(core.Schema):

    backend_defaults: Optional[BackendDefaults] = core.attr(BackendDefaults, default=None)

    listener: Listener = core.attr(Listener)

    logging: Optional[Logging] = core.attr(Logging, default=None)

    def __init__(
        self,
        *,
        listener: Listener,
        backend_defaults: Optional[BackendDefaults] = None,
        logging: Optional[Logging] = None,
    ):
        super().__init__(
            args=Spec.Args(
                listener=listener,
                backend_defaults=backend_defaults,
                logging=logging,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        backend_defaults: Optional[BackendDefaults] = core.arg(default=None)

        listener: Listener = core.arg()

        logging: Optional[Logging] = core.arg(default=None)


@core.resource(type="aws_appmesh_virtual_gateway", namespace="aws_appmesh")
class VirtualGateway(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    mesh_name: Union[str, core.StringOut] = core.attr(str)

    mesh_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    resource_owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    spec: Spec = core.attr(Spec)

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
        mesh_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        spec: Spec,
        mesh_owner: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VirtualGateway.Args(
                mesh_name=mesh_name,
                name=name,
                spec=spec,
                mesh_owner=mesh_owner,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        mesh_name: Union[str, core.StringOut] = core.arg()

        mesh_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        spec: Spec = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
