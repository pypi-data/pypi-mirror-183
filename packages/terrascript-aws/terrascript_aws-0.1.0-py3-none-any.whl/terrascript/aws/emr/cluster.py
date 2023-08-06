from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Configurations(core.Schema):

    classification: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        classification: Optional[Union[str, core.StringOut]] = None,
        properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Configurations.Args(
                classification=classification,
                properties=properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        classification: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class InstanceTypeConfigsEbsConfig(core.Schema):

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    size: Union[int, core.IntOut] = core.attr(int)

    type: Union[str, core.StringOut] = core.attr(str)

    volumes_per_instance: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        size: Union[int, core.IntOut],
        type: Union[str, core.StringOut],
        iops: Optional[Union[int, core.IntOut]] = None,
        volumes_per_instance: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=InstanceTypeConfigsEbsConfig.Args(
                size=size,
                type=type,
                iops=iops,
                volumes_per_instance=volumes_per_instance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        size: Union[int, core.IntOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()

        volumes_per_instance: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class InstanceTypeConfigs(core.Schema):

    bid_price: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bid_price_as_percentage_of_on_demand_price: Optional[Union[float, core.FloatOut]] = core.attr(
        float, default=None
    )

    configurations: Optional[
        Union[List[Configurations], core.ArrayOut[Configurations]]
    ] = core.attr(Configurations, default=None, kind=core.Kind.array)

    ebs_config: Optional[
        Union[List[InstanceTypeConfigsEbsConfig], core.ArrayOut[InstanceTypeConfigsEbsConfig]]
    ] = core.attr(InstanceTypeConfigsEbsConfig, default=None, computed=True, kind=core.Kind.array)

    instance_type: Union[str, core.StringOut] = core.attr(str)

    weighted_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        instance_type: Union[str, core.StringOut],
        bid_price: Optional[Union[str, core.StringOut]] = None,
        bid_price_as_percentage_of_on_demand_price: Optional[Union[float, core.FloatOut]] = None,
        configurations: Optional[Union[List[Configurations], core.ArrayOut[Configurations]]] = None,
        ebs_config: Optional[
            Union[List[InstanceTypeConfigsEbsConfig], core.ArrayOut[InstanceTypeConfigsEbsConfig]]
        ] = None,
        weighted_capacity: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=InstanceTypeConfigs.Args(
                instance_type=instance_type,
                bid_price=bid_price,
                bid_price_as_percentage_of_on_demand_price=bid_price_as_percentage_of_on_demand_price,
                configurations=configurations,
                ebs_config=ebs_config,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bid_price: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bid_price_as_percentage_of_on_demand_price: Optional[
            Union[float, core.FloatOut]
        ] = core.arg(default=None)

        configurations: Optional[
            Union[List[Configurations], core.ArrayOut[Configurations]]
        ] = core.arg(default=None)

        ebs_config: Optional[
            Union[List[InstanceTypeConfigsEbsConfig], core.ArrayOut[InstanceTypeConfigsEbsConfig]]
        ] = core.arg(default=None)

        instance_type: Union[str, core.StringOut] = core.arg()

        weighted_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class OnDemandSpecification(core.Schema):

    allocation_strategy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        allocation_strategy: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OnDemandSpecification.Args(
                allocation_strategy=allocation_strategy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: Union[str, core.StringOut] = core.arg()


@core.schema
class SpotSpecification(core.Schema):

    allocation_strategy: Union[str, core.StringOut] = core.attr(str)

    block_duration_minutes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    timeout_action: Union[str, core.StringOut] = core.attr(str)

    timeout_duration_minutes: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        allocation_strategy: Union[str, core.StringOut],
        timeout_action: Union[str, core.StringOut],
        timeout_duration_minutes: Union[int, core.IntOut],
        block_duration_minutes: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=SpotSpecification.Args(
                allocation_strategy=allocation_strategy,
                timeout_action=timeout_action,
                timeout_duration_minutes=timeout_duration_minutes,
                block_duration_minutes=block_duration_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: Union[str, core.StringOut] = core.arg()

        block_duration_minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        timeout_action: Union[str, core.StringOut] = core.arg()

        timeout_duration_minutes: Union[int, core.IntOut] = core.arg()


@core.schema
class LaunchSpecifications(core.Schema):

    on_demand_specification: Optional[
        Union[List[OnDemandSpecification], core.ArrayOut[OnDemandSpecification]]
    ] = core.attr(OnDemandSpecification, default=None, kind=core.Kind.array)

    spot_specification: Optional[
        Union[List[SpotSpecification], core.ArrayOut[SpotSpecification]]
    ] = core.attr(SpotSpecification, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        on_demand_specification: Optional[
            Union[List[OnDemandSpecification], core.ArrayOut[OnDemandSpecification]]
        ] = None,
        spot_specification: Optional[
            Union[List[SpotSpecification], core.ArrayOut[SpotSpecification]]
        ] = None,
    ):
        super().__init__(
            args=LaunchSpecifications.Args(
                on_demand_specification=on_demand_specification,
                spot_specification=spot_specification,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        on_demand_specification: Optional[
            Union[List[OnDemandSpecification], core.ArrayOut[OnDemandSpecification]]
        ] = core.arg(default=None)

        spot_specification: Optional[
            Union[List[SpotSpecification], core.ArrayOut[SpotSpecification]]
        ] = core.arg(default=None)


@core.schema
class MasterInstanceFleet(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_type_configs: Optional[
        Union[List[InstanceTypeConfigs], core.ArrayOut[InstanceTypeConfigs]]
    ] = core.attr(InstanceTypeConfigs, default=None, kind=core.Kind.array)

    launch_specifications: Optional[LaunchSpecifications] = core.attr(
        LaunchSpecifications, default=None
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    provisioned_on_demand_capacity: Union[int, core.IntOut] = core.attr(int, computed=True)

    provisioned_spot_capacity: Union[int, core.IntOut] = core.attr(int, computed=True)

    target_on_demand_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    target_spot_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        provisioned_on_demand_capacity: Union[int, core.IntOut],
        provisioned_spot_capacity: Union[int, core.IntOut],
        instance_type_configs: Optional[
            Union[List[InstanceTypeConfigs], core.ArrayOut[InstanceTypeConfigs]]
        ] = None,
        launch_specifications: Optional[LaunchSpecifications] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        target_on_demand_capacity: Optional[Union[int, core.IntOut]] = None,
        target_spot_capacity: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=MasterInstanceFleet.Args(
                id=id,
                provisioned_on_demand_capacity=provisioned_on_demand_capacity,
                provisioned_spot_capacity=provisioned_spot_capacity,
                instance_type_configs=instance_type_configs,
                launch_specifications=launch_specifications,
                name=name,
                target_on_demand_capacity=target_on_demand_capacity,
                target_spot_capacity=target_spot_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        instance_type_configs: Optional[
            Union[List[InstanceTypeConfigs], core.ArrayOut[InstanceTypeConfigs]]
        ] = core.arg(default=None)

        launch_specifications: Optional[LaunchSpecifications] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        provisioned_on_demand_capacity: Union[int, core.IntOut] = core.arg()

        provisioned_spot_capacity: Union[int, core.IntOut] = core.arg()

        target_on_demand_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        target_spot_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class BootstrapAction(core.Schema):

    args: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    path: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        path: Union[str, core.StringOut],
        args: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=BootstrapAction.Args(
                name=name,
                path=path,
                args=args,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        args: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        path: Union[str, core.StringOut] = core.arg()


@core.schema
class AutoTerminationPolicy(core.Schema):

    idle_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        idle_timeout: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=AutoTerminationPolicy.Args(
                idle_timeout=idle_timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        idle_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class MasterInstanceGroupEbsConfig(core.Schema):

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    size: Union[int, core.IntOut] = core.attr(int)

    throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    volumes_per_instance: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        size: Union[int, core.IntOut],
        type: Union[str, core.StringOut],
        iops: Optional[Union[int, core.IntOut]] = None,
        throughput: Optional[Union[int, core.IntOut]] = None,
        volumes_per_instance: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=MasterInstanceGroupEbsConfig.Args(
                size=size,
                type=type,
                iops=iops,
                throughput=throughput,
                volumes_per_instance=volumes_per_instance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        size: Union[int, core.IntOut] = core.arg()

        throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()

        volumes_per_instance: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class MasterInstanceGroup(core.Schema):

    bid_price: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ebs_config: Optional[
        Union[List[MasterInstanceGroupEbsConfig], core.ArrayOut[MasterInstanceGroupEbsConfig]]
    ] = core.attr(MasterInstanceGroupEbsConfig, default=None, computed=True, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    instance_type: Union[str, core.StringOut] = core.attr(str)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        instance_type: Union[str, core.StringOut],
        bid_price: Optional[Union[str, core.StringOut]] = None,
        ebs_config: Optional[
            Union[List[MasterInstanceGroupEbsConfig], core.ArrayOut[MasterInstanceGroupEbsConfig]]
        ] = None,
        instance_count: Optional[Union[int, core.IntOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=MasterInstanceGroup.Args(
                id=id,
                instance_type=instance_type,
                bid_price=bid_price,
                ebs_config=ebs_config,
                instance_count=instance_count,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bid_price: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ebs_config: Optional[
            Union[List[MasterInstanceGroupEbsConfig], core.ArrayOut[MasterInstanceGroupEbsConfig]]
        ] = core.arg(default=None)

        id: Union[str, core.StringOut] = core.arg()

        instance_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        instance_type: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CoreInstanceFleet(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_type_configs: Optional[
        Union[List[InstanceTypeConfigs], core.ArrayOut[InstanceTypeConfigs]]
    ] = core.attr(InstanceTypeConfigs, default=None, kind=core.Kind.array)

    launch_specifications: Optional[LaunchSpecifications] = core.attr(
        LaunchSpecifications, default=None
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    provisioned_on_demand_capacity: Union[int, core.IntOut] = core.attr(int, computed=True)

    provisioned_spot_capacity: Union[int, core.IntOut] = core.attr(int, computed=True)

    target_on_demand_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    target_spot_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        provisioned_on_demand_capacity: Union[int, core.IntOut],
        provisioned_spot_capacity: Union[int, core.IntOut],
        instance_type_configs: Optional[
            Union[List[InstanceTypeConfigs], core.ArrayOut[InstanceTypeConfigs]]
        ] = None,
        launch_specifications: Optional[LaunchSpecifications] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        target_on_demand_capacity: Optional[Union[int, core.IntOut]] = None,
        target_spot_capacity: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CoreInstanceFleet.Args(
                id=id,
                provisioned_on_demand_capacity=provisioned_on_demand_capacity,
                provisioned_spot_capacity=provisioned_spot_capacity,
                instance_type_configs=instance_type_configs,
                launch_specifications=launch_specifications,
                name=name,
                target_on_demand_capacity=target_on_demand_capacity,
                target_spot_capacity=target_spot_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        instance_type_configs: Optional[
            Union[List[InstanceTypeConfigs], core.ArrayOut[InstanceTypeConfigs]]
        ] = core.arg(default=None)

        launch_specifications: Optional[LaunchSpecifications] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        provisioned_on_demand_capacity: Union[int, core.IntOut] = core.arg()

        provisioned_spot_capacity: Union[int, core.IntOut] = core.arg()

        target_on_demand_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        target_spot_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class HadoopJarStep(core.Schema):

    args: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    jar: Union[str, core.StringOut] = core.attr(str)

    main_class: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        jar: Union[str, core.StringOut],
        args: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        main_class: Optional[Union[str, core.StringOut]] = None,
        properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=HadoopJarStep.Args(
                jar=jar,
                args=args,
                main_class=main_class,
                properties=properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        args: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        jar: Union[str, core.StringOut] = core.arg()

        main_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class Step(core.Schema):

    action_on_failure: Union[str, core.StringOut] = core.attr(str)

    hadoop_jar_step: HadoopJarStep = core.attr(HadoopJarStep)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        action_on_failure: Union[str, core.StringOut],
        hadoop_jar_step: HadoopJarStep,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Step.Args(
                action_on_failure=action_on_failure,
                hadoop_jar_step=hadoop_jar_step,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_on_failure: Union[str, core.StringOut] = core.arg()

        hadoop_jar_step: HadoopJarStep = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class Ec2Attributes(core.Schema):

    additional_master_security_groups: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    additional_slave_security_groups: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    emr_managed_master_security_group: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    emr_managed_slave_security_group: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    instance_profile: Union[str, core.StringOut] = core.attr(str)

    key_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    service_access_security_group: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        instance_profile: Union[str, core.StringOut],
        additional_master_security_groups: Optional[Union[str, core.StringOut]] = None,
        additional_slave_security_groups: Optional[Union[str, core.StringOut]] = None,
        emr_managed_master_security_group: Optional[Union[str, core.StringOut]] = None,
        emr_managed_slave_security_group: Optional[Union[str, core.StringOut]] = None,
        key_name: Optional[Union[str, core.StringOut]] = None,
        service_access_security_group: Optional[Union[str, core.StringOut]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Ec2Attributes.Args(
                instance_profile=instance_profile,
                additional_master_security_groups=additional_master_security_groups,
                additional_slave_security_groups=additional_slave_security_groups,
                emr_managed_master_security_group=emr_managed_master_security_group,
                emr_managed_slave_security_group=emr_managed_slave_security_group,
                key_name=key_name,
                service_access_security_group=service_access_security_group,
                subnet_id=subnet_id,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        additional_master_security_groups: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        additional_slave_security_groups: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        emr_managed_master_security_group: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        emr_managed_slave_security_group: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        instance_profile: Union[str, core.StringOut] = core.arg()

        key_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_access_security_group: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class KerberosAttributes(core.Schema):

    ad_domain_join_password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ad_domain_join_user: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cross_realm_trust_principal_password: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    kdc_admin_password: Union[str, core.StringOut] = core.attr(str)

    realm: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        kdc_admin_password: Union[str, core.StringOut],
        realm: Union[str, core.StringOut],
        ad_domain_join_password: Optional[Union[str, core.StringOut]] = None,
        ad_domain_join_user: Optional[Union[str, core.StringOut]] = None,
        cross_realm_trust_principal_password: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=KerberosAttributes.Args(
                kdc_admin_password=kdc_admin_password,
                realm=realm,
                ad_domain_join_password=ad_domain_join_password,
                ad_domain_join_user=ad_domain_join_user,
                cross_realm_trust_principal_password=cross_realm_trust_principal_password,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ad_domain_join_password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ad_domain_join_user: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cross_realm_trust_principal_password: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        kdc_admin_password: Union[str, core.StringOut] = core.arg()

        realm: Union[str, core.StringOut] = core.arg()


@core.schema
class CoreInstanceGroup(core.Schema):

    autoscaling_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bid_price: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ebs_config: Optional[
        Union[List[MasterInstanceGroupEbsConfig], core.ArrayOut[MasterInstanceGroupEbsConfig]]
    ] = core.attr(MasterInstanceGroupEbsConfig, default=None, computed=True, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    instance_type: Union[str, core.StringOut] = core.attr(str)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        instance_type: Union[str, core.StringOut],
        autoscaling_policy: Optional[Union[str, core.StringOut]] = None,
        bid_price: Optional[Union[str, core.StringOut]] = None,
        ebs_config: Optional[
            Union[List[MasterInstanceGroupEbsConfig], core.ArrayOut[MasterInstanceGroupEbsConfig]]
        ] = None,
        instance_count: Optional[Union[int, core.IntOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CoreInstanceGroup.Args(
                id=id,
                instance_type=instance_type,
                autoscaling_policy=autoscaling_policy,
                bid_price=bid_price,
                ebs_config=ebs_config,
                instance_count=instance_count,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        autoscaling_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bid_price: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ebs_config: Optional[
            Union[List[MasterInstanceGroupEbsConfig], core.ArrayOut[MasterInstanceGroupEbsConfig]]
        ] = core.arg(default=None)

        id: Union[str, core.StringOut] = core.arg()

        instance_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        instance_type: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_emr_cluster", namespace="aws_emr")
class Cluster(core.Resource):

    additional_info: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    applications: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_termination_policy: Optional[AutoTerminationPolicy] = core.attr(
        AutoTerminationPolicy, default=None
    )

    autoscaling_role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bootstrap_action: Optional[
        Union[List[BootstrapAction], core.ArrayOut[BootstrapAction]]
    ] = core.attr(BootstrapAction, default=None, kind=core.Kind.array)

    cluster_state: Union[str, core.StringOut] = core.attr(str, computed=True)

    configurations: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    configurations_json: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    core_instance_fleet: Optional[CoreInstanceFleet] = core.attr(
        CoreInstanceFleet, default=None, computed=True
    )

    core_instance_group: Optional[CoreInstanceGroup] = core.attr(
        CoreInstanceGroup, default=None, computed=True
    )

    custom_ami_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ebs_root_volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    ec2_attributes: Optional[Ec2Attributes] = core.attr(Ec2Attributes, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    keep_job_flow_alive_when_no_steps: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    kerberos_attributes: Optional[KerberosAttributes] = core.attr(KerberosAttributes, default=None)

    list_steps_states: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    log_encryption_kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    log_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    master_instance_fleet: Optional[MasterInstanceFleet] = core.attr(
        MasterInstanceFleet, default=None, computed=True
    )

    master_instance_group: Optional[MasterInstanceGroup] = core.attr(
        MasterInstanceGroup, default=None, computed=True
    )

    master_public_dns: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    release_label: Union[str, core.StringOut] = core.attr(str)

    scale_down_behavior: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    security_configuration: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    service_role: Union[str, core.StringOut] = core.attr(str)

    step: Optional[Union[List[Step], core.ArrayOut[Step]]] = core.attr(
        Step, default=None, computed=True, kind=core.Kind.array
    )

    step_concurrency_level: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    termination_protection: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    visible_to_all_users: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        release_label: Union[str, core.StringOut],
        service_role: Union[str, core.StringOut],
        additional_info: Optional[Union[str, core.StringOut]] = None,
        applications: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        auto_termination_policy: Optional[AutoTerminationPolicy] = None,
        autoscaling_role: Optional[Union[str, core.StringOut]] = None,
        bootstrap_action: Optional[
            Union[List[BootstrapAction], core.ArrayOut[BootstrapAction]]
        ] = None,
        configurations: Optional[Union[str, core.StringOut]] = None,
        configurations_json: Optional[Union[str, core.StringOut]] = None,
        core_instance_fleet: Optional[CoreInstanceFleet] = None,
        core_instance_group: Optional[CoreInstanceGroup] = None,
        custom_ami_id: Optional[Union[str, core.StringOut]] = None,
        ebs_root_volume_size: Optional[Union[int, core.IntOut]] = None,
        ec2_attributes: Optional[Ec2Attributes] = None,
        keep_job_flow_alive_when_no_steps: Optional[Union[bool, core.BoolOut]] = None,
        kerberos_attributes: Optional[KerberosAttributes] = None,
        list_steps_states: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        log_encryption_kms_key_id: Optional[Union[str, core.StringOut]] = None,
        log_uri: Optional[Union[str, core.StringOut]] = None,
        master_instance_fleet: Optional[MasterInstanceFleet] = None,
        master_instance_group: Optional[MasterInstanceGroup] = None,
        scale_down_behavior: Optional[Union[str, core.StringOut]] = None,
        security_configuration: Optional[Union[str, core.StringOut]] = None,
        step: Optional[Union[List[Step], core.ArrayOut[Step]]] = None,
        step_concurrency_level: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        termination_protection: Optional[Union[bool, core.BoolOut]] = None,
        visible_to_all_users: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                name=name,
                release_label=release_label,
                service_role=service_role,
                additional_info=additional_info,
                applications=applications,
                auto_termination_policy=auto_termination_policy,
                autoscaling_role=autoscaling_role,
                bootstrap_action=bootstrap_action,
                configurations=configurations,
                configurations_json=configurations_json,
                core_instance_fleet=core_instance_fleet,
                core_instance_group=core_instance_group,
                custom_ami_id=custom_ami_id,
                ebs_root_volume_size=ebs_root_volume_size,
                ec2_attributes=ec2_attributes,
                keep_job_flow_alive_when_no_steps=keep_job_flow_alive_when_no_steps,
                kerberos_attributes=kerberos_attributes,
                list_steps_states=list_steps_states,
                log_encryption_kms_key_id=log_encryption_kms_key_id,
                log_uri=log_uri,
                master_instance_fleet=master_instance_fleet,
                master_instance_group=master_instance_group,
                scale_down_behavior=scale_down_behavior,
                security_configuration=security_configuration,
                step=step,
                step_concurrency_level=step_concurrency_level,
                tags=tags,
                tags_all=tags_all,
                termination_protection=termination_protection,
                visible_to_all_users=visible_to_all_users,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        additional_info: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        applications: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        auto_termination_policy: Optional[AutoTerminationPolicy] = core.arg(default=None)

        autoscaling_role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bootstrap_action: Optional[
            Union[List[BootstrapAction], core.ArrayOut[BootstrapAction]]
        ] = core.arg(default=None)

        configurations: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        configurations_json: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        core_instance_fleet: Optional[CoreInstanceFleet] = core.arg(default=None)

        core_instance_group: Optional[CoreInstanceGroup] = core.arg(default=None)

        custom_ami_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ebs_root_volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        ec2_attributes: Optional[Ec2Attributes] = core.arg(default=None)

        keep_job_flow_alive_when_no_steps: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        kerberos_attributes: Optional[KerberosAttributes] = core.arg(default=None)

        list_steps_states: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        log_encryption_kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        master_instance_fleet: Optional[MasterInstanceFleet] = core.arg(default=None)

        master_instance_group: Optional[MasterInstanceGroup] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        release_label: Union[str, core.StringOut] = core.arg()

        scale_down_behavior: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_configuration: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_role: Union[str, core.StringOut] = core.arg()

        step: Optional[Union[List[Step], core.ArrayOut[Step]]] = core.arg(default=None)

        step_concurrency_level: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        termination_protection: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        visible_to_all_users: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
