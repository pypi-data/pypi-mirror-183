from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class TriggerBlk(core.Schema):

    branches: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    custom_data: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    destination_arn: Union[str, core.StringOut] = core.attr(str)

    events: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        destination_arn: Union[str, core.StringOut],
        events: Union[List[str], core.ArrayOut[core.StringOut]],
        name: Union[str, core.StringOut],
        branches: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        custom_data: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=TriggerBlk.Args(
                destination_arn=destination_arn,
                events=events,
                name=name,
                branches=branches,
                custom_data=custom_data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        branches: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        custom_data: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        destination_arn: Union[str, core.StringOut] = core.arg()

        events: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_codecommit_trigger", namespace="aws_codecommit")
class Trigger(core.Resource):

    configuration_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    repository_name: Union[str, core.StringOut] = core.attr(str)

    trigger: Union[List[TriggerBlk], core.ArrayOut[TriggerBlk]] = core.attr(
        TriggerBlk, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        repository_name: Union[str, core.StringOut],
        trigger: Union[List[TriggerBlk], core.ArrayOut[TriggerBlk]],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Trigger.Args(
                repository_name=repository_name,
                trigger=trigger,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        repository_name: Union[str, core.StringOut] = core.arg()

        trigger: Union[List[TriggerBlk], core.ArrayOut[TriggerBlk]] = core.arg()
