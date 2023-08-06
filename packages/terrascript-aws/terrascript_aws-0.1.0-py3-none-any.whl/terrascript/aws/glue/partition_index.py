from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class PartitionIndexBlk(core.Schema):

    index_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    index_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        index_status: Union[str, core.StringOut],
        index_name: Optional[Union[str, core.StringOut]] = None,
        keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=PartitionIndexBlk.Args(
                index_status=index_status,
                index_name=index_name,
                keys=keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        index_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        index_status: Union[str, core.StringOut] = core.arg()

        keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.resource(type="aws_glue_partition_index", namespace="aws_glue")
class PartitionIndex(core.Resource):

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    database_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    partition_index: PartitionIndexBlk = core.attr(PartitionIndexBlk)

    table_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        database_name: Union[str, core.StringOut],
        partition_index: PartitionIndexBlk,
        table_name: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PartitionIndex.Args(
                database_name=database_name,
                partition_index=partition_index,
                table_name=table_name,
                catalog_id=catalog_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        database_name: Union[str, core.StringOut] = core.arg()

        partition_index: PartitionIndexBlk = core.arg()

        table_name: Union[str, core.StringOut] = core.arg()
