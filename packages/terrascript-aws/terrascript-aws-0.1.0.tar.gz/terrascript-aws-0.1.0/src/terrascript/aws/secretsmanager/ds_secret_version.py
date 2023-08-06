from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_secretsmanager_secret_version", namespace="aws_secretsmanager")
class DsSecretVersion(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    secret_binary: Union[str, core.StringOut] = core.attr(str, computed=True)

    secret_id: Union[str, core.StringOut] = core.attr(str)

    secret_string: Union[str, core.StringOut] = core.attr(str, computed=True)

    version_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    version_stage: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    version_stages: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        secret_id: Union[str, core.StringOut],
        version_id: Optional[Union[str, core.StringOut]] = None,
        version_stage: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSecretVersion.Args(
                secret_id=secret_id,
                version_id=version_id,
                version_stage=version_stage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        secret_id: Union[str, core.StringOut] = core.arg()

        version_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version_stage: Optional[Union[str, core.StringOut]] = core.arg(default=None)
