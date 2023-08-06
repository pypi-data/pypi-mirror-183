from typing import Union

import terrascript.core as core


@core.data(type="aws_caller_identity", namespace="aws_sts")
class DsCallerIdentity(core.Data):

    account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsCallerIdentity.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
