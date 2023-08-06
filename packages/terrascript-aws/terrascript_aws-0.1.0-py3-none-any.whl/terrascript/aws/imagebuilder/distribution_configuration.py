from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class LaunchPermission(core.Schema):

    organization_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    organizational_unit_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    user_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    user_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        organization_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        organizational_unit_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        user_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        user_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
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
        organization_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        organizational_unit_arns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        user_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class AmiDistributionConfiguration(core.Schema):

    ami_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    launch_permission: Optional[LaunchPermission] = core.attr(LaunchPermission, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    target_account_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        ami_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        launch_permission: Optional[LaunchPermission] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        target_account_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AmiDistributionConfiguration.Args(
                ami_tags=ami_tags,
                description=description,
                kms_key_id=kms_key_id,
                launch_permission=launch_permission,
                name=name,
                target_account_ids=target_account_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ami_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        launch_permission: Optional[LaunchPermission] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_account_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class TargetRepository(core.Schema):

    repository_name: Union[str, core.StringOut] = core.attr(str)

    service: Union[str, core.StringOut] = core.attr(str)

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

    container_tags: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    target_repository: TargetRepository = core.attr(TargetRepository)

    def __init__(
        self,
        *,
        target_repository: TargetRepository,
        container_tags: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ContainerDistributionConfiguration.Args(
                target_repository=target_repository,
                container_tags=container_tags,
                description=description,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_tags: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_repository: TargetRepository = core.arg()


@core.schema
class SnapshotConfiguration(core.Schema):

    target_resource_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        target_resource_count: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=SnapshotConfiguration.Args(
                target_resource_count=target_resource_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_resource_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class LaunchTemplate(core.Schema):

    launch_template_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    launch_template_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    launch_template_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        launch_template_id: Optional[Union[str, core.StringOut]] = None,
        launch_template_name: Optional[Union[str, core.StringOut]] = None,
        launch_template_version: Optional[Union[str, core.StringOut]] = None,
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
        launch_template_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        launch_template_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        launch_template_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class FastLaunchConfiguration(core.Schema):

    account_id: Union[str, core.StringOut] = core.attr(str)

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    launch_template: Optional[LaunchTemplate] = core.attr(LaunchTemplate, default=None)

    max_parallel_launches: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    snapshot_configuration: Optional[SnapshotConfiguration] = core.attr(
        SnapshotConfiguration, default=None
    )

    def __init__(
        self,
        *,
        account_id: Union[str, core.StringOut],
        enabled: Union[bool, core.BoolOut],
        launch_template: Optional[LaunchTemplate] = None,
        max_parallel_launches: Optional[Union[int, core.IntOut]] = None,
        snapshot_configuration: Optional[SnapshotConfiguration] = None,
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

        launch_template: Optional[LaunchTemplate] = core.arg(default=None)

        max_parallel_launches: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        snapshot_configuration: Optional[SnapshotConfiguration] = core.arg(default=None)


@core.schema
class LaunchTemplateConfiguration(core.Schema):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    default: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    launch_template_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        launch_template_id: Union[str, core.StringOut],
        account_id: Optional[Union[str, core.StringOut]] = None,
        default: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=LaunchTemplateConfiguration.Args(
                launch_template_id=launch_template_id,
                account_id=account_id,
                default=default,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        launch_template_id: Union[str, core.StringOut] = core.arg()


@core.schema
class Distribution(core.Schema):

    ami_distribution_configuration: Optional[AmiDistributionConfiguration] = core.attr(
        AmiDistributionConfiguration, default=None
    )

    container_distribution_configuration: Optional[ContainerDistributionConfiguration] = core.attr(
        ContainerDistributionConfiguration, default=None
    )

    fast_launch_configuration: Optional[
        Union[List[FastLaunchConfiguration], core.ArrayOut[FastLaunchConfiguration]]
    ] = core.attr(FastLaunchConfiguration, default=None, kind=core.Kind.array)

    launch_template_configuration: Optional[
        Union[List[LaunchTemplateConfiguration], core.ArrayOut[LaunchTemplateConfiguration]]
    ] = core.attr(LaunchTemplateConfiguration, default=None, kind=core.Kind.array)

    license_configuration_arns: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    region: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        region: Union[str, core.StringOut],
        ami_distribution_configuration: Optional[AmiDistributionConfiguration] = None,
        container_distribution_configuration: Optional[ContainerDistributionConfiguration] = None,
        fast_launch_configuration: Optional[
            Union[List[FastLaunchConfiguration], core.ArrayOut[FastLaunchConfiguration]]
        ] = None,
        launch_template_configuration: Optional[
            Union[List[LaunchTemplateConfiguration], core.ArrayOut[LaunchTemplateConfiguration]]
        ] = None,
        license_configuration_arns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
    ):
        super().__init__(
            args=Distribution.Args(
                region=region,
                ami_distribution_configuration=ami_distribution_configuration,
                container_distribution_configuration=container_distribution_configuration,
                fast_launch_configuration=fast_launch_configuration,
                launch_template_configuration=launch_template_configuration,
                license_configuration_arns=license_configuration_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ami_distribution_configuration: Optional[AmiDistributionConfiguration] = core.arg(
            default=None
        )

        container_distribution_configuration: Optional[
            ContainerDistributionConfiguration
        ] = core.arg(default=None)

        fast_launch_configuration: Optional[
            Union[List[FastLaunchConfiguration], core.ArrayOut[FastLaunchConfiguration]]
        ] = core.arg(default=None)

        launch_template_configuration: Optional[
            Union[List[LaunchTemplateConfiguration], core.ArrayOut[LaunchTemplateConfiguration]]
        ] = core.arg(default=None)

        license_configuration_arns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        region: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_imagebuilder_distribution_configuration", namespace="aws_imagebuilder")
class DistributionConfiguration(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_created: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_updated: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    distribution: Union[List[Distribution], core.ArrayOut[Distribution]] = core.attr(
        Distribution, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        distribution: Union[List[Distribution], core.ArrayOut[Distribution]],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DistributionConfiguration.Args(
                distribution=distribution,
                name=name,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        distribution: Union[List[Distribution], core.ArrayOut[Distribution]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
