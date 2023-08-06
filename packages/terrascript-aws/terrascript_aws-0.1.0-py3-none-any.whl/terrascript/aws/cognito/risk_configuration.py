from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class CompromisedCredentialsRiskConfigurationActions(core.Schema):

    event_action: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        event_action: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CompromisedCredentialsRiskConfigurationActions.Args(
                event_action=event_action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_action: Union[str, core.StringOut] = core.arg()


@core.schema
class CompromisedCredentialsRiskConfiguration(core.Schema):

    actions: CompromisedCredentialsRiskConfigurationActions = core.attr(
        CompromisedCredentialsRiskConfigurationActions
    )

    event_filter: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        actions: CompromisedCredentialsRiskConfigurationActions,
        event_filter: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=CompromisedCredentialsRiskConfiguration.Args(
                actions=actions,
                event_filter=event_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        actions: CompromisedCredentialsRiskConfigurationActions = core.arg()

        event_filter: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class RiskExceptionConfiguration(core.Schema):

    blocked_ip_range_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    skipped_ip_range_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        blocked_ip_range_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        skipped_ip_range_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=RiskExceptionConfiguration.Args(
                blocked_ip_range_list=blocked_ip_range_list,
                skipped_ip_range_list=skipped_ip_range_list,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        blocked_ip_range_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        skipped_ip_range_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class LowAction(core.Schema):

    event_action: Union[str, core.StringOut] = core.attr(str)

    notify: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        event_action: Union[str, core.StringOut],
        notify: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=LowAction.Args(
                event_action=event_action,
                notify=notify,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_action: Union[str, core.StringOut] = core.arg()

        notify: Union[bool, core.BoolOut] = core.arg()


@core.schema
class MediumAction(core.Schema):

    event_action: Union[str, core.StringOut] = core.attr(str)

    notify: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        event_action: Union[str, core.StringOut],
        notify: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=MediumAction.Args(
                event_action=event_action,
                notify=notify,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_action: Union[str, core.StringOut] = core.arg()

        notify: Union[bool, core.BoolOut] = core.arg()


@core.schema
class HighAction(core.Schema):

    event_action: Union[str, core.StringOut] = core.attr(str)

    notify: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        event_action: Union[str, core.StringOut],
        notify: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=HighAction.Args(
                event_action=event_action,
                notify=notify,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_action: Union[str, core.StringOut] = core.arg()

        notify: Union[bool, core.BoolOut] = core.arg()


@core.schema
class AccountTakeoverRiskConfigurationActions(core.Schema):

    high_action: Optional[HighAction] = core.attr(HighAction, default=None)

    low_action: Optional[LowAction] = core.attr(LowAction, default=None)

    medium_action: Optional[MediumAction] = core.attr(MediumAction, default=None)

    def __init__(
        self,
        *,
        high_action: Optional[HighAction] = None,
        low_action: Optional[LowAction] = None,
        medium_action: Optional[MediumAction] = None,
    ):
        super().__init__(
            args=AccountTakeoverRiskConfigurationActions.Args(
                high_action=high_action,
                low_action=low_action,
                medium_action=medium_action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        high_action: Optional[HighAction] = core.arg(default=None)

        low_action: Optional[LowAction] = core.arg(default=None)

        medium_action: Optional[MediumAction] = core.arg(default=None)


@core.schema
class BlockEmail(core.Schema):

    html_body: Union[str, core.StringOut] = core.attr(str)

    subject: Union[str, core.StringOut] = core.attr(str)

    text_body: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        html_body: Union[str, core.StringOut],
        subject: Union[str, core.StringOut],
        text_body: Union[str, core.StringOut],
    ):
        super().__init__(
            args=BlockEmail.Args(
                html_body=html_body,
                subject=subject,
                text_body=text_body,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        html_body: Union[str, core.StringOut] = core.arg()

        subject: Union[str, core.StringOut] = core.arg()

        text_body: Union[str, core.StringOut] = core.arg()


@core.schema
class MfaEmail(core.Schema):

    html_body: Union[str, core.StringOut] = core.attr(str)

    subject: Union[str, core.StringOut] = core.attr(str)

    text_body: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        html_body: Union[str, core.StringOut],
        subject: Union[str, core.StringOut],
        text_body: Union[str, core.StringOut],
    ):
        super().__init__(
            args=MfaEmail.Args(
                html_body=html_body,
                subject=subject,
                text_body=text_body,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        html_body: Union[str, core.StringOut] = core.arg()

        subject: Union[str, core.StringOut] = core.arg()

        text_body: Union[str, core.StringOut] = core.arg()


@core.schema
class NoActionEmail(core.Schema):

    html_body: Union[str, core.StringOut] = core.attr(str)

    subject: Union[str, core.StringOut] = core.attr(str)

    text_body: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        html_body: Union[str, core.StringOut],
        subject: Union[str, core.StringOut],
        text_body: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NoActionEmail.Args(
                html_body=html_body,
                subject=subject,
                text_body=text_body,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        html_body: Union[str, core.StringOut] = core.arg()

        subject: Union[str, core.StringOut] = core.arg()

        text_body: Union[str, core.StringOut] = core.arg()


@core.schema
class NotifyConfiguration(core.Schema):

    block_email: Optional[BlockEmail] = core.attr(BlockEmail, default=None)

    from_: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, alias="from")

    mfa_email: Optional[MfaEmail] = core.attr(MfaEmail, default=None)

    no_action_email: Optional[NoActionEmail] = core.attr(NoActionEmail, default=None)

    reply_to: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        source_arn: Union[str, core.StringOut],
        block_email: Optional[BlockEmail] = None,
        from_: Optional[Union[str, core.StringOut]] = None,
        mfa_email: Optional[MfaEmail] = None,
        no_action_email: Optional[NoActionEmail] = None,
        reply_to: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=NotifyConfiguration.Args(
                source_arn=source_arn,
                block_email=block_email,
                from_=from_,
                mfa_email=mfa_email,
                no_action_email=no_action_email,
                reply_to=reply_to,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        block_email: Optional[BlockEmail] = core.arg(default=None)

        from_: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mfa_email: Optional[MfaEmail] = core.arg(default=None)

        no_action_email: Optional[NoActionEmail] = core.arg(default=None)

        reply_to: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class AccountTakeoverRiskConfiguration(core.Schema):

    actions: AccountTakeoverRiskConfigurationActions = core.attr(
        AccountTakeoverRiskConfigurationActions
    )

    notify_configuration: NotifyConfiguration = core.attr(NotifyConfiguration)

    def __init__(
        self,
        *,
        actions: AccountTakeoverRiskConfigurationActions,
        notify_configuration: NotifyConfiguration,
    ):
        super().__init__(
            args=AccountTakeoverRiskConfiguration.Args(
                actions=actions,
                notify_configuration=notify_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        actions: AccountTakeoverRiskConfigurationActions = core.arg()

        notify_configuration: NotifyConfiguration = core.arg()


@core.resource(type="aws_cognito_risk_configuration", namespace="aws_cognito")
class RiskConfiguration(core.Resource):

    account_takeover_risk_configuration: Optional[AccountTakeoverRiskConfiguration] = core.attr(
        AccountTakeoverRiskConfiguration, default=None
    )

    client_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    compromised_credentials_risk_configuration: Optional[
        CompromisedCredentialsRiskConfiguration
    ] = core.attr(CompromisedCredentialsRiskConfiguration, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    risk_exception_configuration: Optional[RiskExceptionConfiguration] = core.attr(
        RiskExceptionConfiguration, default=None
    )

    user_pool_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user_pool_id: Union[str, core.StringOut],
        account_takeover_risk_configuration: Optional[AccountTakeoverRiskConfiguration] = None,
        client_id: Optional[Union[str, core.StringOut]] = None,
        compromised_credentials_risk_configuration: Optional[
            CompromisedCredentialsRiskConfiguration
        ] = None,
        risk_exception_configuration: Optional[RiskExceptionConfiguration] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RiskConfiguration.Args(
                user_pool_id=user_pool_id,
                account_takeover_risk_configuration=account_takeover_risk_configuration,
                client_id=client_id,
                compromised_credentials_risk_configuration=compromised_credentials_risk_configuration,
                risk_exception_configuration=risk_exception_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_takeover_risk_configuration: Optional[AccountTakeoverRiskConfiguration] = core.arg(
            default=None
        )

        client_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        compromised_credentials_risk_configuration: Optional[
            CompromisedCredentialsRiskConfiguration
        ] = core.arg(default=None)

        risk_exception_configuration: Optional[RiskExceptionConfiguration] = core.arg(default=None)

        user_pool_id: Union[str, core.StringOut] = core.arg()
