from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_docdb_cluster_snapshot", namespace="aws_docdb")
class ClusterSnapshot(core.Resource):

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    db_cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    db_cluster_snapshot_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_cluster_snapshot_identifier: Union[str, core.StringOut] = core.attr(str)

    engine: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    snapshot_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_db_cluster_snapshot_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    storage_encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        db_cluster_identifier: Union[str, core.StringOut],
        db_cluster_snapshot_identifier: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterSnapshot.Args(
                db_cluster_identifier=db_cluster_identifier,
                db_cluster_snapshot_identifier=db_cluster_snapshot_identifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        db_cluster_identifier: Union[str, core.StringOut] = core.arg()

        db_cluster_snapshot_identifier: Union[str, core.StringOut] = core.arg()
