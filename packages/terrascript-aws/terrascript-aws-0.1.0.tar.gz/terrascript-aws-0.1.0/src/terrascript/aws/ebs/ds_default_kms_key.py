from typing import Union

import terrascript.core as core


@core.data(type="aws_ebs_default_kms_key", namespace="aws_ebs")
class DsDefaultKmsKey(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsDefaultKmsKey.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
