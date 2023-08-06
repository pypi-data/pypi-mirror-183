from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_storagegateway_tape_pool", namespace="aws_storagegateway")
class TapePool(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    pool_name: Union[str, core.StringOut] = core.attr(str)

    retention_lock_time_in_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    retention_lock_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    storage_class: Union[str, core.StringOut] = core.attr(str)

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
        pool_name: Union[str, core.StringOut],
        storage_class: Union[str, core.StringOut],
        retention_lock_time_in_days: Optional[Union[int, core.IntOut]] = None,
        retention_lock_type: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TapePool.Args(
                pool_name=pool_name,
                storage_class=storage_class,
                retention_lock_time_in_days=retention_lock_time_in_days,
                retention_lock_type=retention_lock_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        pool_name: Union[str, core.StringOut] = core.arg()

        retention_lock_time_in_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        retention_lock_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        storage_class: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
