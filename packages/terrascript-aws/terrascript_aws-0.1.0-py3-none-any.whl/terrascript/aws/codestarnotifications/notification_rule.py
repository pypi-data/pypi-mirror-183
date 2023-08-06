from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Target(core.Schema):

    address: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        address: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Target.Args(
                address=address,
                status=status,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: Union[str, core.StringOut] = core.arg()

        status: Union[str, core.StringOut] = core.arg()

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(
    type="aws_codestarnotifications_notification_rule", namespace="aws_codestarnotifications"
)
class NotificationRule(core.Resource):
    """
    The codestar notification rule ARN.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The level of detail to include in the notifications for this resource. Possible values ar
    e `BASIC` and `FULL`.
    """
    detail_type: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) A list of event types associated with this notification rule.
    """
    event_type_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    """
    The codestar notification rule ARN.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The name of notification rule.
    """
    name: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) The ARN of the resource to associate with the notification rule.
    """
    resource: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) The status of the notification rule. Possible values are `ENABLED` and `DISABLED`, defaul
    t is `ENABLED`.
    """
    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Configuration blocks containing notification target information. Can be specified multipl
    e times. At least one target must be specified on creation.
    """
    target: Optional[Union[List[Target], core.ArrayOut[Target]]] = core.attr(
        Target, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        detail_type: Union[str, core.StringOut],
        event_type_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        name: Union[str, core.StringOut],
        resource: Union[str, core.StringOut],
        status: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        target: Optional[Union[List[Target], core.ArrayOut[Target]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=NotificationRule.Args(
                detail_type=detail_type,
                event_type_ids=event_type_ids,
                name=name,
                resource=resource,
                status=status,
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
        detail_type: Union[str, core.StringOut] = core.arg()

        event_type_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        resource: Union[str, core.StringOut] = core.arg()

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target: Optional[Union[List[Target], core.ArrayOut[Target]]] = core.arg(default=None)
