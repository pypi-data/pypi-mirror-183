from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class LaunchPermission(core.Schema):

    organization_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    organizational_unit_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    user_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    user_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        organization_arns: Union[List[str], core.ArrayOut[core.StringOut]],
        organizational_unit_arns: Union[List[str], core.ArrayOut[core.StringOut]],
        user_groups: Union[List[str], core.ArrayOut[core.StringOut]],
        user_ids: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=LaunchPermission.Args(
                organization_arns=organization_arns,
                organizational_unit_arns=organizational_unit_arns,
                user_groups=user_groups,
                user_ids=user_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        organization_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        organizational_unit_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        user_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        user_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class AmiDistributionConfiguration(core.Schema):

    ami_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    launch_permission: Union[List[LaunchPermission], core.ArrayOut[LaunchPermission]] = core.attr(
        LaunchPermission, computed=True, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    target_account_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        description: Union[str, core.StringOut],
        kms_key_id: Union[str, core.StringOut],
        launch_permission: Union[List[LaunchPermission], core.ArrayOut[LaunchPermission]],
        name: Union[str, core.StringOut],
        target_account_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        ami_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AmiDistributionConfiguration.Args(
                description=description,
                kms_key_id=kms_key_id,
                launch_permission=launch_permission,
                name=name,
                target_account_ids=target_account_ids,
                ami_tags=ami_tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ami_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        description: Union[str, core.StringOut] = core.arg()

        kms_key_id: Union[str, core.StringOut] = core.arg()

        launch_permission: Union[
            List[LaunchPermission], core.ArrayOut[LaunchPermission]
        ] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        target_account_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class TargetRepository(core.Schema):

    repository_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    service: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        repository_name: Union[str, core.StringOut],
        service: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TargetRepository.Args(
                repository_name=repository_name,
                service=service,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        repository_name: Union[str, core.StringOut] = core.arg()

        service: Union[str, core.StringOut] = core.arg()


@core.schema
class ContainerDistributionConfiguration(core.Schema):

    container_tags: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    target_repository: Union[List[TargetRepository], core.ArrayOut[TargetRepository]] = core.attr(
        TargetRepository, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        container_tags: Union[List[str], core.ArrayOut[core.StringOut]],
        description: Union[str, core.StringOut],
        target_repository: Union[List[TargetRepository], core.ArrayOut[TargetRepository]],
    ):
        super().__init__(
            args=ContainerDistributionConfiguration.Args(
                container_tags=container_tags,
                description=description,
                target_repository=target_repository,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_tags: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        description: Union[str, core.StringOut] = core.arg()

        target_repository: Union[
            List[TargetRepository], core.ArrayOut[TargetRepository]
        ] = core.arg()


@core.schema
class SnapshotConfiguration(core.Schema):

    target_resource_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        target_resource_count: Union[int, core.IntOut],
    ):
        super().__init__(
            args=SnapshotConfiguration.Args(
                target_resource_count=target_resource_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_resource_count: Union[int, core.IntOut] = core.arg()


@core.schema
class LaunchTemplate(core.Schema):

    launch_template_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    launch_template_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    launch_template_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        launch_template_id: Union[str, core.StringOut],
        launch_template_name: Union[str, core.StringOut],
        launch_template_version: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LaunchTemplate.Args(
                launch_template_id=launch_template_id,
                launch_template_name=launch_template_name,
                launch_template_version=launch_template_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_id: Union[str, core.StringOut] = core.arg()

        launch_template_name: Union[str, core.StringOut] = core.arg()

        launch_template_version: Union[str, core.StringOut] = core.arg()


@core.schema
class FastLaunchConfiguration(core.Schema):

    account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    launch_template: Union[List[LaunchTemplate], core.ArrayOut[LaunchTemplate]] = core.attr(
        LaunchTemplate, computed=True, kind=core.Kind.array
    )

    max_parallel_launches: Union[int, core.IntOut] = core.attr(int, computed=True)

    snapshot_configuration: Union[
        List[SnapshotConfiguration], core.ArrayOut[SnapshotConfiguration]
    ] = core.attr(SnapshotConfiguration, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        account_id: Union[str, core.StringOut],
        enabled: Union[bool, core.BoolOut],
        launch_template: Union[List[LaunchTemplate], core.ArrayOut[LaunchTemplate]],
        max_parallel_launches: Union[int, core.IntOut],
        snapshot_configuration: Union[
            List[SnapshotConfiguration], core.ArrayOut[SnapshotConfiguration]
        ],
    ):
        super().__init__(
            args=FastLaunchConfiguration.Args(
                account_id=account_id,
                enabled=enabled,
                launch_template=launch_template,
                max_parallel_launches=max_parallel_launches,
                snapshot_configuration=snapshot_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: Union[str, core.StringOut] = core.arg()

        enabled: Union[bool, core.BoolOut] = core.arg()

        launch_template: Union[List[LaunchTemplate], core.ArrayOut[LaunchTemplate]] = core.arg()

        max_parallel_launches: Union[int, core.IntOut] = core.arg()

        snapshot_configuration: Union[
            List[SnapshotConfiguration], core.ArrayOut[SnapshotConfiguration]
        ] = core.arg()


@core.schema
class LaunchTemplateConfiguration(core.Schema):

    account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    default: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    launch_template_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        account_id: Union[str, core.StringOut],
        default: Union[bool, core.BoolOut],
        launch_template_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LaunchTemplateConfiguration.Args(
                account_id=account_id,
                default=default,
                launch_template_id=launch_template_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: Union[str, core.StringOut] = core.arg()

        default: Union[bool, core.BoolOut] = core.arg()

        launch_template_id: Union[str, core.StringOut] = core.arg()


@core.schema
class Distribution(core.Schema):

    ami_distribution_configuration: Union[
        List[AmiDistributionConfiguration], core.ArrayOut[AmiDistributionConfiguration]
    ] = core.attr(AmiDistributionConfiguration, computed=True, kind=core.Kind.array)

    container_distribution_configuration: Union[
        List[ContainerDistributionConfiguration], core.ArrayOut[ContainerDistributionConfiguration]
    ] = core.attr(ContainerDistributionConfiguration, computed=True, kind=core.Kind.array)

    fast_launch_configuration: Union[
        List[FastLaunchConfiguration], core.ArrayOut[FastLaunchConfiguration]
    ] = core.attr(FastLaunchConfiguration, computed=True, kind=core.Kind.array)

    launch_template_configuration: Union[
        List[LaunchTemplateConfiguration], core.ArrayOut[LaunchTemplateConfiguration]
    ] = core.attr(LaunchTemplateConfiguration, computed=True, kind=core.Kind.array)

    license_configuration_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    region: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        ami_distribution_configuration: Union[
            List[AmiDistributionConfiguration], core.ArrayOut[AmiDistributionConfiguration]
        ],
        container_distribution_configuration: Union[
            List[ContainerDistributionConfiguration],
            core.ArrayOut[ContainerDistributionConfiguration],
        ],
        fast_launch_configuration: Union[
            List[FastLaunchConfiguration], core.ArrayOut[FastLaunchConfiguration]
        ],
        launch_template_configuration: Union[
            List[LaunchTemplateConfiguration], core.ArrayOut[LaunchTemplateConfiguration]
        ],
        license_configuration_arns: Union[List[str], core.ArrayOut[core.StringOut]],
        region: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Distribution.Args(
                ami_distribution_configuration=ami_distribution_configuration,
                container_distribution_configuration=container_distribution_configuration,
                fast_launch_configuration=fast_launch_configuration,
                launch_template_configuration=launch_template_configuration,
                license_configuration_arns=license_configuration_arns,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ami_distribution_configuration: Union[
            List[AmiDistributionConfiguration], core.ArrayOut[AmiDistributionConfiguration]
        ] = core.arg()

        container_distribution_configuration: Union[
            List[ContainerDistributionConfiguration],
            core.ArrayOut[ContainerDistributionConfiguration],
        ] = core.arg()

        fast_launch_configuration: Union[
            List[FastLaunchConfiguration], core.ArrayOut[FastLaunchConfiguration]
        ] = core.arg()

        launch_template_configuration: Union[
            List[LaunchTemplateConfiguration], core.ArrayOut[LaunchTemplateConfiguration]
        ] = core.arg()

        license_configuration_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        region: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_imagebuilder_distribution_configuration", namespace="aws_imagebuilder")
class DsDistributionConfiguration(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str)

    date_created: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_updated: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    distribution: Union[List[Distribution], core.ArrayOut[Distribution]] = core.attr(
        Distribution, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDistributionConfiguration.Args(
                arn=arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
