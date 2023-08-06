from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_db_proxy_target", namespace="aws_rds")
class DbProxyTarget(core.Resource):

    db_cluster_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    db_instance_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    db_proxy_name: Union[str, core.StringOut] = core.attr(str)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    rds_resource_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    target_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    target_group_name: Union[str, core.StringOut] = core.attr(str)

    tracked_cluster_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        db_proxy_name: Union[str, core.StringOut],
        target_group_name: Union[str, core.StringOut],
        db_cluster_identifier: Optional[Union[str, core.StringOut]] = None,
        db_instance_identifier: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbProxyTarget.Args(
                db_proxy_name=db_proxy_name,
                target_group_name=target_group_name,
                db_cluster_identifier=db_cluster_identifier,
                db_instance_identifier=db_instance_identifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        db_cluster_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        db_instance_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        db_proxy_name: Union[str, core.StringOut] = core.arg()

        target_group_name: Union[str, core.StringOut] = core.arg()
