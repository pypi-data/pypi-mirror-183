from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.data(type="aws_route53_zone", namespace="aws_route53")
class DsZone(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    caller_reference: Union[str, core.StringOut] = core.attr(str, computed=True)

    comment: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    linked_service_description: Union[str, core.StringOut] = core.attr(str, computed=True)

    linked_service_principal: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_servers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    private_zone: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    resource_record_set_count: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    zone_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
        private_zone: Optional[Union[bool, core.BoolOut]] = None,
        resource_record_set_count: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_id: Optional[Union[str, core.StringOut]] = None,
        zone_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsZone.Args(
                name=name,
                private_zone=private_zone,
                resource_record_set_count=resource_record_set_count,
                tags=tags,
                vpc_id=vpc_id,
                zone_id=zone_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        private_zone: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        resource_record_set_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        vpc_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        zone_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
