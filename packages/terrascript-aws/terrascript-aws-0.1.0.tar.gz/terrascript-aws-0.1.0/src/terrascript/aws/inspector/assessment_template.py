from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EventSubscription(core.Schema):

    event: Union[str, core.StringOut] = core.attr(str)

    topic_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        event: Union[str, core.StringOut],
        topic_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EventSubscription.Args(
                event=event,
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event: Union[str, core.StringOut] = core.arg()

        topic_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_inspector_assessment_template", namespace="aws_inspector")
class AssessmentTemplate(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    duration: Union[int, core.IntOut] = core.attr(int)

    event_subscription: Optional[
        Union[List[EventSubscription], core.ArrayOut[EventSubscription]]
    ] = core.attr(EventSubscription, default=None, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    rules_package_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        duration: Union[int, core.IntOut],
        name: Union[str, core.StringOut],
        rules_package_arns: Union[List[str], core.ArrayOut[core.StringOut]],
        target_arn: Union[str, core.StringOut],
        event_subscription: Optional[
            Union[List[EventSubscription], core.ArrayOut[EventSubscription]]
        ] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AssessmentTemplate.Args(
                duration=duration,
                name=name,
                rules_package_arns=rules_package_arns,
                target_arn=target_arn,
                event_subscription=event_subscription,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        duration: Union[int, core.IntOut] = core.arg()

        event_subscription: Optional[
            Union[List[EventSubscription], core.ArrayOut[EventSubscription]]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        rules_package_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_arn: Union[str, core.StringOut] = core.arg()
