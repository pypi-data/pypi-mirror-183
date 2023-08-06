from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Attachments(core.Schema):

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        state: Union[str, core.StringOut],
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Attachments.Args(
                state=state,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        state: Union[str, core.StringOut] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


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


@core.data(type="aws_internet_gateway", namespace="aws_vpc")
class DsInternetGateway(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    attachments: Union[List[Attachments], core.ArrayOut[Attachments]] = core.attr(
        Attachments, computed=True, kind=core.Kind.array
    )

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    internet_gateway_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        internet_gateway_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsInternetGateway.Args(
                filter=filter,
                internet_gateway_id=internet_gateway_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        internet_gateway_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
