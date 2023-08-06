from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class IpSets(core.Schema):

    ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    ip_family: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]],
        ip_family: Union[str, core.StringOut],
    ):
        super().__init__(
            args=IpSets.Args(
                ip_addresses=ip_addresses,
                ip_family=ip_family,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        ip_family: Union[str, core.StringOut] = core.arg()


@core.schema
class Attributes(core.Schema):

    flow_logs_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    flow_logs_s3_bucket: Union[str, core.StringOut] = core.attr(str, computed=True)

    flow_logs_s3_prefix: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        flow_logs_enabled: Union[bool, core.BoolOut],
        flow_logs_s3_bucket: Union[str, core.StringOut],
        flow_logs_s3_prefix: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Attributes.Args(
                flow_logs_enabled=flow_logs_enabled,
                flow_logs_s3_bucket=flow_logs_s3_bucket,
                flow_logs_s3_prefix=flow_logs_s3_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        flow_logs_enabled: Union[bool, core.BoolOut] = core.arg()

        flow_logs_s3_bucket: Union[str, core.StringOut] = core.arg()

        flow_logs_s3_prefix: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_globalaccelerator_accelerator", namespace="aws_globalaccelerator")
class DsAccelerator(core.Data):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    attributes: Union[List[Attributes], core.ArrayOut[Attributes]] = core.attr(
        Attributes, computed=True, kind=core.Kind.array
    )

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_address_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_sets: Union[List[IpSets], core.ArrayOut[IpSets]] = core.attr(
        IpSets, computed=True, kind=core.Kind.array
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
            args=DsAccelerator.Args(
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
