from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iam_account_password_policy", namespace="aws_iam")
class AccountPasswordPolicy(core.Resource):

    allow_users_to_change_password: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    expire_passwords: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    hard_expiry: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    max_password_age: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    minimum_password_length: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    password_reuse_prevention: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    require_lowercase_characters: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    require_numbers: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    require_symbols: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    require_uppercase_characters: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        allow_users_to_change_password: Optional[Union[bool, core.BoolOut]] = None,
        hard_expiry: Optional[Union[bool, core.BoolOut]] = None,
        max_password_age: Optional[Union[int, core.IntOut]] = None,
        minimum_password_length: Optional[Union[int, core.IntOut]] = None,
        password_reuse_prevention: Optional[Union[int, core.IntOut]] = None,
        require_lowercase_characters: Optional[Union[bool, core.BoolOut]] = None,
        require_numbers: Optional[Union[bool, core.BoolOut]] = None,
        require_symbols: Optional[Union[bool, core.BoolOut]] = None,
        require_uppercase_characters: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccountPasswordPolicy.Args(
                allow_users_to_change_password=allow_users_to_change_password,
                hard_expiry=hard_expiry,
                max_password_age=max_password_age,
                minimum_password_length=minimum_password_length,
                password_reuse_prevention=password_reuse_prevention,
                require_lowercase_characters=require_lowercase_characters,
                require_numbers=require_numbers,
                require_symbols=require_symbols,
                require_uppercase_characters=require_uppercase_characters,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allow_users_to_change_password: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        hard_expiry: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        max_password_age: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        minimum_password_length: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        password_reuse_prevention: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        require_lowercase_characters: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        require_numbers: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        require_symbols: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        require_uppercase_characters: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
