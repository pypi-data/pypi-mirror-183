from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iam_access_key", namespace="aws_iam")
class AccessKey(core.Resource):

    create_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    encrypted_secret: Union[str, core.StringOut] = core.attr(str, computed=True)

    encrypted_ses_smtp_password_v4: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_fingerprint: Union[str, core.StringOut] = core.attr(str, computed=True)

    pgp_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    secret: Union[str, core.StringOut] = core.attr(str, computed=True)

    ses_smtp_password_v4: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user: Union[str, core.StringOut],
        pgp_key: Optional[Union[str, core.StringOut]] = None,
        status: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccessKey.Args(
                user=user,
                pgp_key=pgp_key,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        pgp_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user: Union[str, core.StringOut] = core.arg()
