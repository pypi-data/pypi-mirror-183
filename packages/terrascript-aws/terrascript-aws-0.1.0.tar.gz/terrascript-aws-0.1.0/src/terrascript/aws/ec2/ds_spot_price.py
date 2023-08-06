from typing import List, Optional, Union

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


@core.data(type="aws_ec2_spot_price", namespace="aws_ec2")
class DsSpotPrice(core.Data):

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    spot_price: Union[str, core.StringOut] = core.attr(str, computed=True)

    spot_price_timestamp: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        instance_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSpotPrice.Args(
                availability_zone=availability_zone,
                filter=filter,
                instance_type=instance_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
