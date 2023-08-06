from typing import List, Union

import terrascript.core as core


@core.data(type="aws_outposts_outpost_instance_types", namespace="aws_outposts")
class DsOutpostInstanceTypes(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsOutpostInstanceTypes.Args(
                arn=arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()
