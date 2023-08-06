from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EncryptionOptions(core.Schema):

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    use_aws_owned_key: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        use_aws_owned_key: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=EncryptionOptions.Args(
                kms_key_id=kms_key_id,
                use_aws_owned_key=use_aws_owned_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        use_aws_owned_key: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class Configuration(core.Schema):

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    revision: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        *,
        id: Optional[Union[str, core.StringOut]] = None,
        revision: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Configuration.Args(
                id=id,
                revision=revision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        revision: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class LdapServerMetadata(core.Schema):

    hosts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    role_base: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_search_matching: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_search_subtree: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    service_account_password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    service_account_username: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_base: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_role_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_search_matching: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_search_subtree: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        hosts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        role_base: Optional[Union[str, core.StringOut]] = None,
        role_name: Optional[Union[str, core.StringOut]] = None,
        role_search_matching: Optional[Union[str, core.StringOut]] = None,
        role_search_subtree: Optional[Union[bool, core.BoolOut]] = None,
        service_account_password: Optional[Union[str, core.StringOut]] = None,
        service_account_username: Optional[Union[str, core.StringOut]] = None,
        user_base: Optional[Union[str, core.StringOut]] = None,
        user_role_name: Optional[Union[str, core.StringOut]] = None,
        user_search_matching: Optional[Union[str, core.StringOut]] = None,
        user_search_subtree: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=LdapServerMetadata.Args(
                hosts=hosts,
                role_base=role_base,
                role_name=role_name,
                role_search_matching=role_search_matching,
                role_search_subtree=role_search_subtree,
                service_account_password=service_account_password,
                service_account_username=service_account_username,
                user_base=user_base,
                user_role_name=user_role_name,
                user_search_matching=user_search_matching,
                user_search_subtree=user_search_subtree,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hosts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        role_base: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_search_matching: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_search_subtree: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        service_account_password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_account_username: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_base: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_role_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_search_matching: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_search_subtree: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class Logs(core.Schema):

    audit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    general: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        audit: Optional[Union[str, core.StringOut]] = None,
        general: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Logs.Args(
                audit=audit,
                general=general,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        audit: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        general: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class User(core.Schema):

    console_access: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    password: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
        console_access: Optional[Union[bool, core.BoolOut]] = None,
        groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=User.Args(
                password=password,
                username=username,
                console_access=console_access,
                groups=groups,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        console_access: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        password: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class MaintenanceWindowStartTime(core.Schema):

    day_of_week: Union[str, core.StringOut] = core.attr(str)

    time_of_day: Union[str, core.StringOut] = core.attr(str)

    time_zone: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        day_of_week: Union[str, core.StringOut],
        time_of_day: Union[str, core.StringOut],
        time_zone: Union[str, core.StringOut],
    ):
        super().__init__(
            args=MaintenanceWindowStartTime.Args(
                day_of_week=day_of_week,
                time_of_day=time_of_day,
                time_zone=time_zone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        day_of_week: Union[str, core.StringOut] = core.arg()

        time_of_day: Union[str, core.StringOut] = core.arg()

        time_zone: Union[str, core.StringOut] = core.arg()


@core.schema
class Instances(core.Schema):

    console_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoints: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        console_url: Union[str, core.StringOut],
        endpoints: Union[List[str], core.ArrayOut[core.StringOut]],
        ip_address: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Instances.Args(
                console_url=console_url,
                endpoints=endpoints,
                ip_address=ip_address,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        console_url: Union[str, core.StringOut] = core.arg()

        endpoints: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        ip_address: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_mq_broker", namespace="aws_mq")
class Broker(core.Resource):

    apply_immediately: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authentication_strategy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    broker_name: Union[str, core.StringOut] = core.attr(str)

    configuration: Optional[Configuration] = core.attr(Configuration, default=None, computed=True)

    deployment_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encryption_options: Optional[EncryptionOptions] = core.attr(EncryptionOptions, default=None)

    engine_type: Union[str, core.StringOut] = core.attr(str)

    engine_version: Union[str, core.StringOut] = core.attr(str)

    host_instance_type: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instances: Union[List[Instances], core.ArrayOut[Instances]] = core.attr(
        Instances, computed=True, kind=core.Kind.array
    )

    ldap_server_metadata: Optional[LdapServerMetadata] = core.attr(LdapServerMetadata, default=None)

    logs: Optional[Logs] = core.attr(Logs, default=None)

    maintenance_window_start_time: Optional[MaintenanceWindowStartTime] = core.attr(
        MaintenanceWindowStartTime, default=None, computed=True
    )

    publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    storage_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user: Union[List[User], core.ArrayOut[User]] = core.attr(User, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        broker_name: Union[str, core.StringOut],
        engine_type: Union[str, core.StringOut],
        engine_version: Union[str, core.StringOut],
        host_instance_type: Union[str, core.StringOut],
        user: Union[List[User], core.ArrayOut[User]],
        apply_immediately: Optional[Union[bool, core.BoolOut]] = None,
        authentication_strategy: Optional[Union[str, core.StringOut]] = None,
        auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = None,
        configuration: Optional[Configuration] = None,
        deployment_mode: Optional[Union[str, core.StringOut]] = None,
        encryption_options: Optional[EncryptionOptions] = None,
        ldap_server_metadata: Optional[LdapServerMetadata] = None,
        logs: Optional[Logs] = None,
        maintenance_window_start_time: Optional[MaintenanceWindowStartTime] = None,
        publicly_accessible: Optional[Union[bool, core.BoolOut]] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        storage_type: Optional[Union[str, core.StringOut]] = None,
        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Broker.Args(
                broker_name=broker_name,
                engine_type=engine_type,
                engine_version=engine_version,
                host_instance_type=host_instance_type,
                user=user,
                apply_immediately=apply_immediately,
                authentication_strategy=authentication_strategy,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                configuration=configuration,
                deployment_mode=deployment_mode,
                encryption_options=encryption_options,
                ldap_server_metadata=ldap_server_metadata,
                logs=logs,
                maintenance_window_start_time=maintenance_window_start_time,
                publicly_accessible=publicly_accessible,
                security_groups=security_groups,
                storage_type=storage_type,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        apply_immediately: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        authentication_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        broker_name: Union[str, core.StringOut] = core.arg()

        configuration: Optional[Configuration] = core.arg(default=None)

        deployment_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encryption_options: Optional[EncryptionOptions] = core.arg(default=None)

        engine_type: Union[str, core.StringOut] = core.arg()

        engine_version: Union[str, core.StringOut] = core.arg()

        host_instance_type: Union[str, core.StringOut] = core.arg()

        ldap_server_metadata: Optional[LdapServerMetadata] = core.arg(default=None)

        logs: Optional[Logs] = core.arg(default=None)

        maintenance_window_start_time: Optional[MaintenanceWindowStartTime] = core.arg(default=None)

        publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        storage_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user: Union[List[User], core.ArrayOut[User]] = core.arg()
