from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Destination(core.Schema):

    region: Union[str, core.StringOut] = core.attr(str)

    registry_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        region: Union[str, core.StringOut],
        registry_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Destination.Args(
                region=region,
                registry_id=registry_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region: Union[str, core.StringOut] = core.arg()

        registry_id: Union[str, core.StringOut] = core.arg()


@core.schema
class RepositoryFilter(core.Schema):

    filter: Union[str, core.StringOut] = core.attr(str)

    filter_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        filter: Union[str, core.StringOut],
        filter_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RepositoryFilter.Args(
                filter=filter,
                filter_type=filter_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Union[str, core.StringOut] = core.arg()

        filter_type: Union[str, core.StringOut] = core.arg()


@core.schema
class Rule(core.Schema):

    destination: Union[List[Destination], core.ArrayOut[Destination]] = core.attr(
        Destination, kind=core.Kind.array
    )

    repository_filter: Optional[
        Union[List[RepositoryFilter], core.ArrayOut[RepositoryFilter]]
    ] = core.attr(RepositoryFilter, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        destination: Union[List[Destination], core.ArrayOut[Destination]],
        repository_filter: Optional[
            Union[List[RepositoryFilter], core.ArrayOut[RepositoryFilter]]
        ] = None,
    ):
        super().__init__(
            args=Rule.Args(
                destination=destination,
                repository_filter=repository_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: Union[List[Destination], core.ArrayOut[Destination]] = core.arg()

        repository_filter: Optional[
            Union[List[RepositoryFilter], core.ArrayOut[RepositoryFilter]]
        ] = core.arg(default=None)


@core.schema
class ReplicationConfigurationBlk(core.Schema):

    rule: Union[List[Rule], core.ArrayOut[Rule]] = core.attr(Rule, kind=core.Kind.array)

    def __init__(
        self,
        *,
        rule: Union[List[Rule], core.ArrayOut[Rule]],
    ):
        super().__init__(
            args=ReplicationConfigurationBlk.Args(
                rule=rule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rule: Union[List[Rule], core.ArrayOut[Rule]] = core.arg()


@core.resource(type="aws_ecr_replication_configuration", namespace="aws_ecr")
class ReplicationConfiguration(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    registry_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    replication_configuration: Optional[ReplicationConfigurationBlk] = core.attr(
        ReplicationConfigurationBlk, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        replication_configuration: Optional[ReplicationConfigurationBlk] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationConfiguration.Args(
                replication_configuration=replication_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        replication_configuration: Optional[ReplicationConfigurationBlk] = core.arg(default=None)
