from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dms_replication_subnet_group", namespace="aws_dms")
class ReplicationSubnetGroup(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    replication_subnet_group_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    replication_subnet_group_description: Union[str, core.StringOut] = core.attr(str)

    replication_subnet_group_id: Union[str, core.StringOut] = core.attr(str)

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

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
        replication_subnet_group_description: Union[str, core.StringOut],
        replication_subnet_group_id: Union[str, core.StringOut],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationSubnetGroup.Args(
                replication_subnet_group_description=replication_subnet_group_description,
                replication_subnet_group_id=replication_subnet_group_id,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        replication_subnet_group_description: Union[str, core.StringOut] = core.arg()

        replication_subnet_group_id: Union[str, core.StringOut] = core.arg()

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
