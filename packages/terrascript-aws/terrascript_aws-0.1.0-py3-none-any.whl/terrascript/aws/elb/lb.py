from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AccessLogs(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AccessLogs.Args(
                bucket=bucket,
                enabled=enabled,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SubnetMapping(core.Schema):

    allocation_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ipv6_address: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    outpost_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_ipv4_address: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    subnet_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        outpost_id: Union[str, core.StringOut],
        subnet_id: Union[str, core.StringOut],
        allocation_id: Optional[Union[str, core.StringOut]] = None,
        ipv6_address: Optional[Union[str, core.StringOut]] = None,
        private_ipv4_address: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SubnetMapping.Args(
                outpost_id=outpost_id,
                subnet_id=subnet_id,
                allocation_id=allocation_id,
                ipv6_address=ipv6_address,
                private_ipv4_address=private_ipv4_address,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv6_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        outpost_id: Union[str, core.StringOut] = core.arg()

        private_ipv4_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_id: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_lb", namespace="aws_elb")
class Lb(core.Resource):

    access_logs: Optional[AccessLogs] = core.attr(AccessLogs, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn_suffix: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_owned_ipv4_pool: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    desync_mitigation_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    drop_invalid_header_fields: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_cross_zone_load_balancing: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    enable_deletion_protection: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_http2: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_waf_fail_open: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    idle_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    internal: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    ip_address_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    load_balancer_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    preserve_host_header: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    subnet_mapping: Optional[Union[List[SubnetMapping], core.ArrayOut[SubnetMapping]]] = core.attr(
        SubnetMapping, default=None, computed=True, kind=core.Kind.array
    )

    subnets: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        access_logs: Optional[AccessLogs] = None,
        customer_owned_ipv4_pool: Optional[Union[str, core.StringOut]] = None,
        desync_mitigation_mode: Optional[Union[str, core.StringOut]] = None,
        drop_invalid_header_fields: Optional[Union[bool, core.BoolOut]] = None,
        enable_cross_zone_load_balancing: Optional[Union[bool, core.BoolOut]] = None,
        enable_deletion_protection: Optional[Union[bool, core.BoolOut]] = None,
        enable_http2: Optional[Union[bool, core.BoolOut]] = None,
        enable_waf_fail_open: Optional[Union[bool, core.BoolOut]] = None,
        idle_timeout: Optional[Union[int, core.IntOut]] = None,
        internal: Optional[Union[bool, core.BoolOut]] = None,
        ip_address_type: Optional[Union[str, core.StringOut]] = None,
        load_balancer_type: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        preserve_host_header: Optional[Union[bool, core.BoolOut]] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        subnet_mapping: Optional[Union[List[SubnetMapping], core.ArrayOut[SubnetMapping]]] = None,
        subnets: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Lb.Args(
                access_logs=access_logs,
                customer_owned_ipv4_pool=customer_owned_ipv4_pool,
                desync_mitigation_mode=desync_mitigation_mode,
                drop_invalid_header_fields=drop_invalid_header_fields,
                enable_cross_zone_load_balancing=enable_cross_zone_load_balancing,
                enable_deletion_protection=enable_deletion_protection,
                enable_http2=enable_http2,
                enable_waf_fail_open=enable_waf_fail_open,
                idle_timeout=idle_timeout,
                internal=internal,
                ip_address_type=ip_address_type,
                load_balancer_type=load_balancer_type,
                name=name,
                name_prefix=name_prefix,
                preserve_host_header=preserve_host_header,
                security_groups=security_groups,
                subnet_mapping=subnet_mapping,
                subnets=subnets,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_logs: Optional[AccessLogs] = core.arg(default=None)

        customer_owned_ipv4_pool: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        desync_mitigation_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        drop_invalid_header_fields: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_cross_zone_load_balancing: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        enable_deletion_protection: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_http2: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_waf_fail_open: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        idle_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        internal: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ip_address_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        load_balancer_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        preserve_host_header: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_mapping: Optional[
            Union[List[SubnetMapping], core.ArrayOut[SubnetMapping]]
        ] = core.arg(default=None)

        subnets: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
