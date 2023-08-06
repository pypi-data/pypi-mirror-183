from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Notification(core.Schema):

    comparison_operator: Union[str, core.StringOut] = core.attr(str)

    notification_type: Union[str, core.StringOut] = core.attr(str)

    subscriber_email_addresses: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    subscriber_sns_topic_arns: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    threshold: Union[float, core.FloatOut] = core.attr(float)

    threshold_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison_operator: Union[str, core.StringOut],
        notification_type: Union[str, core.StringOut],
        threshold: Union[float, core.FloatOut],
        threshold_type: Union[str, core.StringOut],
        subscriber_email_addresses: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        subscriber_sns_topic_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Notification.Args(
                comparison_operator=comparison_operator,
                notification_type=notification_type,
                threshold=threshold,
                threshold_type=threshold_type,
                subscriber_email_addresses=subscriber_email_addresses,
                subscriber_sns_topic_arns=subscriber_sns_topic_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison_operator: Union[str, core.StringOut] = core.arg()

        notification_type: Union[str, core.StringOut] = core.arg()

        subscriber_email_addresses: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        subscriber_sns_topic_arns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        threshold: Union[float, core.FloatOut] = core.arg()

        threshold_type: Union[str, core.StringOut] = core.arg()


@core.schema
class CostFilter(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=CostFilter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class CostTypes(core.Schema):

    include_credit: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_discount: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_other_subscription: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_recurring: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_refund: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_subscription: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_support: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_tax: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_upfront: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    use_amortized: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    use_blended: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        include_credit: Optional[Union[bool, core.BoolOut]] = None,
        include_discount: Optional[Union[bool, core.BoolOut]] = None,
        include_other_subscription: Optional[Union[bool, core.BoolOut]] = None,
        include_recurring: Optional[Union[bool, core.BoolOut]] = None,
        include_refund: Optional[Union[bool, core.BoolOut]] = None,
        include_subscription: Optional[Union[bool, core.BoolOut]] = None,
        include_support: Optional[Union[bool, core.BoolOut]] = None,
        include_tax: Optional[Union[bool, core.BoolOut]] = None,
        include_upfront: Optional[Union[bool, core.BoolOut]] = None,
        use_amortized: Optional[Union[bool, core.BoolOut]] = None,
        use_blended: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=CostTypes.Args(
                include_credit=include_credit,
                include_discount=include_discount,
                include_other_subscription=include_other_subscription,
                include_recurring=include_recurring,
                include_refund=include_refund,
                include_subscription=include_subscription,
                include_support=include_support,
                include_tax=include_tax,
                include_upfront=include_upfront,
                use_amortized=use_amortized,
                use_blended=use_blended,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        include_credit: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_discount: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_other_subscription: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_recurring: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_refund: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_subscription: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_support: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_tax: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_upfront: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        use_amortized: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        use_blended: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.resource(type="aws_budgets_budget", namespace="aws_budgets")
class Budget(core.Resource):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    budget_type: Union[str, core.StringOut] = core.attr(str)

    cost_filter: Optional[Union[List[CostFilter], core.ArrayOut[CostFilter]]] = core.attr(
        CostFilter, default=None, computed=True, kind=core.Kind.array
    )

    cost_filters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    cost_types: Optional[CostTypes] = core.attr(CostTypes, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    limit_amount: Union[str, core.StringOut] = core.attr(str)

    limit_unit: Union[str, core.StringOut] = core.attr(str)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    notification: Optional[Union[List[Notification], core.ArrayOut[Notification]]] = core.attr(
        Notification, default=None, kind=core.Kind.array
    )

    time_period_end: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    time_period_start: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    time_unit: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        budget_type: Union[str, core.StringOut],
        limit_amount: Union[str, core.StringOut],
        limit_unit: Union[str, core.StringOut],
        time_unit: Union[str, core.StringOut],
        account_id: Optional[Union[str, core.StringOut]] = None,
        cost_filter: Optional[Union[List[CostFilter], core.ArrayOut[CostFilter]]] = None,
        cost_filters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        cost_types: Optional[CostTypes] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        notification: Optional[Union[List[Notification], core.ArrayOut[Notification]]] = None,
        time_period_end: Optional[Union[str, core.StringOut]] = None,
        time_period_start: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Budget.Args(
                budget_type=budget_type,
                limit_amount=limit_amount,
                limit_unit=limit_unit,
                time_unit=time_unit,
                account_id=account_id,
                cost_filter=cost_filter,
                cost_filters=cost_filters,
                cost_types=cost_types,
                name=name,
                name_prefix=name_prefix,
                notification=notification,
                time_period_end=time_period_end,
                time_period_start=time_period_start,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        budget_type: Union[str, core.StringOut] = core.arg()

        cost_filter: Optional[Union[List[CostFilter], core.ArrayOut[CostFilter]]] = core.arg(
            default=None
        )

        cost_filters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        cost_types: Optional[CostTypes] = core.arg(default=None)

        limit_amount: Union[str, core.StringOut] = core.arg()

        limit_unit: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        notification: Optional[Union[List[Notification], core.ArrayOut[Notification]]] = core.arg(
            default=None
        )

        time_period_end: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        time_period_start: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        time_unit: Union[str, core.StringOut] = core.arg()
