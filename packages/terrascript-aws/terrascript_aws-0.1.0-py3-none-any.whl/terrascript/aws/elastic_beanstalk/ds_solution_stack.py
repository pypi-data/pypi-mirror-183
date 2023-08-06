from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_elastic_beanstalk_solution_stack", namespace="aws_elastic_beanstalk")
class DsSolutionStack(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    most_recent: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    name_regex: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name_regex: Union[str, core.StringOut],
        most_recent: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSolutionStack.Args(
                name_regex=name_regex,
                most_recent=most_recent,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        most_recent: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name_regex: Union[str, core.StringOut] = core.arg()
