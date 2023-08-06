from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ExternalConnections(core.Schema):

    external_connection_name: Union[str, core.StringOut] = core.attr(str)

    package_format: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        external_connection_name: Union[str, core.StringOut],
        package_format: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ExternalConnections.Args(
                external_connection_name=external_connection_name,
                package_format=package_format,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        external_connection_name: Union[str, core.StringOut] = core.arg()

        package_format: Union[str, core.StringOut] = core.arg()

        status: Union[str, core.StringOut] = core.arg()


@core.schema
class Upstream(core.Schema):

    repository_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        repository_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Upstream.Args(
                repository_name=repository_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        repository_name: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_codeartifact_repository", namespace="aws_codeartifact")
class Repository(core.Resource):

    administrator_account: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    domain: Union[str, core.StringOut] = core.attr(str)

    domain_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    external_connections: Optional[ExternalConnections] = core.attr(
        ExternalConnections, default=None
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    repository: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    upstream: Optional[Union[List[Upstream], core.ArrayOut[Upstream]]] = core.attr(
        Upstream, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        domain: Union[str, core.StringOut],
        repository: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        domain_owner: Optional[Union[str, core.StringOut]] = None,
        external_connections: Optional[ExternalConnections] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        upstream: Optional[Union[List[Upstream], core.ArrayOut[Upstream]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Repository.Args(
                domain=domain,
                repository=repository,
                description=description,
                domain_owner=domain_owner,
                external_connections=external_connections,
                tags=tags,
                tags_all=tags_all,
                upstream=upstream,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        domain: Union[str, core.StringOut] = core.arg()

        domain_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        external_connections: Optional[ExternalConnections] = core.arg(default=None)

        repository: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        upstream: Optional[Union[List[Upstream], core.ArrayOut[Upstream]]] = core.arg(default=None)
