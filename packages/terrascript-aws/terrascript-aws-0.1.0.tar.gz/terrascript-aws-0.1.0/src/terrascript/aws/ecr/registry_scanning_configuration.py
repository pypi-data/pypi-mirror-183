from typing import List, Optional, Union

import terrascript.core as core


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

    repository_filter: Union[List[RepositoryFilter], core.ArrayOut[RepositoryFilter]] = core.attr(
        RepositoryFilter, kind=core.Kind.array
    )

    scan_frequency: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        repository_filter: Union[List[RepositoryFilter], core.ArrayOut[RepositoryFilter]],
        scan_frequency: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Rule.Args(
                repository_filter=repository_filter,
                scan_frequency=scan_frequency,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        repository_filter: Union[
            List[RepositoryFilter], core.ArrayOut[RepositoryFilter]
        ] = core.arg()

        scan_frequency: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_ecr_registry_scanning_configuration", namespace="aws_ecr")
class RegistryScanningConfiguration(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    registry_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    rule: Optional[Union[List[Rule], core.ArrayOut[Rule]]] = core.attr(
        Rule, default=None, kind=core.Kind.array
    )

    scan_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        scan_type: Union[str, core.StringOut],
        rule: Optional[Union[List[Rule], core.ArrayOut[Rule]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RegistryScanningConfiguration.Args(
                scan_type=scan_type,
                rule=rule,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        rule: Optional[Union[List[Rule], core.ArrayOut[Rule]]] = core.arg(default=None)

        scan_type: Union[str, core.StringOut] = core.arg()
