from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Attributes(core.Schema):

    flow_logs_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    flow_logs_s3_bucket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    flow_logs_s3_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        flow_logs_enabled: Optional[Union[bool, core.BoolOut]] = None,
        flow_logs_s3_bucket: Optional[Union[str, core.StringOut]] = None,
        flow_logs_s3_prefix: Optional[Union[str, core.StringOut]] = None,
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
        flow_logs_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        flow_logs_s3_bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        flow_logs_s3_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


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


@core.resource(type="aws_globalaccelerator_accelerator", namespace="aws_globalaccelerator")
class Accelerator(core.Resource):

    attributes: Optional[Attributes] = core.attr(Attributes, default=None)

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_address_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ip_sets: Union[List[IpSets], core.ArrayOut[IpSets]] = core.attr(
        IpSets, computed=True, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

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
        name: Union[str, core.StringOut],
        attributes: Optional[Attributes] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        ip_address_type: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Accelerator.Args(
                name=name,
                attributes=attributes,
                enabled=enabled,
                ip_address_type=ip_address_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attributes: Optional[Attributes] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ip_address_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
