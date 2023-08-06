from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_iam_users", namespace="aws_iam")
class DsUsers(core.Data):

    arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name_regex: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    path_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        name_regex: Optional[Union[str, core.StringOut]] = None,
        path_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsUsers.Args(
                name_regex=name_regex,
                path_prefix=path_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name_regex: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        path_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)
