from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iam_user_login_profile", namespace="aws_iam")
class UserLoginProfile(core.Resource):

    encrypted_password: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_fingerprint: Union[str, core.StringOut] = core.attr(str, computed=True)

    password: Union[str, core.StringOut] = core.attr(str, computed=True)

    password_length: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    password_reset_required: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    pgp_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user: Union[str, core.StringOut],
        password_length: Optional[Union[int, core.IntOut]] = None,
        password_reset_required: Optional[Union[bool, core.BoolOut]] = None,
        pgp_key: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserLoginProfile.Args(
                user=user,
                password_length=password_length,
                password_reset_required=password_reset_required,
                pgp_key=pgp_key,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        password_length: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        password_reset_required: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        pgp_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user: Union[str, core.StringOut] = core.arg()
