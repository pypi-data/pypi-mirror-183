from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_redshift_snapshot_schedule_association", namespace="aws_redshift")
class SnapshotScheduleAssociation(core.Resource):

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    schedule_identifier: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_identifier: Union[str, core.StringOut],
        schedule_identifier: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SnapshotScheduleAssociation.Args(
                cluster_identifier=cluster_identifier,
                schedule_identifier=schedule_identifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_identifier: Union[str, core.StringOut] = core.arg()

        schedule_identifier: Union[str, core.StringOut] = core.arg()
