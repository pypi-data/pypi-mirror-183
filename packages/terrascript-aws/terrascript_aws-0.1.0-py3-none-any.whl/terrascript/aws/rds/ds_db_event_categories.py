from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_db_event_categories", namespace="aws_rds")
class DsDbEventCategories(core.Data):

    event_categories: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        source_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDbEventCategories.Args(
                source_type=source_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        source_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
