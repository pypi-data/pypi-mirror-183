from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_neptune_cluster_endpoint", namespace="aws_neptune")
class ClusterEndpoint(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_endpoint_identifier: Union[str, core.StringOut] = core.attr(str)

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint_type: Union[str, core.StringOut] = core.attr(str)

    excluded_members: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    static_members: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

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
        cluster_endpoint_identifier: Union[str, core.StringOut],
        cluster_identifier: Union[str, core.StringOut],
        endpoint_type: Union[str, core.StringOut],
        excluded_members: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        static_members: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterEndpoint.Args(
                cluster_endpoint_identifier=cluster_endpoint_identifier,
                cluster_identifier=cluster_identifier,
                endpoint_type=endpoint_type,
                excluded_members=excluded_members,
                static_members=static_members,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_endpoint_identifier: Union[str, core.StringOut] = core.arg()

        cluster_identifier: Union[str, core.StringOut] = core.arg()

        endpoint_type: Union[str, core.StringOut] = core.arg()

        excluded_members: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        static_members: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
