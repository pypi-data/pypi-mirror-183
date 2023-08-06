from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class UsernameConfiguration(core.Schema):

    case_sensitive: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        case_sensitive: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=UsernameConfiguration.Args(
                case_sensitive=case_sensitive,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        case_sensitive: Union[bool, core.BoolOut] = core.arg()


@core.schema
class DeviceConfiguration(core.Schema):

    challenge_required_on_new_device: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    device_only_remembered_on_user_prompt: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        *,
        challenge_required_on_new_device: Optional[Union[bool, core.BoolOut]] = None,
        device_only_remembered_on_user_prompt: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=DeviceConfiguration.Args(
                challenge_required_on_new_device=challenge_required_on_new_device,
                device_only_remembered_on_user_prompt=device_only_remembered_on_user_prompt,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        challenge_required_on_new_device: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        device_only_remembered_on_user_prompt: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )


@core.schema
class UserPoolAddOns(core.Schema):

    advanced_security_mode: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        advanced_security_mode: Union[str, core.StringOut],
    ):
        super().__init__(
            args=UserPoolAddOns.Args(
                advanced_security_mode=advanced_security_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        advanced_security_mode: Union[str, core.StringOut] = core.arg()


@core.schema
class SmsConfiguration(core.Schema):

    external_id: Union[str, core.StringOut] = core.attr(str)

    sns_caller_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        external_id: Union[str, core.StringOut],
        sns_caller_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SmsConfiguration.Args(
                external_id=external_id,
                sns_caller_arn=sns_caller_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        external_id: Union[str, core.StringOut] = core.arg()

        sns_caller_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class CustomEmailSender(core.Schema):

    lambda_arn: Union[str, core.StringOut] = core.attr(str)

    lambda_version: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        lambda_arn: Union[str, core.StringOut],
        lambda_version: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CustomEmailSender.Args(
                lambda_arn=lambda_arn,
                lambda_version=lambda_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        lambda_arn: Union[str, core.StringOut] = core.arg()

        lambda_version: Union[str, core.StringOut] = core.arg()


@core.schema
class CustomSmsSender(core.Schema):

    lambda_arn: Union[str, core.StringOut] = core.attr(str)

    lambda_version: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        lambda_arn: Union[str, core.StringOut],
        lambda_version: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CustomSmsSender.Args(
                lambda_arn=lambda_arn,
                lambda_version=lambda_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        lambda_arn: Union[str, core.StringOut] = core.arg()

        lambda_version: Union[str, core.StringOut] = core.arg()


@core.schema
class LambdaConfig(core.Schema):

    create_auth_challenge: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    custom_email_sender: Optional[CustomEmailSender] = core.attr(
        CustomEmailSender, default=None, computed=True
    )

    custom_message: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    custom_sms_sender: Optional[CustomSmsSender] = core.attr(
        CustomSmsSender, default=None, computed=True
    )

    define_auth_challenge: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    post_authentication: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    post_confirmation: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    pre_authentication: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    pre_sign_up: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    pre_token_generation: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_migration: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    verify_auth_challenge_response: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    def __init__(
        self,
        *,
        create_auth_challenge: Optional[Union[str, core.StringOut]] = None,
        custom_email_sender: Optional[CustomEmailSender] = None,
        custom_message: Optional[Union[str, core.StringOut]] = None,
        custom_sms_sender: Optional[CustomSmsSender] = None,
        define_auth_challenge: Optional[Union[str, core.StringOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        post_authentication: Optional[Union[str, core.StringOut]] = None,
        post_confirmation: Optional[Union[str, core.StringOut]] = None,
        pre_authentication: Optional[Union[str, core.StringOut]] = None,
        pre_sign_up: Optional[Union[str, core.StringOut]] = None,
        pre_token_generation: Optional[Union[str, core.StringOut]] = None,
        user_migration: Optional[Union[str, core.StringOut]] = None,
        verify_auth_challenge_response: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LambdaConfig.Args(
                create_auth_challenge=create_auth_challenge,
                custom_email_sender=custom_email_sender,
                custom_message=custom_message,
                custom_sms_sender=custom_sms_sender,
                define_auth_challenge=define_auth_challenge,
                kms_key_id=kms_key_id,
                post_authentication=post_authentication,
                post_confirmation=post_confirmation,
                pre_authentication=pre_authentication,
                pre_sign_up=pre_sign_up,
                pre_token_generation=pre_token_generation,
                user_migration=user_migration,
                verify_auth_challenge_response=verify_auth_challenge_response,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        create_auth_challenge: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        custom_email_sender: Optional[CustomEmailSender] = core.arg(default=None)

        custom_message: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        custom_sms_sender: Optional[CustomSmsSender] = core.arg(default=None)

        define_auth_challenge: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        post_authentication: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        post_confirmation: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        pre_authentication: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        pre_sign_up: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        pre_token_generation: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_migration: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        verify_auth_challenge_response: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )


@core.schema
class RecoveryMechanism(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    priority: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        priority: Union[int, core.IntOut],
    ):
        super().__init__(
            args=RecoveryMechanism.Args(
                name=name,
                priority=priority,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        priority: Union[int, core.IntOut] = core.arg()


@core.schema
class AccountRecoverySetting(core.Schema):

    recovery_mechanism: Union[
        List[RecoveryMechanism], core.ArrayOut[RecoveryMechanism]
    ] = core.attr(RecoveryMechanism, kind=core.Kind.array)

    def __init__(
        self,
        *,
        recovery_mechanism: Union[List[RecoveryMechanism], core.ArrayOut[RecoveryMechanism]],
    ):
        super().__init__(
            args=AccountRecoverySetting.Args(
                recovery_mechanism=recovery_mechanism,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        recovery_mechanism: Union[
            List[RecoveryMechanism], core.ArrayOut[RecoveryMechanism]
        ] = core.arg()


@core.schema
class NumberAttributeConstraints(core.Schema):

    max_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    min_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        max_value: Optional[Union[str, core.StringOut]] = None,
        min_value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=NumberAttributeConstraints.Args(
                max_value=max_value,
                min_value=min_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        min_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class StringAttributeConstraints(core.Schema):

    max_length: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    min_length: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        max_length: Optional[Union[str, core.StringOut]] = None,
        min_length: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=StringAttributeConstraints.Args(
                max_length=max_length,
                min_length=min_length,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_length: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        min_length: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Schema(core.Schema):

    attribute_data_type: Union[str, core.StringOut] = core.attr(str)

    developer_only_attribute: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    mutable: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    number_attribute_constraints: Optional[NumberAttributeConstraints] = core.attr(
        NumberAttributeConstraints, default=None
    )

    required: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    string_attribute_constraints: Optional[StringAttributeConstraints] = core.attr(
        StringAttributeConstraints, default=None
    )

    def __init__(
        self,
        *,
        attribute_data_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        developer_only_attribute: Optional[Union[bool, core.BoolOut]] = None,
        mutable: Optional[Union[bool, core.BoolOut]] = None,
        number_attribute_constraints: Optional[NumberAttributeConstraints] = None,
        required: Optional[Union[bool, core.BoolOut]] = None,
        string_attribute_constraints: Optional[StringAttributeConstraints] = None,
    ):
        super().__init__(
            args=Schema.Args(
                attribute_data_type=attribute_data_type,
                name=name,
                developer_only_attribute=developer_only_attribute,
                mutable=mutable,
                number_attribute_constraints=number_attribute_constraints,
                required=required,
                string_attribute_constraints=string_attribute_constraints,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attribute_data_type: Union[str, core.StringOut] = core.arg()

        developer_only_attribute: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        mutable: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        number_attribute_constraints: Optional[NumberAttributeConstraints] = core.arg(default=None)

        required: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        string_attribute_constraints: Optional[StringAttributeConstraints] = core.arg(default=None)


@core.schema
class EmailConfiguration(core.Schema):

    configuration_set: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    email_sending_account: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    from_email_address: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    reply_to_email_address: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        configuration_set: Optional[Union[str, core.StringOut]] = None,
        email_sending_account: Optional[Union[str, core.StringOut]] = None,
        from_email_address: Optional[Union[str, core.StringOut]] = None,
        reply_to_email_address: Optional[Union[str, core.StringOut]] = None,
        source_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EmailConfiguration.Args(
                configuration_set=configuration_set,
                email_sending_account=email_sending_account,
                from_email_address=from_email_address,
                reply_to_email_address=reply_to_email_address,
                source_arn=source_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        configuration_set: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        email_sending_account: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        from_email_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        reply_to_email_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SoftwareTokenMfaConfiguration(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=SoftwareTokenMfaConfiguration.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class VerificationMessageTemplate(core.Schema):

    default_email_option: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    email_message: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    email_message_by_link: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    email_subject: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    email_subject_by_link: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    sms_message: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        default_email_option: Optional[Union[str, core.StringOut]] = None,
        email_message: Optional[Union[str, core.StringOut]] = None,
        email_message_by_link: Optional[Union[str, core.StringOut]] = None,
        email_subject: Optional[Union[str, core.StringOut]] = None,
        email_subject_by_link: Optional[Union[str, core.StringOut]] = None,
        sms_message: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=VerificationMessageTemplate.Args(
                default_email_option=default_email_option,
                email_message=email_message,
                email_message_by_link=email_message_by_link,
                email_subject=email_subject,
                email_subject_by_link=email_subject_by_link,
                sms_message=sms_message,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_email_option: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        email_message: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        email_message_by_link: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        email_subject: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        email_subject_by_link: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sms_message: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class PasswordPolicy(core.Schema):

    minimum_length: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    require_lowercase: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    require_numbers: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    require_symbols: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    require_uppercase: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    temporary_password_validity_days: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    def __init__(
        self,
        *,
        minimum_length: Optional[Union[int, core.IntOut]] = None,
        require_lowercase: Optional[Union[bool, core.BoolOut]] = None,
        require_numbers: Optional[Union[bool, core.BoolOut]] = None,
        require_symbols: Optional[Union[bool, core.BoolOut]] = None,
        require_uppercase: Optional[Union[bool, core.BoolOut]] = None,
        temporary_password_validity_days: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=PasswordPolicy.Args(
                minimum_length=minimum_length,
                require_lowercase=require_lowercase,
                require_numbers=require_numbers,
                require_symbols=require_symbols,
                require_uppercase=require_uppercase,
                temporary_password_validity_days=temporary_password_validity_days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        minimum_length: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        require_lowercase: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        require_numbers: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        require_symbols: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        require_uppercase: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        temporary_password_validity_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class InviteMessageTemplate(core.Schema):

    email_message: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    email_subject: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sms_message: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        email_message: Optional[Union[str, core.StringOut]] = None,
        email_subject: Optional[Union[str, core.StringOut]] = None,
        sms_message: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InviteMessageTemplate.Args(
                email_message=email_message,
                email_subject=email_subject,
                sms_message=sms_message,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        email_message: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        email_subject: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sms_message: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AdminCreateUserConfig(core.Schema):

    allow_admin_create_user_only: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    invite_message_template: Optional[InviteMessageTemplate] = core.attr(
        InviteMessageTemplate, default=None
    )

    def __init__(
        self,
        *,
        allow_admin_create_user_only: Optional[Union[bool, core.BoolOut]] = None,
        invite_message_template: Optional[InviteMessageTemplate] = None,
    ):
        super().__init__(
            args=AdminCreateUserConfig.Args(
                allow_admin_create_user_only=allow_admin_create_user_only,
                invite_message_template=invite_message_template,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_admin_create_user_only: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        invite_message_template: Optional[InviteMessageTemplate] = core.arg(default=None)


@core.resource(type="aws_cognito_user_pool", namespace="aws_cognito")
class UserPool(core.Resource):
    """
    (Optional) Configuration block to define which verified available method a user can use to recover t
    heir forgotten password. [Detailed below](#account_recovery_setting).
    """

    account_recovery_setting: Optional[AccountRecoverySetting] = core.attr(
        AccountRecoverySetting, default=None
    )

    """
    (Optional) Configuration block for creating a new user profile. [Detailed below](#admin_create_user_
    config).
    """
    admin_create_user_config: Optional[AdminCreateUserConfig] = core.attr(
        AdminCreateUserConfig, default=None, computed=True
    )

    """
    (Optional) Attributes supported as an alias for this user pool. Valid values: `phone_number`, `email
    , or `preferred_username`. Conflicts with `username_attributes`.
    """
    alias_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    ARN of the user pool.
    """
    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) Attributes to be auto-verified. Valid values: `email`, `phone_number`.
    """
    auto_verified_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Date the user pool was created.
    """
    creation_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    A custom domain name that you provide to Amazon Cognito. This parameter applies only if you use a cu
    stom domain to host the sign-up and sign-in pages for your application. For example: `auth.example.c
    om`.
    """
    custom_domain: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) Configuration block for the user pool's device tracking. [Detailed below](#device_configu
    ration).
    """
    device_configuration: Optional[DeviceConfiguration] = core.attr(
        DeviceConfiguration, default=None
    )

    """
    Holds the domain prefix if the user pool has a domain associated with it.
    """
    domain: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) Configuration block for configuring email. [Detailed below](#email_configuration).
    """
    email_configuration: Optional[EmailConfiguration] = core.attr(EmailConfiguration, default=None)

    """
    (Optional) String representing the email verification message. Conflicts with `verification_message_
    template` configuration block `email_message` argument.
    """
    email_verification_message: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) String representing the email verification subject. Conflicts with `verification_message_
    template` configuration block `email_subject` argument.
    """
    email_verification_subject: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    """
    Endpoint name of the user pool. Example format: `cognito-idp.REGION.amazonaws.com/xxxx_yyyyy`
    """
    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    A number estimating the size of the user pool.
    """
    estimated_number_of_users: Union[int, core.IntOut] = core.attr(int, computed=True)

    """
    ID of the user pool.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) Configuration block for the AWS Lambda triggers associated with the user pool. [Detailed
    below](#lambda_config).
    """
    lambda_config: Optional[LambdaConfig] = core.attr(LambdaConfig, default=None)

    """
    Date the user pool was last modified.
    """
    last_modified_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) Multi-Factor Authentication (MFA) configuration for the User Pool. Defaults of `OFF`. Val
    id values are `OFF` (MFA Tokens are not required), `ON` (MFA is required for all users to sign in; r
    equires at least one of `sms_configuration` or `software_token_mfa_configuration` to be configured),
    or `OPTIONAL` (MFA Will be required only for individual users who have MFA Enabled; requires at lea
    st one of `sms_configuration` or `software_token_mfa_configuration` to be configured).
    """
    mfa_configuration: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Required) Name of the user pool.
    """
    name: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) Configuration blocked for information about the user pool password policy. [Detailed belo
    w](#password_policy).
    """
    password_policy: Optional[PasswordPolicy] = core.attr(
        PasswordPolicy, default=None, computed=True
    )

    """
    (Optional) Configuration block for the schema attributes of a user pool. [Detailed below](#schema).
    Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/devel
    operguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be
    specified if they are different from the default configuration. Attributes can be added, but not mo
    dified or removed. Maximum of 50 attributes.
    """
    schema: Optional[Union[List[Schema], core.ArrayOut[Schema]]] = core.attr(
        Schema, default=None, kind=core.Kind.array
    )

    """
    (Optional) String representing the SMS authentication message. The Message must contain the `{####}`
    placeholder, which will be replaced with the code.
    """
    sms_authentication_message: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Optional) Configuration block for Short Message Service (SMS) settings. [Detailed below](#sms_confi
    guration). These settings apply to SMS user verification and SMS Multi-Factor Authentication (MFA).
    Due to Cognito API restrictions, the SMS configuration cannot be removed without recreating the Cogn
    ito User Pool. For user data safety, this resource will ignore the removal of this configuration by
    disabling drift detection. To force resource recreation after this configuration has been applied, s
    ee the [`taint` command](https://www.terraform.io/docs/commands/taint.html).
    """
    sms_configuration: Optional[SmsConfiguration] = core.attr(
        SmsConfiguration, default=None, computed=True
    )

    """
    (Optional) String representing the SMS verification message. Conflicts with `verification_message_te
    mplate` configuration block `sms_message` argument.
    """
    sms_verification_message: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Configuration block for software token Mult-Factor Authentication (MFA) settings. [Detail
    ed below](#software_token_mfa_configuration).
    """
    software_token_mfa_configuration: Optional[SoftwareTokenMfaConfiguration] = core.attr(
        SoftwareTokenMfaConfiguration, default=None
    )

    """
    (Optional) Map of tags to assign to the User Pool. If configured with a provider [`default_tags` con
    figuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-con
    figuration-block) present, tags with matching keys will overwrite those defined at the provider-leve
    l.
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
    (Optional) Configuration block for user pool add-ons to enable user pool advanced security mode feat
    ures. [Detailed below](#user_pool_add_ons).
    """
    user_pool_add_ons: Optional[UserPoolAddOns] = core.attr(UserPoolAddOns, default=None)

    """
    (Optional) Whether email addresses or phone numbers can be specified as usernames when a user signs
    up. Conflicts with `alias_attributes`.
    """
    username_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Configuration block for username configuration. [Detailed below](#username_configuration)
    .
    """
    username_configuration: Optional[UsernameConfiguration] = core.attr(
        UsernameConfiguration, default=None
    )

    """
    (Optional) Configuration block for verification message templates. [Detailed below](#verification_me
    ssage_template).
    """
    verification_message_template: Optional[VerificationMessageTemplate] = core.attr(
        VerificationMessageTemplate, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        account_recovery_setting: Optional[AccountRecoverySetting] = None,
        admin_create_user_config: Optional[AdminCreateUserConfig] = None,
        alias_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        auto_verified_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        device_configuration: Optional[DeviceConfiguration] = None,
        email_configuration: Optional[EmailConfiguration] = None,
        email_verification_message: Optional[Union[str, core.StringOut]] = None,
        email_verification_subject: Optional[Union[str, core.StringOut]] = None,
        lambda_config: Optional[LambdaConfig] = None,
        mfa_configuration: Optional[Union[str, core.StringOut]] = None,
        password_policy: Optional[PasswordPolicy] = None,
        schema: Optional[Union[List[Schema], core.ArrayOut[Schema]]] = None,
        sms_authentication_message: Optional[Union[str, core.StringOut]] = None,
        sms_configuration: Optional[SmsConfiguration] = None,
        sms_verification_message: Optional[Union[str, core.StringOut]] = None,
        software_token_mfa_configuration: Optional[SoftwareTokenMfaConfiguration] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        user_pool_add_ons: Optional[UserPoolAddOns] = None,
        username_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        username_configuration: Optional[UsernameConfiguration] = None,
        verification_message_template: Optional[VerificationMessageTemplate] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserPool.Args(
                name=name,
                account_recovery_setting=account_recovery_setting,
                admin_create_user_config=admin_create_user_config,
                alias_attributes=alias_attributes,
                auto_verified_attributes=auto_verified_attributes,
                device_configuration=device_configuration,
                email_configuration=email_configuration,
                email_verification_message=email_verification_message,
                email_verification_subject=email_verification_subject,
                lambda_config=lambda_config,
                mfa_configuration=mfa_configuration,
                password_policy=password_policy,
                schema=schema,
                sms_authentication_message=sms_authentication_message,
                sms_configuration=sms_configuration,
                sms_verification_message=sms_verification_message,
                software_token_mfa_configuration=software_token_mfa_configuration,
                tags=tags,
                tags_all=tags_all,
                user_pool_add_ons=user_pool_add_ons,
                username_attributes=username_attributes,
                username_configuration=username_configuration,
                verification_message_template=verification_message_template,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_recovery_setting: Optional[AccountRecoverySetting] = core.arg(default=None)

        admin_create_user_config: Optional[AdminCreateUserConfig] = core.arg(default=None)

        alias_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        auto_verified_attributes: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        device_configuration: Optional[DeviceConfiguration] = core.arg(default=None)

        email_configuration: Optional[EmailConfiguration] = core.arg(default=None)

        email_verification_message: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        email_verification_subject: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lambda_config: Optional[LambdaConfig] = core.arg(default=None)

        mfa_configuration: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        password_policy: Optional[PasswordPolicy] = core.arg(default=None)

        schema: Optional[Union[List[Schema], core.ArrayOut[Schema]]] = core.arg(default=None)

        sms_authentication_message: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sms_configuration: Optional[SmsConfiguration] = core.arg(default=None)

        sms_verification_message: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        software_token_mfa_configuration: Optional[SoftwareTokenMfaConfiguration] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_pool_add_ons: Optional[UserPoolAddOns] = core.arg(default=None)

        username_attributes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        username_configuration: Optional[UsernameConfiguration] = core.arg(default=None)

        verification_message_template: Optional[VerificationMessageTemplate] = core.arg(
            default=None
        )
