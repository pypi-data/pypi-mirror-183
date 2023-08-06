from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EbsVolume(core.Schema):

    encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    mount_point: Union[str, core.StringOut] = core.attr(str)

    number_of_disks: Union[int, core.IntOut] = core.attr(int)

    raid_level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    size: Union[int, core.IntOut] = core.attr(int)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        mount_point: Union[str, core.StringOut],
        number_of_disks: Union[int, core.IntOut],
        size: Union[int, core.IntOut],
        encrypted: Optional[Union[bool, core.BoolOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        raid_level: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EbsVolume.Args(
                mount_point=mount_point,
                number_of_disks=number_of_disks,
                size=size,
                encrypted=encrypted,
                iops=iops,
                raid_level=raid_level,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        mount_point: Union[str, core.StringOut] = core.arg()

        number_of_disks: Union[int, core.IntOut] = core.arg()

        raid_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        size: Union[int, core.IntOut] = core.arg()

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class LogStreams(core.Schema):

    batch_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    batch_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    buffer_duration: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    datetime_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encoding: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    file: Union[str, core.StringOut] = core.attr(str)

    file_fingerprint_lines: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    initial_position: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    log_group_name: Union[str, core.StringOut] = core.attr(str)

    multiline_start_pattern: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    time_zone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        file: Union[str, core.StringOut],
        log_group_name: Union[str, core.StringOut],
        batch_count: Optional[Union[int, core.IntOut]] = None,
        batch_size: Optional[Union[int, core.IntOut]] = None,
        buffer_duration: Optional[Union[int, core.IntOut]] = None,
        datetime_format: Optional[Union[str, core.StringOut]] = None,
        encoding: Optional[Union[str, core.StringOut]] = None,
        file_fingerprint_lines: Optional[Union[str, core.StringOut]] = None,
        initial_position: Optional[Union[str, core.StringOut]] = None,
        multiline_start_pattern: Optional[Union[str, core.StringOut]] = None,
        time_zone: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LogStreams.Args(
                file=file,
                log_group_name=log_group_name,
                batch_count=batch_count,
                batch_size=batch_size,
                buffer_duration=buffer_duration,
                datetime_format=datetime_format,
                encoding=encoding,
                file_fingerprint_lines=file_fingerprint_lines,
                initial_position=initial_position,
                multiline_start_pattern=multiline_start_pattern,
                time_zone=time_zone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        batch_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        batch_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        buffer_duration: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        datetime_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encoding: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        file: Union[str, core.StringOut] = core.arg()

        file_fingerprint_lines: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        initial_position: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_group_name: Union[str, core.StringOut] = core.arg()

        multiline_start_pattern: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        time_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CloudwatchConfiguration(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    log_streams: Optional[Union[List[LogStreams], core.ArrayOut[LogStreams]]] = core.attr(
        LogStreams, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        log_streams: Optional[Union[List[LogStreams], core.ArrayOut[LogStreams]]] = None,
    ):
        super().__init__(
            args=CloudwatchConfiguration.Args(
                enabled=enabled,
                log_streams=log_streams,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        log_streams: Optional[Union[List[LogStreams], core.ArrayOut[LogStreams]]] = core.arg(
            default=None
        )


@core.resource(type="aws_opsworks_memcached_layer", namespace="aws_opsworks")
class MemcachedLayer(core.Resource):

    allocated_memory: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_assign_elastic_ips: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    auto_assign_public_ips: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    auto_healing: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    cloudwatch_configuration: Optional[CloudwatchConfiguration] = core.attr(
        CloudwatchConfiguration, default=None
    )

    custom_configure_recipes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    custom_deploy_recipes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    custom_instance_profile_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    custom_json: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    custom_security_group_ids: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    custom_setup_recipes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    custom_shutdown_recipes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    custom_undeploy_recipes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    drain_elb_on_shutdown: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ebs_volume: Optional[Union[List[EbsVolume], core.ArrayOut[EbsVolume]]] = core.attr(
        EbsVolume, default=None, computed=True, kind=core.Kind.array
    )

    elastic_load_balancer: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    install_updates_on_boot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    instance_shutdown_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    stack_id: Union[str, core.StringOut] = core.attr(str)

    system_packages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    use_ebs_optimized_instances: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        stack_id: Union[str, core.StringOut],
        allocated_memory: Optional[Union[int, core.IntOut]] = None,
        auto_assign_elastic_ips: Optional[Union[bool, core.BoolOut]] = None,
        auto_assign_public_ips: Optional[Union[bool, core.BoolOut]] = None,
        auto_healing: Optional[Union[bool, core.BoolOut]] = None,
        cloudwatch_configuration: Optional[CloudwatchConfiguration] = None,
        custom_configure_recipes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        custom_deploy_recipes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        custom_instance_profile_arn: Optional[Union[str, core.StringOut]] = None,
        custom_json: Optional[Union[str, core.StringOut]] = None,
        custom_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        custom_setup_recipes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        custom_shutdown_recipes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        custom_undeploy_recipes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        drain_elb_on_shutdown: Optional[Union[bool, core.BoolOut]] = None,
        ebs_volume: Optional[Union[List[EbsVolume], core.ArrayOut[EbsVolume]]] = None,
        elastic_load_balancer: Optional[Union[str, core.StringOut]] = None,
        install_updates_on_boot: Optional[Union[bool, core.BoolOut]] = None,
        instance_shutdown_timeout: Optional[Union[int, core.IntOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        system_packages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        use_ebs_optimized_instances: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MemcachedLayer.Args(
                stack_id=stack_id,
                allocated_memory=allocated_memory,
                auto_assign_elastic_ips=auto_assign_elastic_ips,
                auto_assign_public_ips=auto_assign_public_ips,
                auto_healing=auto_healing,
                cloudwatch_configuration=cloudwatch_configuration,
                custom_configure_recipes=custom_configure_recipes,
                custom_deploy_recipes=custom_deploy_recipes,
                custom_instance_profile_arn=custom_instance_profile_arn,
                custom_json=custom_json,
                custom_security_group_ids=custom_security_group_ids,
                custom_setup_recipes=custom_setup_recipes,
                custom_shutdown_recipes=custom_shutdown_recipes,
                custom_undeploy_recipes=custom_undeploy_recipes,
                drain_elb_on_shutdown=drain_elb_on_shutdown,
                ebs_volume=ebs_volume,
                elastic_load_balancer=elastic_load_balancer,
                install_updates_on_boot=install_updates_on_boot,
                instance_shutdown_timeout=instance_shutdown_timeout,
                name=name,
                system_packages=system_packages,
                tags=tags,
                tags_all=tags_all,
                use_ebs_optimized_instances=use_ebs_optimized_instances,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allocated_memory: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        auto_assign_elastic_ips: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        auto_assign_public_ips: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        auto_healing: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        cloudwatch_configuration: Optional[CloudwatchConfiguration] = core.arg(default=None)

        custom_configure_recipes: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        custom_deploy_recipes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        custom_instance_profile_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        custom_json: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        custom_security_group_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        custom_setup_recipes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        custom_shutdown_recipes: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        custom_undeploy_recipes: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        drain_elb_on_shutdown: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ebs_volume: Optional[Union[List[EbsVolume], core.ArrayOut[EbsVolume]]] = core.arg(
            default=None
        )

        elastic_load_balancer: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        install_updates_on_boot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        instance_shutdown_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        stack_id: Union[str, core.StringOut] = core.arg()

        system_packages: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        use_ebs_optimized_instances: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
