from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Routes(core.Schema):

    destination_cidr_block: Union[str, core.StringOut] = core.attr(str, computed=True)

    source: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        destination_cidr_block: Union[str, core.StringOut],
        source: Union[str, core.StringOut],
        state: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Routes.Args(
                destination_cidr_block=destination_cidr_block,
                source=source,
                state=state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_cidr_block: Union[str, core.StringOut] = core.arg()

        source: Union[str, core.StringOut] = core.arg()

        state: Union[str, core.StringOut] = core.arg()


@core.schema
class VgwTelemetry(core.Schema):

    accepted_route_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    certificate_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_status_change: Union[str, core.StringOut] = core.attr(str, computed=True)

    outside_ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    status_message: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        accepted_route_count: Union[int, core.IntOut],
        certificate_arn: Union[str, core.StringOut],
        last_status_change: Union[str, core.StringOut],
        outside_ip_address: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
        status_message: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VgwTelemetry.Args(
                accepted_route_count=accepted_route_count,
                certificate_arn=certificate_arn,
                last_status_change=last_status_change,
                outside_ip_address=outside_ip_address,
                status=status,
                status_message=status_message,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accepted_route_count: Union[int, core.IntOut] = core.arg()

        certificate_arn: Union[str, core.StringOut] = core.arg()

        last_status_change: Union[str, core.StringOut] = core.arg()

        outside_ip_address: Union[str, core.StringOut] = core.arg()

        status: Union[str, core.StringOut] = core.arg()

        status_message: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_vpn_connection", namespace="aws_vpn")
class Connection(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    core_network_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    core_network_attachment_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_gateway_configuration: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_gateway_id: Union[str, core.StringOut] = core.attr(str)

    enable_acceleration: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    local_ipv4_network_cidr: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    local_ipv6_network_cidr: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    outside_ip_address_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    remote_ipv4_network_cidr: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    remote_ipv6_network_cidr: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    routes: Union[List[Routes], core.ArrayOut[Routes]] = core.attr(
        Routes, computed=True, kind=core.Kind.array
    )

    static_routes_only: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_gateway_attachment_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    transit_gateway_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    transport_transit_gateway_attachment_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    tunnel1_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    tunnel1_bgp_asn: Union[str, core.StringOut] = core.attr(str, computed=True)

    tunnel1_bgp_holdtime: Union[int, core.IntOut] = core.attr(int, computed=True)

    tunnel1_cgw_inside_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    tunnel1_dpd_timeout_action: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tunnel1_dpd_timeout_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tunnel1_ike_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tunnel1_inside_cidr: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tunnel1_inside_ipv6_cidr: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tunnel1_phase1_dh_group_numbers: Optional[
        Union[List[int], core.ArrayOut[core.IntOut]]
    ] = core.attr(int, default=None, kind=core.Kind.array)

    tunnel1_phase1_encryption_algorithms: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    tunnel1_phase1_integrity_algorithms: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    tunnel1_phase1_lifetime_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    tunnel1_phase2_dh_group_numbers: Optional[
        Union[List[int], core.ArrayOut[core.IntOut]]
    ] = core.attr(int, default=None, kind=core.Kind.array)

    tunnel1_phase2_encryption_algorithms: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    tunnel1_phase2_integrity_algorithms: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    tunnel1_phase2_lifetime_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    tunnel1_preshared_key: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tunnel1_rekey_fuzz_percentage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tunnel1_rekey_margin_time_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    tunnel1_replay_window_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tunnel1_startup_action: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tunnel1_vgw_inside_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    tunnel2_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    tunnel2_bgp_asn: Union[str, core.StringOut] = core.attr(str, computed=True)

    tunnel2_bgp_holdtime: Union[int, core.IntOut] = core.attr(int, computed=True)

    tunnel2_cgw_inside_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    tunnel2_dpd_timeout_action: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tunnel2_dpd_timeout_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tunnel2_ike_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tunnel2_inside_cidr: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tunnel2_inside_ipv6_cidr: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tunnel2_phase1_dh_group_numbers: Optional[
        Union[List[int], core.ArrayOut[core.IntOut]]
    ] = core.attr(int, default=None, kind=core.Kind.array)

    tunnel2_phase1_encryption_algorithms: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    tunnel2_phase1_integrity_algorithms: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    tunnel2_phase1_lifetime_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    tunnel2_phase2_dh_group_numbers: Optional[
        Union[List[int], core.ArrayOut[core.IntOut]]
    ] = core.attr(int, default=None, kind=core.Kind.array)

    tunnel2_phase2_encryption_algorithms: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    tunnel2_phase2_integrity_algorithms: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    tunnel2_phase2_lifetime_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    tunnel2_preshared_key: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tunnel2_rekey_fuzz_percentage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tunnel2_rekey_margin_time_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    tunnel2_replay_window_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tunnel2_startup_action: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tunnel2_vgw_inside_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    tunnel_inside_ip_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    type: Union[str, core.StringOut] = core.attr(str)

    vgw_telemetry: Union[List[VgwTelemetry], core.ArrayOut[VgwTelemetry]] = core.attr(
        VgwTelemetry, computed=True, kind=core.Kind.array
    )

    vpn_gateway_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        customer_gateway_id: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        enable_acceleration: Optional[Union[bool, core.BoolOut]] = None,
        local_ipv4_network_cidr: Optional[Union[str, core.StringOut]] = None,
        local_ipv6_network_cidr: Optional[Union[str, core.StringOut]] = None,
        outside_ip_address_type: Optional[Union[str, core.StringOut]] = None,
        remote_ipv4_network_cidr: Optional[Union[str, core.StringOut]] = None,
        remote_ipv6_network_cidr: Optional[Union[str, core.StringOut]] = None,
        static_routes_only: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        transit_gateway_id: Optional[Union[str, core.StringOut]] = None,
        transport_transit_gateway_attachment_id: Optional[Union[str, core.StringOut]] = None,
        tunnel1_dpd_timeout_action: Optional[Union[str, core.StringOut]] = None,
        tunnel1_dpd_timeout_seconds: Optional[Union[int, core.IntOut]] = None,
        tunnel1_ike_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tunnel1_inside_cidr: Optional[Union[str, core.StringOut]] = None,
        tunnel1_inside_ipv6_cidr: Optional[Union[str, core.StringOut]] = None,
        tunnel1_phase1_dh_group_numbers: Optional[
            Union[List[int], core.ArrayOut[core.IntOut]]
        ] = None,
        tunnel1_phase1_encryption_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        tunnel1_phase1_integrity_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        tunnel1_phase1_lifetime_seconds: Optional[Union[int, core.IntOut]] = None,
        tunnel1_phase2_dh_group_numbers: Optional[
            Union[List[int], core.ArrayOut[core.IntOut]]
        ] = None,
        tunnel1_phase2_encryption_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        tunnel1_phase2_integrity_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        tunnel1_phase2_lifetime_seconds: Optional[Union[int, core.IntOut]] = None,
        tunnel1_preshared_key: Optional[Union[str, core.StringOut]] = None,
        tunnel1_rekey_fuzz_percentage: Optional[Union[int, core.IntOut]] = None,
        tunnel1_rekey_margin_time_seconds: Optional[Union[int, core.IntOut]] = None,
        tunnel1_replay_window_size: Optional[Union[int, core.IntOut]] = None,
        tunnel1_startup_action: Optional[Union[str, core.StringOut]] = None,
        tunnel2_dpd_timeout_action: Optional[Union[str, core.StringOut]] = None,
        tunnel2_dpd_timeout_seconds: Optional[Union[int, core.IntOut]] = None,
        tunnel2_ike_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tunnel2_inside_cidr: Optional[Union[str, core.StringOut]] = None,
        tunnel2_inside_ipv6_cidr: Optional[Union[str, core.StringOut]] = None,
        tunnel2_phase1_dh_group_numbers: Optional[
            Union[List[int], core.ArrayOut[core.IntOut]]
        ] = None,
        tunnel2_phase1_encryption_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        tunnel2_phase1_integrity_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        tunnel2_phase1_lifetime_seconds: Optional[Union[int, core.IntOut]] = None,
        tunnel2_phase2_dh_group_numbers: Optional[
            Union[List[int], core.ArrayOut[core.IntOut]]
        ] = None,
        tunnel2_phase2_encryption_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        tunnel2_phase2_integrity_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        tunnel2_phase2_lifetime_seconds: Optional[Union[int, core.IntOut]] = None,
        tunnel2_preshared_key: Optional[Union[str, core.StringOut]] = None,
        tunnel2_rekey_fuzz_percentage: Optional[Union[int, core.IntOut]] = None,
        tunnel2_rekey_margin_time_seconds: Optional[Union[int, core.IntOut]] = None,
        tunnel2_replay_window_size: Optional[Union[int, core.IntOut]] = None,
        tunnel2_startup_action: Optional[Union[str, core.StringOut]] = None,
        tunnel_inside_ip_version: Optional[Union[str, core.StringOut]] = None,
        vpn_gateway_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Connection.Args(
                customer_gateway_id=customer_gateway_id,
                type=type,
                enable_acceleration=enable_acceleration,
                local_ipv4_network_cidr=local_ipv4_network_cidr,
                local_ipv6_network_cidr=local_ipv6_network_cidr,
                outside_ip_address_type=outside_ip_address_type,
                remote_ipv4_network_cidr=remote_ipv4_network_cidr,
                remote_ipv6_network_cidr=remote_ipv6_network_cidr,
                static_routes_only=static_routes_only,
                tags=tags,
                tags_all=tags_all,
                transit_gateway_id=transit_gateway_id,
                transport_transit_gateway_attachment_id=transport_transit_gateway_attachment_id,
                tunnel1_dpd_timeout_action=tunnel1_dpd_timeout_action,
                tunnel1_dpd_timeout_seconds=tunnel1_dpd_timeout_seconds,
                tunnel1_ike_versions=tunnel1_ike_versions,
                tunnel1_inside_cidr=tunnel1_inside_cidr,
                tunnel1_inside_ipv6_cidr=tunnel1_inside_ipv6_cidr,
                tunnel1_phase1_dh_group_numbers=tunnel1_phase1_dh_group_numbers,
                tunnel1_phase1_encryption_algorithms=tunnel1_phase1_encryption_algorithms,
                tunnel1_phase1_integrity_algorithms=tunnel1_phase1_integrity_algorithms,
                tunnel1_phase1_lifetime_seconds=tunnel1_phase1_lifetime_seconds,
                tunnel1_phase2_dh_group_numbers=tunnel1_phase2_dh_group_numbers,
                tunnel1_phase2_encryption_algorithms=tunnel1_phase2_encryption_algorithms,
                tunnel1_phase2_integrity_algorithms=tunnel1_phase2_integrity_algorithms,
                tunnel1_phase2_lifetime_seconds=tunnel1_phase2_lifetime_seconds,
                tunnel1_preshared_key=tunnel1_preshared_key,
                tunnel1_rekey_fuzz_percentage=tunnel1_rekey_fuzz_percentage,
                tunnel1_rekey_margin_time_seconds=tunnel1_rekey_margin_time_seconds,
                tunnel1_replay_window_size=tunnel1_replay_window_size,
                tunnel1_startup_action=tunnel1_startup_action,
                tunnel2_dpd_timeout_action=tunnel2_dpd_timeout_action,
                tunnel2_dpd_timeout_seconds=tunnel2_dpd_timeout_seconds,
                tunnel2_ike_versions=tunnel2_ike_versions,
                tunnel2_inside_cidr=tunnel2_inside_cidr,
                tunnel2_inside_ipv6_cidr=tunnel2_inside_ipv6_cidr,
                tunnel2_phase1_dh_group_numbers=tunnel2_phase1_dh_group_numbers,
                tunnel2_phase1_encryption_algorithms=tunnel2_phase1_encryption_algorithms,
                tunnel2_phase1_integrity_algorithms=tunnel2_phase1_integrity_algorithms,
                tunnel2_phase1_lifetime_seconds=tunnel2_phase1_lifetime_seconds,
                tunnel2_phase2_dh_group_numbers=tunnel2_phase2_dh_group_numbers,
                tunnel2_phase2_encryption_algorithms=tunnel2_phase2_encryption_algorithms,
                tunnel2_phase2_integrity_algorithms=tunnel2_phase2_integrity_algorithms,
                tunnel2_phase2_lifetime_seconds=tunnel2_phase2_lifetime_seconds,
                tunnel2_preshared_key=tunnel2_preshared_key,
                tunnel2_rekey_fuzz_percentage=tunnel2_rekey_fuzz_percentage,
                tunnel2_rekey_margin_time_seconds=tunnel2_rekey_margin_time_seconds,
                tunnel2_replay_window_size=tunnel2_replay_window_size,
                tunnel2_startup_action=tunnel2_startup_action,
                tunnel_inside_ip_version=tunnel_inside_ip_version,
                vpn_gateway_id=vpn_gateway_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        customer_gateway_id: Union[str, core.StringOut] = core.arg()

        enable_acceleration: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        local_ipv4_network_cidr: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        local_ipv6_network_cidr: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        outside_ip_address_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        remote_ipv4_network_cidr: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        remote_ipv6_network_cidr: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        static_routes_only: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        transit_gateway_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transport_transit_gateway_attachment_id: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        tunnel1_dpd_timeout_action: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tunnel1_dpd_timeout_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tunnel1_ike_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tunnel1_inside_cidr: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tunnel1_inside_ipv6_cidr: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tunnel1_phase1_dh_group_numbers: Optional[
            Union[List[int], core.ArrayOut[core.IntOut]]
        ] = core.arg(default=None)

        tunnel1_phase1_encryption_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        tunnel1_phase1_integrity_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        tunnel1_phase1_lifetime_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tunnel1_phase2_dh_group_numbers: Optional[
            Union[List[int], core.ArrayOut[core.IntOut]]
        ] = core.arg(default=None)

        tunnel1_phase2_encryption_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        tunnel1_phase2_integrity_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        tunnel1_phase2_lifetime_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tunnel1_preshared_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tunnel1_rekey_fuzz_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tunnel1_rekey_margin_time_seconds: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        tunnel1_replay_window_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tunnel1_startup_action: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tunnel2_dpd_timeout_action: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tunnel2_dpd_timeout_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tunnel2_ike_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tunnel2_inside_cidr: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tunnel2_inside_ipv6_cidr: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tunnel2_phase1_dh_group_numbers: Optional[
            Union[List[int], core.ArrayOut[core.IntOut]]
        ] = core.arg(default=None)

        tunnel2_phase1_encryption_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        tunnel2_phase1_integrity_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        tunnel2_phase1_lifetime_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tunnel2_phase2_dh_group_numbers: Optional[
            Union[List[int], core.ArrayOut[core.IntOut]]
        ] = core.arg(default=None)

        tunnel2_phase2_encryption_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        tunnel2_phase2_integrity_algorithms: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        tunnel2_phase2_lifetime_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tunnel2_preshared_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tunnel2_rekey_fuzz_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tunnel2_rekey_margin_time_seconds: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        tunnel2_replay_window_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tunnel2_startup_action: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tunnel_inside_ip_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()

        vpn_gateway_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
