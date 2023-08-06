from typing import List, Union

import terrascript.core as core


@core.data(type="aws_efs_access_points", namespace="aws_efs")
class DsAccessPoints(core.Data):

    arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    file_system_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        file_system_id: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsAccessPoints.Args(
                file_system_id=file_system_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file_system_id: Union[str, core.StringOut] = core.arg()
