from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudformation_stack", namespace="aws_cloudformation")
class Stack(core.Resource):

    capabilities: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    disable_rollback: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    iam_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    notification_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    on_failure: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    outputs: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    policy_body: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    policy_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    template_body: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    template_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    timeout_in_minutes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        capabilities: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        disable_rollback: Optional[Union[bool, core.BoolOut]] = None,
        iam_role_arn: Optional[Union[str, core.StringOut]] = None,
        notification_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        on_failure: Optional[Union[str, core.StringOut]] = None,
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        policy_body: Optional[Union[str, core.StringOut]] = None,
        policy_url: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        template_body: Optional[Union[str, core.StringOut]] = None,
        template_url: Optional[Union[str, core.StringOut]] = None,
        timeout_in_minutes: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stack.Args(
                name=name,
                capabilities=capabilities,
                disable_rollback=disable_rollback,
                iam_role_arn=iam_role_arn,
                notification_arns=notification_arns,
                on_failure=on_failure,
                parameters=parameters,
                policy_body=policy_body,
                policy_url=policy_url,
                tags=tags,
                tags_all=tags_all,
                template_body=template_body,
                template_url=template_url,
                timeout_in_minutes=timeout_in_minutes,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capabilities: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        disable_rollback: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        iam_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        notification_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        on_failure: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        policy_body: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        template_body: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        template_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        timeout_in_minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)
