from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_secretsmanager_random_password", namespace="aws_secretsmanager")
class DsRandomPassword(core.Data):

    exclude_characters: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    exclude_lowercase: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    exclude_numbers: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    exclude_punctuation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    exclude_uppercase: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    include_space: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    password_length: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    random_password: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    require_each_included_type: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        exclude_characters: Optional[Union[str, core.StringOut]] = None,
        exclude_lowercase: Optional[Union[bool, core.BoolOut]] = None,
        exclude_numbers: Optional[Union[bool, core.BoolOut]] = None,
        exclude_punctuation: Optional[Union[bool, core.BoolOut]] = None,
        exclude_uppercase: Optional[Union[bool, core.BoolOut]] = None,
        include_space: Optional[Union[bool, core.BoolOut]] = None,
        password_length: Optional[Union[int, core.IntOut]] = None,
        random_password: Optional[Union[str, core.StringOut]] = None,
        require_each_included_type: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRandomPassword.Args(
                exclude_characters=exclude_characters,
                exclude_lowercase=exclude_lowercase,
                exclude_numbers=exclude_numbers,
                exclude_punctuation=exclude_punctuation,
                exclude_uppercase=exclude_uppercase,
                include_space=include_space,
                password_length=password_length,
                random_password=random_password,
                require_each_included_type=require_each_included_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exclude_characters: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        exclude_lowercase: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        exclude_numbers: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        exclude_punctuation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        exclude_uppercase: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_space: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        password_length: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        random_password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        require_each_included_type: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
