from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iam_user_ssh_key", namespace="aws_iam")
class UserSshKey(core.Resource):

    encoding: Union[str, core.StringOut] = core.attr(str)

    fingerprint: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_key: Union[str, core.StringOut] = core.attr(str)

    ssh_public_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        encoding: Union[str, core.StringOut],
        public_key: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
        status: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserSshKey.Args(
                encoding=encoding,
                public_key=public_key,
                username=username,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        encoding: Union[str, core.StringOut] = core.arg()

        public_key: Union[str, core.StringOut] = core.arg()

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        username: Union[str, core.StringOut] = core.arg()
