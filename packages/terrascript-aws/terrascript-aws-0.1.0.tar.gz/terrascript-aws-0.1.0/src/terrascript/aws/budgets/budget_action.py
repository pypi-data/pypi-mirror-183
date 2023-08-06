from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class SsmActionDefinition(core.Schema):

    action_sub_type: Union[str, core.StringOut] = core.attr(str)

    instance_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    region: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        action_sub_type: Union[str, core.StringOut],
        instance_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        region: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SsmActionDefinition.Args(
                action_sub_type=action_sub_type,
                instance_ids=instance_ids,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_sub_type: Union[str, core.StringOut] = core.arg()

        instance_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        region: Union[str, core.StringOut] = core.arg()


@core.schema
class ScpActionDefinition(core.Schema):

    policy_id: Union[str, core.StringOut] = core.attr(str)

    target_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        policy_id: Union[str, core.StringOut],
        target_ids: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=ScpActionDefinition.Args(
                policy_id=policy_id,
                target_ids=target_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        policy_id: Union[str, core.StringOut] = core.arg()

        target_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class IamActionDefinition(core.Schema):

    groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    policy_arn: Union[str, core.StringOut] = core.attr(str)

    roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    users: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        policy_arn: Union[str, core.StringOut],
        groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        users: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=IamActionDefinition.Args(
                policy_arn=policy_arn,
                groups=groups,
                roles=roles,
                users=users,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        policy_arn: Union[str, core.StringOut] = core.arg()

        roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        users: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class Definition(core.Schema):

    iam_action_definition: Optional[IamActionDefinition] = core.attr(
        IamActionDefinition, default=None
    )

    scp_action_definition: Optional[ScpActionDefinition] = core.attr(
        ScpActionDefinition, default=None
    )

    ssm_action_definition: Optional[SsmActionDefinition] = core.attr(
        SsmActionDefinition, default=None
    )

    def __init__(
        self,
        *,
        iam_action_definition: Optional[IamActionDefinition] = None,
        scp_action_definition: Optional[ScpActionDefinition] = None,
        ssm_action_definition: Optional[SsmActionDefinition] = None,
    ):
        super().__init__(
            args=Definition.Args(
                iam_action_definition=iam_action_definition,
                scp_action_definition=scp_action_definition,
                ssm_action_definition=ssm_action_definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iam_action_definition: Optional[IamActionDefinition] = core.arg(default=None)

        scp_action_definition: Optional[ScpActionDefinition] = core.arg(default=None)

        ssm_action_definition: Optional[SsmActionDefinition] = core.arg(default=None)


@core.schema
class ActionThreshold(core.Schema):

    action_threshold_type: Union[str, core.StringOut] = core.attr(str)

    action_threshold_value: Union[float, core.FloatOut] = core.attr(float)

    def __init__(
        self,
        *,
        action_threshold_type: Union[str, core.StringOut],
        action_threshold_value: Union[float, core.FloatOut],
    ):
        super().__init__(
            args=ActionThreshold.Args(
                action_threshold_type=action_threshold_type,
                action_threshold_value=action_threshold_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_threshold_type: Union[str, core.StringOut] = core.arg()

        action_threshold_value: Union[float, core.FloatOut] = core.arg()


@core.schema
class Subscriber(core.Schema):

    address: Union[str, core.StringOut] = core.attr(str)

    subscription_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        address: Union[str, core.StringOut],
        subscription_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Subscriber.Args(
                address=address,
                subscription_type=subscription_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: Union[str, core.StringOut] = core.arg()

        subscription_type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_budgets_budget_action", namespace="aws_budgets")
class BudgetAction(core.Resource):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    action_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    action_threshold: ActionThreshold = core.attr(ActionThreshold)

    action_type: Union[str, core.StringOut] = core.attr(str)

    approval_model: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    budget_name: Union[str, core.StringOut] = core.attr(str)

    definition: Definition = core.attr(Definition)

    execution_role_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    notification_type: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    subscriber: Union[List[Subscriber], core.ArrayOut[Subscriber]] = core.attr(
        Subscriber, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        action_threshold: ActionThreshold,
        action_type: Union[str, core.StringOut],
        approval_model: Union[str, core.StringOut],
        budget_name: Union[str, core.StringOut],
        definition: Definition,
        execution_role_arn: Union[str, core.StringOut],
        notification_type: Union[str, core.StringOut],
        subscriber: Union[List[Subscriber], core.ArrayOut[Subscriber]],
        account_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BudgetAction.Args(
                action_threshold=action_threshold,
                action_type=action_type,
                approval_model=approval_model,
                budget_name=budget_name,
                definition=definition,
                execution_role_arn=execution_role_arn,
                notification_type=notification_type,
                subscriber=subscriber,
                account_id=account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        action_threshold: ActionThreshold = core.arg()

        action_type: Union[str, core.StringOut] = core.arg()

        approval_model: Union[str, core.StringOut] = core.arg()

        budget_name: Union[str, core.StringOut] = core.arg()

        definition: Definition = core.arg()

        execution_role_arn: Union[str, core.StringOut] = core.arg()

        notification_type: Union[str, core.StringOut] = core.arg()

        subscriber: Union[List[Subscriber], core.ArrayOut[Subscriber]] = core.arg()
