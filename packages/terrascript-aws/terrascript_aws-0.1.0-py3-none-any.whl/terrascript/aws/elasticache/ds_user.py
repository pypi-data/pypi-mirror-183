from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_elasticache_user", namespace="aws_elasticache")
class DsUser(core.Data):

    access_string: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    engine: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    no_password_required: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    passwords: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    user_id: Union[str, core.StringOut] = core.attr(str)

    user_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        user_id: Union[str, core.StringOut],
        access_string: Optional[Union[str, core.StringOut]] = None,
        engine: Optional[Union[str, core.StringOut]] = None,
        no_password_required: Optional[Union[bool, core.BoolOut]] = None,
        passwords: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        user_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsUser.Args(
                user_id=user_id,
                access_string=access_string,
                engine=engine,
                no_password_required=no_password_required,
                passwords=passwords,
                user_name=user_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_string: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        no_password_required: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        passwords: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_id: Union[str, core.StringOut] = core.arg()

        user_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
