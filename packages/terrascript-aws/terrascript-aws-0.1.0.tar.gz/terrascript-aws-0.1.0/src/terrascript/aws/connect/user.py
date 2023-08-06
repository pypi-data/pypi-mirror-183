from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class PhoneConfig(core.Schema):

    after_contact_work_time_limit: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    auto_accept: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    desk_phone_number: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    phone_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        phone_type: Union[str, core.StringOut],
        after_contact_work_time_limit: Optional[Union[int, core.IntOut]] = None,
        auto_accept: Optional[Union[bool, core.BoolOut]] = None,
        desk_phone_number: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=PhoneConfig.Args(
                phone_type=phone_type,
                after_contact_work_time_limit=after_contact_work_time_limit,
                auto_accept=auto_accept,
                desk_phone_number=desk_phone_number,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        after_contact_work_time_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        auto_accept: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        desk_phone_number: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        phone_type: Union[str, core.StringOut] = core.arg()


@core.schema
class IdentityInfo(core.Schema):

    email: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    first_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    last_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        email: Optional[Union[str, core.StringOut]] = None,
        first_name: Optional[Union[str, core.StringOut]] = None,
        last_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=IdentityInfo.Args(
                email=email,
                first_name=first_name,
                last_name=last_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        email: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        first_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        last_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_connect_user", namespace="aws_connect")
class User(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    directory_user_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    hierarchy_group_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity_info: Optional[IdentityInfo] = core.attr(IdentityInfo, default=None)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    phone_config: PhoneConfig = core.attr(PhoneConfig)

    routing_profile_id: Union[str, core.StringOut] = core.attr(str)

    security_profile_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        phone_config: PhoneConfig,
        routing_profile_id: Union[str, core.StringOut],
        security_profile_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        directory_user_id: Optional[Union[str, core.StringOut]] = None,
        hierarchy_group_id: Optional[Union[str, core.StringOut]] = None,
        identity_info: Optional[IdentityInfo] = None,
        password: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                instance_id=instance_id,
                name=name,
                phone_config=phone_config,
                routing_profile_id=routing_profile_id,
                security_profile_ids=security_profile_ids,
                directory_user_id=directory_user_id,
                hierarchy_group_id=hierarchy_group_id,
                identity_info=identity_info,
                password=password,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        directory_user_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        hierarchy_group_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identity_info: Optional[IdentityInfo] = core.arg(default=None)

        instance_id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        phone_config: PhoneConfig = core.arg()

        routing_profile_id: Union[str, core.StringOut] = core.arg()

        security_profile_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
