from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_redshift_orderable_cluster", namespace="aws_redshift")
class DsOrderableCluster(core.Data):

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    cluster_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    cluster_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    node_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    preferred_node_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        cluster_type: Optional[Union[str, core.StringOut]] = None,
        cluster_version: Optional[Union[str, core.StringOut]] = None,
        node_type: Optional[Union[str, core.StringOut]] = None,
        preferred_node_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOrderableCluster.Args(
                cluster_type=cluster_type,
                cluster_version=cluster_version,
                node_type=node_type,
                preferred_node_types=preferred_node_types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        node_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        preferred_node_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )
