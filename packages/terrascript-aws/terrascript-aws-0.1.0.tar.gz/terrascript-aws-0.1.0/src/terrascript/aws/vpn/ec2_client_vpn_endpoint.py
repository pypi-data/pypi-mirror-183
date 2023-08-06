from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ClientLoginBannerOptions(core.Schema):

    banner_text: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        *,
        banner_text: Optional[Union[str, core.StringOut]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=ClientLoginBannerOptions.Args(
                banner_text=banner_text,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        banner_text: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class ClientConnectOptions(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    lambda_function_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        lambda_function_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ClientConnectOptions.Args(
                enabled=enabled,
                lambda_function_arn=lambda_function_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        lambda_function_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AuthenticationOptions(core.Schema):

    active_directory_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    root_certificate_chain_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    saml_provider_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    self_service_saml_provider_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        active_directory_id: Optional[Union[str, core.StringOut]] = None,
        root_certificate_chain_arn: Optional[Union[str, core.StringOut]] = None,
        saml_provider_arn: Optional[Union[str, core.StringOut]] = None,
        self_service_saml_provider_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AuthenticationOptions.Args(
                type=type,
                active_directory_id=active_directory_id,
                root_certificate_chain_arn=root_certificate_chain_arn,
                saml_provider_arn=saml_provider_arn,
                self_service_saml_provider_arn=self_service_saml_provider_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        active_directory_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        root_certificate_chain_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        saml_provider_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        self_service_saml_provider_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class ConnectionLogOptions(core.Schema):

    cloudwatch_log_group: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudwatch_log_stream: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        cloudwatch_log_group: Optional[Union[str, core.StringOut]] = None,
        cloudwatch_log_stream: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ConnectionLogOptions.Args(
                enabled=enabled,
                cloudwatch_log_group=cloudwatch_log_group,
                cloudwatch_log_stream=cloudwatch_log_stream,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_log_group: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudwatch_log_stream: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Union[bool, core.BoolOut] = core.arg()


@core.resource(type="aws_ec2_client_vpn_endpoint", namespace="aws_vpn")
class Ec2ClientVpnEndpoint(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authentication_options: Union[
        List[AuthenticationOptions], core.ArrayOut[AuthenticationOptions]
    ] = core.attr(AuthenticationOptions, kind=core.Kind.array)

    client_cidr_block: Union[str, core.StringOut] = core.attr(str)

    client_connect_options: Optional[ClientConnectOptions] = core.attr(
        ClientConnectOptions, default=None, computed=True
    )

    client_login_banner_options: Optional[ClientLoginBannerOptions] = core.attr(
        ClientLoginBannerOptions, default=None, computed=True
    )

    connection_log_options: ConnectionLogOptions = core.attr(ConnectionLogOptions)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    dns_servers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    self_service_portal: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    server_certificate_arn: Union[str, core.StringOut] = core.attr(str)

    session_timeout_hours: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    split_tunnel: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transport_protocol: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    vpn_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        authentication_options: Union[
            List[AuthenticationOptions], core.ArrayOut[AuthenticationOptions]
        ],
        client_cidr_block: Union[str, core.StringOut],
        connection_log_options: ConnectionLogOptions,
        server_certificate_arn: Union[str, core.StringOut],
        client_connect_options: Optional[ClientConnectOptions] = None,
        client_login_banner_options: Optional[ClientLoginBannerOptions] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        dns_servers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        self_service_portal: Optional[Union[str, core.StringOut]] = None,
        session_timeout_hours: Optional[Union[int, core.IntOut]] = None,
        split_tunnel: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        transport_protocol: Optional[Union[str, core.StringOut]] = None,
        vpc_id: Optional[Union[str, core.StringOut]] = None,
        vpn_port: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2ClientVpnEndpoint.Args(
                authentication_options=authentication_options,
                client_cidr_block=client_cidr_block,
                connection_log_options=connection_log_options,
                server_certificate_arn=server_certificate_arn,
                client_connect_options=client_connect_options,
                client_login_banner_options=client_login_banner_options,
                description=description,
                dns_servers=dns_servers,
                security_group_ids=security_group_ids,
                self_service_portal=self_service_portal,
                session_timeout_hours=session_timeout_hours,
                split_tunnel=split_tunnel,
                tags=tags,
                tags_all=tags_all,
                transport_protocol=transport_protocol,
                vpc_id=vpc_id,
                vpn_port=vpn_port,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authentication_options: Union[
            List[AuthenticationOptions], core.ArrayOut[AuthenticationOptions]
        ] = core.arg()

        client_cidr_block: Union[str, core.StringOut] = core.arg()

        client_connect_options: Optional[ClientConnectOptions] = core.arg(default=None)

        client_login_banner_options: Optional[ClientLoginBannerOptions] = core.arg(default=None)

        connection_log_options: ConnectionLogOptions = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dns_servers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        self_service_portal: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        server_certificate_arn: Union[str, core.StringOut] = core.arg()

        session_timeout_hours: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        split_tunnel: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        transport_protocol: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpn_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)
