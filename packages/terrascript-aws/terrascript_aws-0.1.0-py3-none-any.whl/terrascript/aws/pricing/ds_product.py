from typing import List, Union

import terrascript.core as core


@core.schema
class Filters(core.Schema):

    field: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        field: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Filters.Args(
                field=field,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_pricing_product", namespace="aws_pricing")
class DsProduct(core.Data):

    filters: Union[List[Filters], core.ArrayOut[Filters]] = core.attr(Filters, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    result: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_code: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        filters: Union[List[Filters], core.ArrayOut[Filters]],
        service_code: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsProduct.Args(
                filters=filters,
                service_code=service_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filters: Union[List[Filters], core.ArrayOut[Filters]] = core.arg()

        service_code: Union[str, core.StringOut] = core.arg()
