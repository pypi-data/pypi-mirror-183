from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class User(core.Schema):

    console_access: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        console_access: Union[bool, core.BoolOut],
        groups: Union[List[str], core.ArrayOut[core.StringOut]],
        username: Union[str, core.StringOut],
    ):
        super().__init__(
            args=User.Args(
                console_access=console_access,
                groups=groups,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        console_access: Union[bool, core.BoolOut] = core.arg()

        groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class EncryptionOptions(core.Schema):

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    use_aws_owned_key: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        kms_key_id: Union[str, core.StringOut],
        use_aws_owned_key: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=EncryptionOptions.Args(
                kms_key_id=kms_key_id,
                use_aws_owned_key=use_aws_owned_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: Union[str, core.StringOut] = core.arg()

        use_aws_owned_key: Union[bool, core.BoolOut] = core.arg()


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


@core.schema
class MaintenanceWindowStartTime(core.Schema):

    day_of_week: Union[str, core.StringOut] = core.attr(str, computed=True)

    time_of_day: Union[str, core.StringOut] = core.attr(str, computed=True)

    time_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

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
class Configuration(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    revision: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        revision: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Configuration.Args(
                id=id,
                revision=revision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        revision: Union[int, core.IntOut] = core.arg()


@core.schema
class LdapServerMetadata(core.Schema):

    hosts: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    role_base: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_search_matching: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_search_subtree: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    service_account_password: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_account_username: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_base: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_role_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_search_matching: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_search_subtree: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        hosts: Union[List[str], core.ArrayOut[core.StringOut]],
        role_base: Union[str, core.StringOut],
        role_name: Union[str, core.StringOut],
        role_search_matching: Union[str, core.StringOut],
        role_search_subtree: Union[bool, core.BoolOut],
        service_account_password: Union[str, core.StringOut],
        service_account_username: Union[str, core.StringOut],
        user_base: Union[str, core.StringOut],
        user_role_name: Union[str, core.StringOut],
        user_search_matching: Union[str, core.StringOut],
        user_search_subtree: Union[bool, core.BoolOut],
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
        hosts: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        role_base: Union[str, core.StringOut] = core.arg()

        role_name: Union[str, core.StringOut] = core.arg()

        role_search_matching: Union[str, core.StringOut] = core.arg()

        role_search_subtree: Union[bool, core.BoolOut] = core.arg()

        service_account_password: Union[str, core.StringOut] = core.arg()

        service_account_username: Union[str, core.StringOut] = core.arg()

        user_base: Union[str, core.StringOut] = core.arg()

        user_role_name: Union[str, core.StringOut] = core.arg()

        user_search_matching: Union[str, core.StringOut] = core.arg()

        user_search_subtree: Union[bool, core.BoolOut] = core.arg()


@core.schema
class Logs(core.Schema):

    audit: Union[str, core.StringOut] = core.attr(str, computed=True)

    general: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        audit: Union[str, core.StringOut],
        general: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=Logs.Args(
                audit=audit,
                general=general,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        audit: Union[str, core.StringOut] = core.arg()

        general: Union[bool, core.BoolOut] = core.arg()


@core.data(type="aws_mq_broker", namespace="aws_mq")
class DsBroker(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authentication_strategy: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_minor_version_upgrade: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    broker_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    broker_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    configuration: Union[List[Configuration], core.ArrayOut[Configuration]] = core.attr(
        Configuration, computed=True, kind=core.Kind.array
    )

    deployment_mode: Union[str, core.StringOut] = core.attr(str, computed=True)

    encryption_options: Union[
        List[EncryptionOptions], core.ArrayOut[EncryptionOptions]
    ] = core.attr(EncryptionOptions, computed=True, kind=core.Kind.array)

    engine_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    host_instance_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instances: Union[List[Instances], core.ArrayOut[Instances]] = core.attr(
        Instances, computed=True, kind=core.Kind.array
    )

    ldap_server_metadata: Union[
        List[LdapServerMetadata], core.ArrayOut[LdapServerMetadata]
    ] = core.attr(LdapServerMetadata, computed=True, kind=core.Kind.array)

    logs: Union[List[Logs], core.ArrayOut[Logs]] = core.attr(
        Logs, computed=True, kind=core.Kind.array
    )

    maintenance_window_start_time: Union[
        List[MaintenanceWindowStartTime], core.ArrayOut[MaintenanceWindowStartTime]
    ] = core.attr(MaintenanceWindowStartTime, computed=True, kind=core.Kind.array)

    publicly_accessible: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    storage_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user: Union[List[User], core.ArrayOut[User]] = core.attr(
        User, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        broker_id: Optional[Union[str, core.StringOut]] = None,
        broker_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsBroker.Args(
                broker_id=broker_id,
                broker_name=broker_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        broker_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        broker_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
