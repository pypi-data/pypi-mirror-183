from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ClusterEndpoints(core.Schema):

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    region: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        endpoint: Union[str, core.StringOut],
        region: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ClusterEndpoints.Args(
                endpoint=endpoint,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint: Union[str, core.StringOut] = core.arg()

        region: Union[str, core.StringOut] = core.arg()


@core.resource(
    type="aws_route53recoverycontrolconfig_cluster", namespace="aws_route53recoverycontrolconfig"
)
class Cluster(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_endpoints: Union[List[ClusterEndpoints], core.ArrayOut[ClusterEndpoints]] = core.attr(
        ClusterEndpoints, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()
