from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class GlobalClusterMembers(core.Schema):

    db_cluster_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    is_writer: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        db_cluster_arn: Union[str, core.StringOut],
        is_writer: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=GlobalClusterMembers.Args(
                db_cluster_arn=db_cluster_arn,
                is_writer=is_writer,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        db_cluster_arn: Union[str, core.StringOut] = core.arg()

        is_writer: Union[bool, core.BoolOut] = core.arg()


@core.resource(type="aws_rds_global_cluster", namespace="aws_rds")
class GlobalCluster(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    database_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    deletion_protection: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    engine: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    engine_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    force_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    global_cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    global_cluster_members: Union[
        List[GlobalClusterMembers], core.ArrayOut[GlobalClusterMembers]
    ] = core.attr(GlobalClusterMembers, computed=True, kind=core.Kind.array)

    global_cluster_resource_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_db_cluster_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    storage_encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        global_cluster_identifier: Union[str, core.StringOut],
        database_name: Optional[Union[str, core.StringOut]] = None,
        deletion_protection: Optional[Union[bool, core.BoolOut]] = None,
        engine: Optional[Union[str, core.StringOut]] = None,
        engine_version: Optional[Union[str, core.StringOut]] = None,
        force_destroy: Optional[Union[bool, core.BoolOut]] = None,
        source_db_cluster_identifier: Optional[Union[str, core.StringOut]] = None,
        storage_encrypted: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GlobalCluster.Args(
                global_cluster_identifier=global_cluster_identifier,
                database_name=database_name,
                deletion_protection=deletion_protection,
                engine=engine,
                engine_version=engine_version,
                force_destroy=force_destroy,
                source_db_cluster_identifier=source_db_cluster_identifier,
                storage_encrypted=storage_encrypted,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        database_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        deletion_protection: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        engine: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        force_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        global_cluster_identifier: Union[str, core.StringOut] = core.arg()

        source_db_cluster_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        storage_encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
