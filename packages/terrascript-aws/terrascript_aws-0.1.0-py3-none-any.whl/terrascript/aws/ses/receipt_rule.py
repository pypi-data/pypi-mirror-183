from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class BounceAction(core.Schema):

    message: Union[str, core.StringOut] = core.attr(str)

    position: Union[int, core.IntOut] = core.attr(int)

    sender: Union[str, core.StringOut] = core.attr(str)

    smtp_reply_code: Union[str, core.StringOut] = core.attr(str)

    status_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    topic_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        message: Union[str, core.StringOut],
        position: Union[int, core.IntOut],
        sender: Union[str, core.StringOut],
        smtp_reply_code: Union[str, core.StringOut],
        status_code: Optional[Union[str, core.StringOut]] = None,
        topic_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=BounceAction.Args(
                message=message,
                position=position,
                sender=sender,
                smtp_reply_code=smtp_reply_code,
                status_code=status_code,
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message: Union[str, core.StringOut] = core.arg()

        position: Union[int, core.IntOut] = core.arg()

        sender: Union[str, core.StringOut] = core.arg()

        smtp_reply_code: Union[str, core.StringOut] = core.arg()

        status_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        topic_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class WorkmailAction(core.Schema):

    organization_arn: Union[str, core.StringOut] = core.attr(str)

    position: Union[int, core.IntOut] = core.attr(int)

    topic_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        organization_arn: Union[str, core.StringOut],
        position: Union[int, core.IntOut],
        topic_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=WorkmailAction.Args(
                organization_arn=organization_arn,
                position=position,
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        organization_arn: Union[str, core.StringOut] = core.arg()

        position: Union[int, core.IntOut] = core.arg()

        topic_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class StopAction(core.Schema):

    position: Union[int, core.IntOut] = core.attr(int)

    scope: Union[str, core.StringOut] = core.attr(str)

    topic_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        position: Union[int, core.IntOut],
        scope: Union[str, core.StringOut],
        topic_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=StopAction.Args(
                position=position,
                scope=scope,
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        position: Union[int, core.IntOut] = core.arg()

        scope: Union[str, core.StringOut] = core.arg()

        topic_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class S3Action(core.Schema):

    bucket_name: Union[str, core.StringOut] = core.attr(str)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    object_key_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    position: Union[int, core.IntOut] = core.attr(int)

    topic_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_name: Union[str, core.StringOut],
        position: Union[int, core.IntOut],
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        object_key_prefix: Optional[Union[str, core.StringOut]] = None,
        topic_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3Action.Args(
                bucket_name=bucket_name,
                position=position,
                kms_key_arn=kms_key_arn,
                object_key_prefix=object_key_prefix,
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Union[str, core.StringOut] = core.arg()

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        object_key_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        position: Union[int, core.IntOut] = core.arg()

        topic_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class LambdaAction(core.Schema):

    function_arn: Union[str, core.StringOut] = core.attr(str)

    invocation_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    position: Union[int, core.IntOut] = core.attr(int)

    topic_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        function_arn: Union[str, core.StringOut],
        position: Union[int, core.IntOut],
        invocation_type: Optional[Union[str, core.StringOut]] = None,
        topic_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LambdaAction.Args(
                function_arn=function_arn,
                position=position,
                invocation_type=invocation_type,
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_arn: Union[str, core.StringOut] = core.arg()

        invocation_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        position: Union[int, core.IntOut] = core.arg()

        topic_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AddHeaderAction(core.Schema):

    header_name: Union[str, core.StringOut] = core.attr(str)

    header_value: Union[str, core.StringOut] = core.attr(str)

    position: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        header_name: Union[str, core.StringOut],
        header_value: Union[str, core.StringOut],
        position: Union[int, core.IntOut],
    ):
        super().__init__(
            args=AddHeaderAction.Args(
                header_name=header_name,
                header_value=header_value,
                position=position,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        header_name: Union[str, core.StringOut] = core.arg()

        header_value: Union[str, core.StringOut] = core.arg()

        position: Union[int, core.IntOut] = core.arg()


@core.schema
class SnsAction(core.Schema):

    encoding: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    position: Union[int, core.IntOut] = core.attr(int)

    topic_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        position: Union[int, core.IntOut],
        topic_arn: Union[str, core.StringOut],
        encoding: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SnsAction.Args(
                position=position,
                topic_arn=topic_arn,
                encoding=encoding,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encoding: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        position: Union[int, core.IntOut] = core.arg()

        topic_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_ses_receipt_rule", namespace="aws_ses")
class ReceiptRule(core.Resource):

    add_header_action: Optional[
        Union[List[AddHeaderAction], core.ArrayOut[AddHeaderAction]]
    ] = core.attr(AddHeaderAction, default=None, kind=core.Kind.array)

    after: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    bounce_action: Optional[Union[List[BounceAction], core.ArrayOut[BounceAction]]] = core.attr(
        BounceAction, default=None, kind=core.Kind.array
    )

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lambda_action: Optional[Union[List[LambdaAction], core.ArrayOut[LambdaAction]]] = core.attr(
        LambdaAction, default=None, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    recipients: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    rule_set_name: Union[str, core.StringOut] = core.attr(str)

    s3_action: Optional[Union[List[S3Action], core.ArrayOut[S3Action]]] = core.attr(
        S3Action, default=None, kind=core.Kind.array
    )

    scan_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    sns_action: Optional[Union[List[SnsAction], core.ArrayOut[SnsAction]]] = core.attr(
        SnsAction, default=None, kind=core.Kind.array
    )

    stop_action: Optional[Union[List[StopAction], core.ArrayOut[StopAction]]] = core.attr(
        StopAction, default=None, kind=core.Kind.array
    )

    tls_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    workmail_action: Optional[
        Union[List[WorkmailAction], core.ArrayOut[WorkmailAction]]
    ] = core.attr(WorkmailAction, default=None, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        rule_set_name: Union[str, core.StringOut],
        add_header_action: Optional[
            Union[List[AddHeaderAction], core.ArrayOut[AddHeaderAction]]
        ] = None,
        after: Optional[Union[str, core.StringOut]] = None,
        bounce_action: Optional[Union[List[BounceAction], core.ArrayOut[BounceAction]]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        lambda_action: Optional[Union[List[LambdaAction], core.ArrayOut[LambdaAction]]] = None,
        recipients: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        s3_action: Optional[Union[List[S3Action], core.ArrayOut[S3Action]]] = None,
        scan_enabled: Optional[Union[bool, core.BoolOut]] = None,
        sns_action: Optional[Union[List[SnsAction], core.ArrayOut[SnsAction]]] = None,
        stop_action: Optional[Union[List[StopAction], core.ArrayOut[StopAction]]] = None,
        tls_policy: Optional[Union[str, core.StringOut]] = None,
        workmail_action: Optional[
            Union[List[WorkmailAction], core.ArrayOut[WorkmailAction]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReceiptRule.Args(
                name=name,
                rule_set_name=rule_set_name,
                add_header_action=add_header_action,
                after=after,
                bounce_action=bounce_action,
                enabled=enabled,
                lambda_action=lambda_action,
                recipients=recipients,
                s3_action=s3_action,
                scan_enabled=scan_enabled,
                sns_action=sns_action,
                stop_action=stop_action,
                tls_policy=tls_policy,
                workmail_action=workmail_action,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        add_header_action: Optional[
            Union[List[AddHeaderAction], core.ArrayOut[AddHeaderAction]]
        ] = core.arg(default=None)

        after: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bounce_action: Optional[Union[List[BounceAction], core.ArrayOut[BounceAction]]] = core.arg(
            default=None
        )

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        lambda_action: Optional[Union[List[LambdaAction], core.ArrayOut[LambdaAction]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        recipients: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        rule_set_name: Union[str, core.StringOut] = core.arg()

        s3_action: Optional[Union[List[S3Action], core.ArrayOut[S3Action]]] = core.arg(default=None)

        scan_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        sns_action: Optional[Union[List[SnsAction], core.ArrayOut[SnsAction]]] = core.arg(
            default=None
        )

        stop_action: Optional[Union[List[StopAction], core.ArrayOut[StopAction]]] = core.arg(
            default=None
        )

        tls_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        workmail_action: Optional[
            Union[List[WorkmailAction], core.ArrayOut[WorkmailAction]]
        ] = core.arg(default=None)
