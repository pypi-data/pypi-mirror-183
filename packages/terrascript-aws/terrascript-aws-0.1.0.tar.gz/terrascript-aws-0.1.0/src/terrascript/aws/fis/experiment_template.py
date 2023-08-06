from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Parameter(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Parameter.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class ActionTarget(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ActionTarget.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Action(core.Schema):

    action_id: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    start_after: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    target: Optional[ActionTarget] = core.attr(ActionTarget, default=None)

    def __init__(
        self,
        *,
        action_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = None,
        start_after: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        target: Optional[ActionTarget] = None,
    ):
        super().__init__(
            args=Action.Args(
                action_id=action_id,
                name=name,
                description=description,
                parameter=parameter,
                start_after=start_after,
                target=target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_id: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.arg(
            default=None
        )

        start_after: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        target: Optional[ActionTarget] = core.arg(default=None)


@core.schema
class StopCondition(core.Schema):

    source: Union[str, core.StringOut] = core.attr(str)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        source: Union[str, core.StringOut],
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=StopCondition.Args(
                source=source,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        source: Union[str, core.StringOut] = core.arg()

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ResourceTag(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceTag.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Filter(core.Schema):

    path: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        path: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Filter.Args(
                path=path,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        path: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Target(core.Schema):

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    resource_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    resource_tag: Optional[Union[List[ResourceTag], core.ArrayOut[ResourceTag]]] = core.attr(
        ResourceTag, default=None, kind=core.Kind.array
    )

    resource_type: Union[str, core.StringOut] = core.attr(str)

    selection_mode: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        resource_type: Union[str, core.StringOut],
        selection_mode: Union[str, core.StringOut],
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        resource_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        resource_tag: Optional[Union[List[ResourceTag], core.ArrayOut[ResourceTag]]] = None,
    ):
        super().__init__(
            args=Target.Args(
                name=name,
                resource_type=resource_type,
                selection_mode=selection_mode,
                filter=filter,
                resource_arns=resource_arns,
                resource_tag=resource_tag,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        resource_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        resource_tag: Optional[Union[List[ResourceTag], core.ArrayOut[ResourceTag]]] = core.arg(
            default=None
        )

        resource_type: Union[str, core.StringOut] = core.arg()

        selection_mode: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_fis_experiment_template", namespace="aws_fis")
class ExperimentTemplate(core.Resource):

    action: Union[List[Action], core.ArrayOut[Action]] = core.attr(Action, kind=core.Kind.array)

    description: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    stop_condition: Union[List[StopCondition], core.ArrayOut[StopCondition]] = core.attr(
        StopCondition, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target: Optional[Union[List[Target], core.ArrayOut[Target]]] = core.attr(
        Target, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        action: Union[List[Action], core.ArrayOut[Action]],
        description: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        stop_condition: Union[List[StopCondition], core.ArrayOut[StopCondition]],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        target: Optional[Union[List[Target], core.ArrayOut[Target]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ExperimentTemplate.Args(
                action=action,
                description=description,
                role_arn=role_arn,
                stop_condition=stop_condition,
                tags=tags,
                tags_all=tags_all,
                target=target,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: Union[List[Action], core.ArrayOut[Action]] = core.arg()

        description: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        stop_condition: Union[List[StopCondition], core.ArrayOut[StopCondition]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target: Optional[Union[List[Target], core.ArrayOut[Target]]] = core.arg(default=None)
