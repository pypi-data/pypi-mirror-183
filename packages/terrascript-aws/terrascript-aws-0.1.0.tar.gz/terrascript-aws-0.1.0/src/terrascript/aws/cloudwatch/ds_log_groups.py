from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_cloudwatch_log_groups", namespace="aws_cloudwatch")
class DsLogGroups(core.Data):

    arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_group_name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    log_group_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        log_group_name_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLogGroups.Args(
                log_group_name_prefix=log_group_name_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        log_group_name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)
