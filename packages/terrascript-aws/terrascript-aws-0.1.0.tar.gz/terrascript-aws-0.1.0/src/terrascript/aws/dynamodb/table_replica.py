from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dynamodb_table_replica", namespace="aws_dynamodb")
class TableReplica(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    global_table_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    point_in_time_recovery: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    table_class_override: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        global_table_arn: Union[str, core.StringOut],
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        point_in_time_recovery: Optional[Union[bool, core.BoolOut]] = None,
        table_class_override: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TableReplica.Args(
                global_table_arn=global_table_arn,
                kms_key_arn=kms_key_arn,
                point_in_time_recovery=point_in_time_recovery,
                table_class_override=table_class_override,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        global_table_arn: Union[str, core.StringOut] = core.arg()

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        point_in_time_recovery: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        table_class_override: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
