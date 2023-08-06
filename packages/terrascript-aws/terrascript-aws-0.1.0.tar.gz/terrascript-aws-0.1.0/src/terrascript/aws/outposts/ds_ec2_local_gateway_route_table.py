from typing import Dict, List, Optional, Union

import terrascript.core as core


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


@core.data(type="aws_ec2_local_gateway_route_table", namespace="aws_outposts")
class DsEc2LocalGatewayRouteTable(core.Data):

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    local_gateway_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    local_gateway_route_table_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    outpost_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        local_gateway_id: Optional[Union[str, core.StringOut]] = None,
        local_gateway_route_table_id: Optional[Union[str, core.StringOut]] = None,
        outpost_arn: Optional[Union[str, core.StringOut]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2LocalGatewayRouteTable.Args(
                filter=filter,
                local_gateway_id=local_gateway_id,
                local_gateway_route_table_id=local_gateway_route_table_id,
                outpost_arn=outpost_arn,
                state=state,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        local_gateway_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        local_gateway_route_table_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        outpost_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
