from typing import List, Union

import terrascript.core as core


@core.data(type="aws_backup_selection", namespace="aws_backup")
class DsSelection(core.Data):

    iam_role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    plan_id: Union[str, core.StringOut] = core.attr(str)

    resources: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    selection_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        plan_id: Union[str, core.StringOut],
        selection_id: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsSelection.Args(
                plan_id=plan_id,
                selection_id=selection_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        plan_id: Union[str, core.StringOut] = core.arg()

        selection_id: Union[str, core.StringOut] = core.arg()
