from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dynamodb_table_item", namespace="aws_dynamodb")
class TableItem(core.Resource):

    hash_key: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    item: Union[str, core.StringOut] = core.attr(str)

    range_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    table_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        hash_key: Union[str, core.StringOut],
        item: Union[str, core.StringOut],
        table_name: Union[str, core.StringOut],
        range_key: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TableItem.Args(
                hash_key=hash_key,
                item=item,
                table_name=table_name,
                range_key=range_key,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        hash_key: Union[str, core.StringOut] = core.arg()

        item: Union[str, core.StringOut] = core.arg()

        range_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        table_name: Union[str, core.StringOut] = core.arg()
