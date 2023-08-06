from typing import Dict, List, Optional, Union

import terrascript.core as core


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
class VirtualService(core.Schema):

    client_policy: Optional[ClientPolicy] = core.attr(ClientPolicy, default=None)

    virtual_service_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        virtual_service_name: Union[str, core.StringOut],
        client_policy: Optional[ClientPolicy] = None,
    ):
        super().__init__(
            args=VirtualService.Args(
                virtual_service_name=virtual_service_name,
                client_policy=client_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_policy: Optional[ClientPolicy] = core.arg(default=None)

        virtual_service_name: Union[str, core.StringOut] = core.arg()


@core.schema
class Backend(core.Schema):

    virtual_service: VirtualService = core.attr(VirtualService)

    def __init__(
        self,
        *,
        virtual_service: VirtualService,
    ):
        super().__init__(
            args=Backend.Args(
                virtual_service=virtual_service,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        virtual_service: VirtualService = core.arg()


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
class PerRequest(core.Schema):

    unit: Union[str, core.StringOut] = core.attr(str)

    value: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        unit: Union[str, core.StringOut],
        value: Union[int, core.IntOut],
    ):
        super().__init__(
            args=PerRequest.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: Union[str, core.StringOut] = core.arg()

        value: Union[int, core.IntOut] = core.arg()


@core.schema
class Idle(core.Schema):

    unit: Union[str, core.StringOut] = core.attr(str)

    value: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        unit: Union[str, core.StringOut],
        value: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Idle.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: Union[str, core.StringOut] = core.arg()

        value: Union[int, core.IntOut] = core.arg()


@core.schema
class TimeoutGrpc(core.Schema):

    idle: Optional[Idle] = core.attr(Idle, default=None)

    per_request: Optional[PerRequest] = core.attr(PerRequest, default=None)

    def __init__(
        self,
        *,
        idle: Optional[Idle] = None,
        per_request: Optional[PerRequest] = None,
    ):
        super().__init__(
            args=TimeoutGrpc.Args(
                idle=idle,
                per_request=per_request,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        idle: Optional[Idle] = core.arg(default=None)

        per_request: Optional[PerRequest] = core.arg(default=None)


@core.schema
class TimeoutHttp(core.Schema):

    idle: Optional[Idle] = core.attr(Idle, default=None)

    per_request: Optional[PerRequest] = core.attr(PerRequest, default=None)

    def __init__(
        self,
        *,
        idle: Optional[Idle] = None,
        per_request: Optional[PerRequest] = None,
    ):
        super().__init__(
            args=TimeoutHttp.Args(
                idle=idle,
                per_request=per_request,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        idle: Optional[Idle] = core.arg(default=None)

        per_request: Optional[PerRequest] = core.arg(default=None)


@core.schema
class TimeoutHttp2(core.Schema):

    idle: Optional[Idle] = core.attr(Idle, default=None)

    per_request: Optional[PerRequest] = core.attr(PerRequest, default=None)

    def __init__(
        self,
        *,
        idle: Optional[Idle] = None,
        per_request: Optional[PerRequest] = None,
    ):
        super().__init__(
            args=TimeoutHttp2.Args(
                idle=idle,
                per_request=per_request,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        idle: Optional[Idle] = core.arg(default=None)

        per_request: Optional[PerRequest] = core.arg(default=None)


@core.schema
class TimeoutTcp(core.Schema):

    idle: Optional[Idle] = core.attr(Idle, default=None)

    def __init__(
        self,
        *,
        idle: Optional[Idle] = None,
    ):
        super().__init__(
            args=TimeoutTcp.Args(
                idle=idle,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        idle: Optional[Idle] = core.arg(default=None)


@core.schema
class Timeout(core.Schema):

    grpc: Optional[TimeoutGrpc] = core.attr(TimeoutGrpc, default=None)

    http: Optional[TimeoutHttp] = core.attr(TimeoutHttp, default=None)

    http2: Optional[TimeoutHttp2] = core.attr(TimeoutHttp2, default=None)

    tcp: Optional[TimeoutTcp] = core.attr(TimeoutTcp, default=None)

    def __init__(
        self,
        *,
        grpc: Optional[TimeoutGrpc] = None,
        http: Optional[TimeoutHttp] = None,
        http2: Optional[TimeoutHttp2] = None,
        tcp: Optional[TimeoutTcp] = None,
    ):
        super().__init__(
            args=Timeout.Args(
                grpc=grpc,
                http=http,
                http2=http2,
                tcp=tcp,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grpc: Optional[TimeoutGrpc] = core.arg(default=None)

        http: Optional[TimeoutHttp] = core.arg(default=None)

        http2: Optional[TimeoutHttp2] = core.arg(default=None)

        tcp: Optional[TimeoutTcp] = core.arg(default=None)


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
class ConnectionPoolTcp(core.Schema):

    max_connections: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        max_connections: Union[int, core.IntOut],
    ):
        super().__init__(
            args=ConnectionPoolTcp.Args(
                max_connections=max_connections,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_connections: Union[int, core.IntOut] = core.arg()


@core.schema
class ConnectionPoolGrpc(core.Schema):

    max_requests: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        max_requests: Union[int, core.IntOut],
    ):
        super().__init__(
            args=ConnectionPoolGrpc.Args(
                max_requests=max_requests,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_requests: Union[int, core.IntOut] = core.arg()


@core.schema
class ConnectionPoolHttp(core.Schema):

    max_connections: Union[int, core.IntOut] = core.attr(int)

    max_pending_requests: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max_connections: Union[int, core.IntOut],
        max_pending_requests: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ConnectionPoolHttp.Args(
                max_connections=max_connections,
                max_pending_requests=max_pending_requests,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_connections: Union[int, core.IntOut] = core.arg()

        max_pending_requests: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class ConnectionPoolHttp2(core.Schema):

    max_requests: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        max_requests: Union[int, core.IntOut],
    ):
        super().__init__(
            args=ConnectionPoolHttp2.Args(
                max_requests=max_requests,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_requests: Union[int, core.IntOut] = core.arg()


@core.schema
class ConnectionPool(core.Schema):

    grpc: Optional[ConnectionPoolGrpc] = core.attr(ConnectionPoolGrpc, default=None)

    http: Optional[ConnectionPoolHttp] = core.attr(ConnectionPoolHttp, default=None)

    http2: Optional[ConnectionPoolHttp2] = core.attr(ConnectionPoolHttp2, default=None)

    tcp: Optional[ConnectionPoolTcp] = core.attr(ConnectionPoolTcp, default=None)

    def __init__(
        self,
        *,
        grpc: Optional[ConnectionPoolGrpc] = None,
        http: Optional[ConnectionPoolHttp] = None,
        http2: Optional[ConnectionPoolHttp2] = None,
        tcp: Optional[ConnectionPoolTcp] = None,
    ):
        super().__init__(
            args=ConnectionPool.Args(
                grpc=grpc,
                http=http,
                http2=http2,
                tcp=tcp,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grpc: Optional[ConnectionPoolGrpc] = core.arg(default=None)

        http: Optional[ConnectionPoolHttp] = core.arg(default=None)

        http2: Optional[ConnectionPoolHttp2] = core.arg(default=None)

        tcp: Optional[ConnectionPoolTcp] = core.arg(default=None)


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
class BaseEjectionDuration(core.Schema):

    unit: Union[str, core.StringOut] = core.attr(str)

    value: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        unit: Union[str, core.StringOut],
        value: Union[int, core.IntOut],
    ):
        super().__init__(
            args=BaseEjectionDuration.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: Union[str, core.StringOut] = core.arg()

        value: Union[int, core.IntOut] = core.arg()


@core.schema
class Interval(core.Schema):

    unit: Union[str, core.StringOut] = core.attr(str)

    value: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        unit: Union[str, core.StringOut],
        value: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Interval.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: Union[str, core.StringOut] = core.arg()

        value: Union[int, core.IntOut] = core.arg()


@core.schema
class OutlierDetection(core.Schema):

    base_ejection_duration: BaseEjectionDuration = core.attr(BaseEjectionDuration)

    interval: Interval = core.attr(Interval)

    max_ejection_percent: Union[int, core.IntOut] = core.attr(int)

    max_server_errors: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        base_ejection_duration: BaseEjectionDuration,
        interval: Interval,
        max_ejection_percent: Union[int, core.IntOut],
        max_server_errors: Union[int, core.IntOut],
    ):
        super().__init__(
            args=OutlierDetection.Args(
                base_ejection_duration=base_ejection_duration,
                interval=interval,
                max_ejection_percent=max_ejection_percent,
                max_server_errors=max_server_errors,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        base_ejection_duration: BaseEjectionDuration = core.arg()

        interval: Interval = core.arg()

        max_ejection_percent: Union[int, core.IntOut] = core.arg()

        max_server_errors: Union[int, core.IntOut] = core.arg()


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

    outlier_detection: Optional[OutlierDetection] = core.attr(OutlierDetection, default=None)

    port_mapping: PortMapping = core.attr(PortMapping)

    timeout: Optional[Timeout] = core.attr(Timeout, default=None)

    tls: Optional[ListenerTls] = core.attr(ListenerTls, default=None)

    def __init__(
        self,
        *,
        port_mapping: PortMapping,
        connection_pool: Optional[ConnectionPool] = None,
        health_check: Optional[HealthCheck] = None,
        outlier_detection: Optional[OutlierDetection] = None,
        timeout: Optional[Timeout] = None,
        tls: Optional[ListenerTls] = None,
    ):
        super().__init__(
            args=Listener.Args(
                port_mapping=port_mapping,
                connection_pool=connection_pool,
                health_check=health_check,
                outlier_detection=outlier_detection,
                timeout=timeout,
                tls=tls,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_pool: Optional[ConnectionPool] = core.arg(default=None)

        health_check: Optional[HealthCheck] = core.arg(default=None)

        outlier_detection: Optional[OutlierDetection] = core.arg(default=None)

        port_mapping: PortMapping = core.arg()

        timeout: Optional[Timeout] = core.arg(default=None)

        tls: Optional[ListenerTls] = core.arg(default=None)


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
class AwsCloudMap(core.Schema):

    attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    namespace_name: Union[str, core.StringOut] = core.attr(str)

    service_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        namespace_name: Union[str, core.StringOut],
        service_name: Union[str, core.StringOut],
        attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AwsCloudMap.Args(
                namespace_name=namespace_name,
                service_name=service_name,
                attributes=attributes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        namespace_name: Union[str, core.StringOut] = core.arg()

        service_name: Union[str, core.StringOut] = core.arg()


@core.schema
class Dns(core.Schema):

    hostname: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        hostname: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Dns.Args(
                hostname=hostname,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hostname: Union[str, core.StringOut] = core.arg()


@core.schema
class ServiceDiscovery(core.Schema):

    aws_cloud_map: Optional[AwsCloudMap] = core.attr(AwsCloudMap, default=None)

    dns: Optional[Dns] = core.attr(Dns, default=None)

    def __init__(
        self,
        *,
        aws_cloud_map: Optional[AwsCloudMap] = None,
        dns: Optional[Dns] = None,
    ):
        super().__init__(
            args=ServiceDiscovery.Args(
                aws_cloud_map=aws_cloud_map,
                dns=dns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_cloud_map: Optional[AwsCloudMap] = core.arg(default=None)

        dns: Optional[Dns] = core.arg(default=None)


@core.schema
class Spec(core.Schema):

    backend: Optional[Union[List[Backend], core.ArrayOut[Backend]]] = core.attr(
        Backend, default=None, kind=core.Kind.array
    )

    backend_defaults: Optional[BackendDefaults] = core.attr(BackendDefaults, default=None)

    listener: Optional[Listener] = core.attr(Listener, default=None)

    logging: Optional[Logging] = core.attr(Logging, default=None)

    service_discovery: Optional[ServiceDiscovery] = core.attr(ServiceDiscovery, default=None)

    def __init__(
        self,
        *,
        backend: Optional[Union[List[Backend], core.ArrayOut[Backend]]] = None,
        backend_defaults: Optional[BackendDefaults] = None,
        listener: Optional[Listener] = None,
        logging: Optional[Logging] = None,
        service_discovery: Optional[ServiceDiscovery] = None,
    ):
        super().__init__(
            args=Spec.Args(
                backend=backend,
                backend_defaults=backend_defaults,
                listener=listener,
                logging=logging,
                service_discovery=service_discovery,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        backend: Optional[Union[List[Backend], core.ArrayOut[Backend]]] = core.arg(default=None)

        backend_defaults: Optional[BackendDefaults] = core.arg(default=None)

        listener: Optional[Listener] = core.arg(default=None)

        logging: Optional[Logging] = core.arg(default=None)

        service_discovery: Optional[ServiceDiscovery] = core.arg(default=None)


@core.resource(type="aws_appmesh_virtual_node", namespace="aws_appmesh")
class VirtualNode(core.Resource):

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
            args=VirtualNode.Args(
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
