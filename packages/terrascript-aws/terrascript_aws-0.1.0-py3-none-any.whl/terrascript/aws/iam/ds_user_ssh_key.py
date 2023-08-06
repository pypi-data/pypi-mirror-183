from typing import Union

import terrascript.core as core


@core.data(type="aws_iam_user_ssh_key", namespace="aws_iam")
class DsUserSshKey(core.Data):

    encoding: Union[str, core.StringOut] = core.attr(str)

    fingerprint: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    ssh_public_key_id: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        encoding: Union[str, core.StringOut],
        ssh_public_key_id: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsUserSshKey.Args(
                encoding=encoding,
                ssh_public_key_id=ssh_public_key_id,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encoding: Union[str, core.StringOut] = core.arg()

        ssh_public_key_id: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()
