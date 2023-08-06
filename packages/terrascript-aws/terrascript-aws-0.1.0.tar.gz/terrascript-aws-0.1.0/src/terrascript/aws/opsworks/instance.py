from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class EphemeralBlockDevice(core.Schema):

    device_name: Union[str, core.StringOut] = core.attr(str)

    virtual_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        virtual_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EphemeralBlockDevice.Args(
                device_name=device_name,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: Union[str, core.StringOut] = core.arg()

        virtual_name: Union[str, core.StringOut] = core.arg()


@core.schema
class RootBlockDevice(core.Schema):

    delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        volume_size: Optional[Union[int, core.IntOut]] = None,
        volume_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RootBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                iops=iops,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    device_name: Union[str, core.StringOut] = core.attr(str)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    snapshot_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        snapshot_id: Optional[Union[str, core.StringOut]] = None,
        volume_size: Optional[Union[int, core.IntOut]] = None,
        volume_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EbsBlockDevice.Args(
                device_name=device_name,
                delete_on_termination=delete_on_termination,
                iops=iops,
                snapshot_id=snapshot_id,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        device_name: Union[str, core.StringOut] = core.arg()

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        snapshot_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_opsworks_instance", namespace="aws_opsworks")
class Instance(core.Resource):

    agent_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ami_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    architecture: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    auto_scaling_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    created_at: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    delete_ebs: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    delete_eip: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ebs_block_device: Optional[
        Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
    ] = core.attr(EbsBlockDevice, default=None, computed=True, kind=core.Kind.array)

    ebs_optimized: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ec2_instance_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ecs_cluster_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    elastic_ip: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    ephemeral_block_device: Optional[
        Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
    ] = core.attr(EphemeralBlockDevice, default=None, computed=True, kind=core.Kind.array)

    hostname: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    infrastructure_class: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    install_updates_on_boot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    instance_profile_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    instance_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    last_service_error_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    layer_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    os: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    platform: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_dns: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_dns: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    registered_by: Union[str, core.StringOut] = core.attr(str, computed=True)

    reported_agent_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    reported_os_family: Union[str, core.StringOut] = core.attr(str, computed=True)

    reported_os_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    reported_os_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_block_device: Optional[
        Union[List[RootBlockDevice], core.ArrayOut[RootBlockDevice]]
    ] = core.attr(RootBlockDevice, default=None, computed=True, kind=core.Kind.array)

    root_device_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    root_device_volume_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    ssh_host_dsa_key_fingerprint: Union[str, core.StringOut] = core.attr(str, computed=True)

    ssh_host_rsa_key_fingerprint: Union[str, core.StringOut] = core.attr(str, computed=True)

    ssh_key_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    stack_id: Union[str, core.StringOut] = core.attr(str)

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tenancy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    virtualization_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        layer_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        stack_id: Union[str, core.StringOut],
        agent_version: Optional[Union[str, core.StringOut]] = None,
        ami_id: Optional[Union[str, core.StringOut]] = None,
        architecture: Optional[Union[str, core.StringOut]] = None,
        auto_scaling_type: Optional[Union[str, core.StringOut]] = None,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        created_at: Optional[Union[str, core.StringOut]] = None,
        delete_ebs: Optional[Union[bool, core.BoolOut]] = None,
        delete_eip: Optional[Union[bool, core.BoolOut]] = None,
        ebs_block_device: Optional[
            Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
        ] = None,
        ebs_optimized: Optional[Union[bool, core.BoolOut]] = None,
        ecs_cluster_arn: Optional[Union[str, core.StringOut]] = None,
        elastic_ip: Optional[Union[str, core.StringOut]] = None,
        ephemeral_block_device: Optional[
            Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
        ] = None,
        hostname: Optional[Union[str, core.StringOut]] = None,
        infrastructure_class: Optional[Union[str, core.StringOut]] = None,
        install_updates_on_boot: Optional[Union[bool, core.BoolOut]] = None,
        instance_profile_arn: Optional[Union[str, core.StringOut]] = None,
        instance_type: Optional[Union[str, core.StringOut]] = None,
        os: Optional[Union[str, core.StringOut]] = None,
        root_block_device: Optional[
            Union[List[RootBlockDevice], core.ArrayOut[RootBlockDevice]]
        ] = None,
        root_device_type: Optional[Union[str, core.StringOut]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        ssh_key_name: Optional[Union[str, core.StringOut]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
        status: Optional[Union[str, core.StringOut]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        tenancy: Optional[Union[str, core.StringOut]] = None,
        virtualization_type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Instance.Args(
                layer_ids=layer_ids,
                stack_id=stack_id,
                agent_version=agent_version,
                ami_id=ami_id,
                architecture=architecture,
                auto_scaling_type=auto_scaling_type,
                availability_zone=availability_zone,
                created_at=created_at,
                delete_ebs=delete_ebs,
                delete_eip=delete_eip,
                ebs_block_device=ebs_block_device,
                ebs_optimized=ebs_optimized,
                ecs_cluster_arn=ecs_cluster_arn,
                elastic_ip=elastic_ip,
                ephemeral_block_device=ephemeral_block_device,
                hostname=hostname,
                infrastructure_class=infrastructure_class,
                install_updates_on_boot=install_updates_on_boot,
                instance_profile_arn=instance_profile_arn,
                instance_type=instance_type,
                os=os,
                root_block_device=root_block_device,
                root_device_type=root_device_type,
                security_group_ids=security_group_ids,
                ssh_key_name=ssh_key_name,
                state=state,
                status=status,
                subnet_id=subnet_id,
                tenancy=tenancy,
                virtualization_type=virtualization_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        agent_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ami_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        architecture: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        auto_scaling_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        created_at: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        delete_ebs: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        delete_eip: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ebs_block_device: Optional[
            Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
        ] = core.arg(default=None)

        ebs_optimized: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ecs_cluster_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elastic_ip: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ephemeral_block_device: Optional[
            Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
        ] = core.arg(default=None)

        hostname: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        infrastructure_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        install_updates_on_boot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        instance_profile_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        layer_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        os: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        root_block_device: Optional[
            Union[List[RootBlockDevice], core.ArrayOut[RootBlockDevice]]
        ] = core.arg(default=None)

        root_device_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        ssh_key_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        stack_id: Union[str, core.StringOut] = core.arg()

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tenancy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        virtualization_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
