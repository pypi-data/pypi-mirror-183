from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class SubnetMapping(core.Schema):

    allocation_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    outpost_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_ipv4_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        allocation_id: Union[str, core.StringOut],
        ipv6_address: Union[str, core.StringOut],
        outpost_id: Union[str, core.StringOut],
        private_ipv4_address: Union[str, core.StringOut],
        subnet_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SubnetMapping.Args(
                allocation_id=allocation_id,
                ipv6_address=ipv6_address,
                outpost_id=outpost_id,
                private_ipv4_address=private_ipv4_address,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_id: Union[str, core.StringOut] = core.arg()

        ipv6_address: Union[str, core.StringOut] = core.arg()

        outpost_id: Union[str, core.StringOut] = core.arg()

        private_ipv4_address: Union[str, core.StringOut] = core.arg()

        subnet_id: Union[str, core.StringOut] = core.arg()


@core.schema
class AccessLogs(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    prefix: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        enabled: Union[bool, core.BoolOut],
        prefix: Union[str, core.StringOut],
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

        enabled: Union[bool, core.BoolOut] = core.arg()

        prefix: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_lb", namespace="aws_elb")
class DsLb(core.Data):

    access_logs: Union[List[AccessLogs], core.ArrayOut[AccessLogs]] = core.attr(
        AccessLogs, computed=True, kind=core.Kind.array
    )

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    arn_suffix: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_owned_ipv4_pool: Union[str, core.StringOut] = core.attr(str, computed=True)

    desync_mitigation_mode: Union[str, core.StringOut] = core.attr(str, computed=True)

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    drop_invalid_header_fields: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    enable_deletion_protection: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    enable_http2: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    enable_waf_fail_open: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    idle_timeout: Union[int, core.IntOut] = core.attr(int, computed=True)

    internal: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    ip_address_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    load_balancer_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    preserve_host_header: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_mapping: Union[List[SubnetMapping], core.ArrayOut[SubnetMapping]] = core.attr(
        SubnetMapping, computed=True, kind=core.Kind.array
    )

    subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLb.Args(
                arn=arn,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
