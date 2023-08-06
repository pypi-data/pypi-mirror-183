from typing import Union

import terrascript.core as core


@core.data(type="aws_partition", namespace="aws_meta_data_sources")
class DsPartition(core.Data):

    dns_suffix: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    partition: Union[str, core.StringOut] = core.attr(str, computed=True)

    reverse_dns_prefix: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsPartition.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
