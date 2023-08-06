from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CustomCookbooksSource(core.Schema):

    password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    revision: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssh_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    url: Union[str, core.StringOut] = core.attr(str)

    username: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        url: Union[str, core.StringOut],
        password: Optional[Union[str, core.StringOut]] = None,
        revision: Optional[Union[str, core.StringOut]] = None,
        ssh_key: Optional[Union[str, core.StringOut]] = None,
        username: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CustomCookbooksSource.Args(
                type=type,
                url=url,
                password=password,
                revision=revision,
                ssh_key=ssh_key,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        revision: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssh_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()

        url: Union[str, core.StringOut] = core.arg()

        username: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_opsworks_stack", namespace="aws_opsworks")
class Stack(core.Resource):

    agent_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    berkshelf_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    color: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    configuration_manager_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    configuration_manager_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    custom_cookbooks_source: Optional[CustomCookbooksSource] = core.attr(
        CustomCookbooksSource, default=None, computed=True
    )

    custom_json: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    default_availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    default_instance_profile_arn: Union[str, core.StringOut] = core.attr(str)

    default_os: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    default_root_device_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    default_ssh_key_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    default_subnet_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    hostname_theme: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    manage_berkshelf: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    region: Union[str, core.StringOut] = core.attr(str)

    service_role_arn: Union[str, core.StringOut] = core.attr(str)

    stack_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    use_custom_cookbooks: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    use_opsworks_security_groups: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    vpc_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        default_instance_profile_arn: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        region: Union[str, core.StringOut],
        service_role_arn: Union[str, core.StringOut],
        agent_version: Optional[Union[str, core.StringOut]] = None,
        berkshelf_version: Optional[Union[str, core.StringOut]] = None,
        color: Optional[Union[str, core.StringOut]] = None,
        configuration_manager_name: Optional[Union[str, core.StringOut]] = None,
        configuration_manager_version: Optional[Union[str, core.StringOut]] = None,
        custom_cookbooks_source: Optional[CustomCookbooksSource] = None,
        custom_json: Optional[Union[str, core.StringOut]] = None,
        default_availability_zone: Optional[Union[str, core.StringOut]] = None,
        default_os: Optional[Union[str, core.StringOut]] = None,
        default_root_device_type: Optional[Union[str, core.StringOut]] = None,
        default_ssh_key_name: Optional[Union[str, core.StringOut]] = None,
        default_subnet_id: Optional[Union[str, core.StringOut]] = None,
        hostname_theme: Optional[Union[str, core.StringOut]] = None,
        manage_berkshelf: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        use_custom_cookbooks: Optional[Union[bool, core.BoolOut]] = None,
        use_opsworks_security_groups: Optional[Union[bool, core.BoolOut]] = None,
        vpc_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stack.Args(
                default_instance_profile_arn=default_instance_profile_arn,
                name=name,
                region=region,
                service_role_arn=service_role_arn,
                agent_version=agent_version,
                berkshelf_version=berkshelf_version,
                color=color,
                configuration_manager_name=configuration_manager_name,
                configuration_manager_version=configuration_manager_version,
                custom_cookbooks_source=custom_cookbooks_source,
                custom_json=custom_json,
                default_availability_zone=default_availability_zone,
                default_os=default_os,
                default_root_device_type=default_root_device_type,
                default_ssh_key_name=default_ssh_key_name,
                default_subnet_id=default_subnet_id,
                hostname_theme=hostname_theme,
                manage_berkshelf=manage_berkshelf,
                tags=tags,
                tags_all=tags_all,
                use_custom_cookbooks=use_custom_cookbooks,
                use_opsworks_security_groups=use_opsworks_security_groups,
                vpc_id=vpc_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        agent_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        berkshelf_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        color: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        configuration_manager_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        configuration_manager_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        custom_cookbooks_source: Optional[CustomCookbooksSource] = core.arg(default=None)

        custom_json: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_instance_profile_arn: Union[str, core.StringOut] = core.arg()

        default_os: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_root_device_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_ssh_key_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        hostname_theme: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        manage_berkshelf: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        region: Union[str, core.StringOut] = core.arg()

        service_role_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        use_custom_cookbooks: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        use_opsworks_security_groups: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        vpc_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
