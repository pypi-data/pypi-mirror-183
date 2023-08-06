from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class DefaultCapacityProviderStrategy(core.Schema):

    base: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    capacity_provider: Union[str, core.StringOut] = core.attr(str)

    weight: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        capacity_provider: Union[str, core.StringOut],
        base: Optional[Union[int, core.IntOut]] = None,
        weight: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=DefaultCapacityProviderStrategy.Args(
                capacity_provider=capacity_provider,
                base=base,
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        base: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        capacity_provider: Union[str, core.StringOut] = core.arg()

        weight: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_ecs_cluster_capacity_providers", namespace="aws_ecs")
class ClusterCapacityProviders(core.Resource):

    capacity_providers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    cluster_name: Union[str, core.StringOut] = core.attr(str)

    default_capacity_provider_strategy: Optional[
        Union[List[DefaultCapacityProviderStrategy], core.ArrayOut[DefaultCapacityProviderStrategy]]
    ] = core.attr(DefaultCapacityProviderStrategy, default=None, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_name: Union[str, core.StringOut],
        capacity_providers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        default_capacity_provider_strategy: Optional[
            Union[
                List[DefaultCapacityProviderStrategy],
                core.ArrayOut[DefaultCapacityProviderStrategy],
            ]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterCapacityProviders.Args(
                cluster_name=cluster_name,
                capacity_providers=capacity_providers,
                default_capacity_provider_strategy=default_capacity_provider_strategy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity_providers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        cluster_name: Union[str, core.StringOut] = core.arg()

        default_capacity_provider_strategy: Optional[
            Union[
                List[DefaultCapacityProviderStrategy],
                core.ArrayOut[DefaultCapacityProviderStrategy],
            ]
        ] = core.arg(default=None)
