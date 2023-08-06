from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ConnectionLogOptions(core.Schema):

    cloudwatch_log_group: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudwatch_log_stream: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        cloudwatch_log_group: Union[str, core.StringOut],
        cloudwatch_log_stream: Union[str, core.StringOut],
        enabled: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=ConnectionLogOptions.Args(
                cloudwatch_log_group=cloudwatch_log_group,
                cloudwatch_log_stream=cloudwatch_log_stream,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_log_group: Union[str, core.StringOut] = core.arg()

        cloudwatch_log_stream: Union[str, core.StringOut] = core.arg()

        enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class ClientLoginBannerOptions(core.Schema):

    banner_text: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        banner_text: Union[str, core.StringOut],
        enabled: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=ClientLoginBannerOptions.Args(
                banner_text=banner_text,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        banner_text: Union[str, core.StringOut] = core.arg()

        enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class AuthenticationOptions(core.Schema):

    active_directory_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_certificate_chain_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    saml_provider_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    self_service_saml_provider_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        active_directory_id: Union[str, core.StringOut],
        root_certificate_chain_arn: Union[str, core.StringOut],
        saml_provider_arn: Union[str, core.StringOut],
        self_service_saml_provider_arn: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AuthenticationOptions.Args(
                active_directory_id=active_directory_id,
                root_certificate_chain_arn=root_certificate_chain_arn,
                saml_provider_arn=saml_provider_arn,
                self_service_saml_provider_arn=self_service_saml_provider_arn,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        active_directory_id: Union[str, core.StringOut] = core.arg()

        root_certificate_chain_arn: Union[str, core.StringOut] = core.arg()

        saml_provider_arn: Union[str, core.StringOut] = core.arg()

        self_service_saml_provider_arn: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class ClientConnectOptions(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    lambda_function_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        lambda_function_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ClientConnectOptions.Args(
                enabled=enabled,
                lambda_function_arn=lambda_function_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        lambda_function_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class Filter(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.data(type="aws_ec2_client_vpn_endpoint", namespace="aws_vpn")
class DsEc2ClientVpnEndpoint(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authentication_options: Union[
        List[AuthenticationOptions], core.ArrayOut[AuthenticationOptions]
    ] = core.attr(AuthenticationOptions, computed=True, kind=core.Kind.array)

    client_cidr_block: Union[str, core.StringOut] = core.attr(str, computed=True)

    client_connect_options: Union[
        List[ClientConnectOptions], core.ArrayOut[ClientConnectOptions]
    ] = core.attr(ClientConnectOptions, computed=True, kind=core.Kind.array)

    client_login_banner_options: Union[
        List[ClientLoginBannerOptions], core.ArrayOut[ClientLoginBannerOptions]
    ] = core.attr(ClientLoginBannerOptions, computed=True, kind=core.Kind.array)

    client_vpn_endpoint_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    connection_log_options: Union[
        List[ConnectionLogOptions], core.ArrayOut[ConnectionLogOptions]
    ] = core.attr(ConnectionLogOptions, computed=True, kind=core.Kind.array)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    dns_servers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    self_service_portal: Union[str, core.StringOut] = core.attr(str, computed=True)

    server_certificate_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    session_timeout_hours: Union[int, core.IntOut] = core.attr(int, computed=True)

    split_tunnel: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transport_protocol: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpn_port: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        client_vpn_endpoint_id: Optional[Union[str, core.StringOut]] = None,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2ClientVpnEndpoint.Args(
                client_vpn_endpoint_id=client_vpn_endpoint_id,
                filter=filter,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_vpn_endpoint_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
