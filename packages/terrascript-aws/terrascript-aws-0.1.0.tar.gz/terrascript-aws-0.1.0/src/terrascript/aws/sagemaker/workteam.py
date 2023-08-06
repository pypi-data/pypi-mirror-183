from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CognitoMemberDefinition(core.Schema):

    client_id: Union[str, core.StringOut] = core.attr(str)

    user_group: Union[str, core.StringOut] = core.attr(str)

    user_pool: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        client_id: Union[str, core.StringOut],
        user_group: Union[str, core.StringOut],
        user_pool: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CognitoMemberDefinition.Args(
                client_id=client_id,
                user_group=user_group,
                user_pool=user_pool,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_id: Union[str, core.StringOut] = core.arg()

        user_group: Union[str, core.StringOut] = core.arg()

        user_pool: Union[str, core.StringOut] = core.arg()


@core.schema
class OidcMemberDefinition(core.Schema):

    groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        groups: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=OidcMemberDefinition.Args(
                groups=groups,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class MemberDefinition(core.Schema):

    cognito_member_definition: Optional[CognitoMemberDefinition] = core.attr(
        CognitoMemberDefinition, default=None
    )

    oidc_member_definition: Optional[OidcMemberDefinition] = core.attr(
        OidcMemberDefinition, default=None
    )

    def __init__(
        self,
        *,
        cognito_member_definition: Optional[CognitoMemberDefinition] = None,
        oidc_member_definition: Optional[OidcMemberDefinition] = None,
    ):
        super().__init__(
            args=MemberDefinition.Args(
                cognito_member_definition=cognito_member_definition,
                oidc_member_definition=oidc_member_definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cognito_member_definition: Optional[CognitoMemberDefinition] = core.arg(default=None)

        oidc_member_definition: Optional[OidcMemberDefinition] = core.arg(default=None)


@core.schema
class NotificationConfiguration(core.Schema):

    notification_topic_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        notification_topic_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=NotificationConfiguration.Args(
                notification_topic_arn=notification_topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        notification_topic_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_sagemaker_workteam", namespace="aws_sagemaker")
class Workteam(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    member_definition: Union[List[MemberDefinition], core.ArrayOut[MemberDefinition]] = core.attr(
        MemberDefinition, kind=core.Kind.array
    )

    notification_configuration: Optional[NotificationConfiguration] = core.attr(
        NotificationConfiguration, default=None
    )

    subdomain: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    workforce_name: Union[str, core.StringOut] = core.attr(str)

    workteam_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        description: Union[str, core.StringOut],
        member_definition: Union[List[MemberDefinition], core.ArrayOut[MemberDefinition]],
        workforce_name: Union[str, core.StringOut],
        workteam_name: Union[str, core.StringOut],
        notification_configuration: Optional[NotificationConfiguration] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workteam.Args(
                description=description,
                member_definition=member_definition,
                workforce_name=workforce_name,
                workteam_name=workteam_name,
                notification_configuration=notification_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Union[str, core.StringOut] = core.arg()

        member_definition: Union[
            List[MemberDefinition], core.ArrayOut[MemberDefinition]
        ] = core.arg()

        notification_configuration: Optional[NotificationConfiguration] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        workforce_name: Union[str, core.StringOut] = core.arg()

        workteam_name: Union[str, core.StringOut] = core.arg()
