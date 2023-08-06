from typing import List, Union

import terrascript.core as core


@core.schema
class Users(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    path: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        path: Union[str, core.StringOut],
        user_id: Union[str, core.StringOut],
        user_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Users.Args(
                arn=arn,
                path=path,
                user_id=user_id,
                user_name=user_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        path: Union[str, core.StringOut] = core.arg()

        user_id: Union[str, core.StringOut] = core.arg()

        user_name: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_iam_group", namespace="aws_iam")
class DsGroup(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    group_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    path: Union[str, core.StringOut] = core.attr(str, computed=True)

    users: Union[List[Users], core.ArrayOut[Users]] = core.attr(
        Users, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        group_name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsGroup.Args(
                group_name=group_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        group_name: Union[str, core.StringOut] = core.arg()
