from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_db_snapshot", namespace="aws_rds")
class DbSnapshot(core.Resource):

    allocated_storage: Union[int, core.IntOut] = core.attr(int, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_instance_identifier: Union[str, core.StringOut] = core.attr(str)

    db_snapshot_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_snapshot_identifier: Union[str, core.StringOut] = core.attr(str)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    engine: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    iops: Union[int, core.IntOut] = core.attr(int, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    license_model: Union[str, core.StringOut] = core.attr(str, computed=True)

    option_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    snapshot_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_db_snapshot_identifier: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_region: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    storage_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        db_instance_identifier: Union[str, core.StringOut],
        db_snapshot_identifier: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbSnapshot.Args(
                db_instance_identifier=db_instance_identifier,
                db_snapshot_identifier=db_snapshot_identifier,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        db_instance_identifier: Union[str, core.StringOut] = core.arg()

        db_snapshot_identifier: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
