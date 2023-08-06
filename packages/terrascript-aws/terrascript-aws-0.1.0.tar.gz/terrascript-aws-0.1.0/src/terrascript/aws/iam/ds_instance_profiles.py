from typing import List, Union

import terrascript.core as core


@core.data(type="aws_iam_instance_profiles", namespace="aws_iam")
class DsInstanceProfiles(core.Data):

    arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    paths: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    role_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        role_name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsInstanceProfiles.Args(
                role_name=role_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        role_name: Union[str, core.StringOut] = core.arg()
