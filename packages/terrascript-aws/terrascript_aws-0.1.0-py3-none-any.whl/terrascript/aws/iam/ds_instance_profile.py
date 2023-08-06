from typing import Union

import terrascript.core as core


@core.data(type="aws_iam_instance_profile", namespace="aws_iam")
class DsInstanceProfile(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    create_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    path: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsInstanceProfile.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()
