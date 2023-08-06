from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_kinesisanalyticsv2_application_snapshot", namespace="aws_kinesisanalyticsv2"
)
class ApplicationSnapshot(core.Resource):

    application_name: Union[str, core.StringOut] = core.attr(str)

    application_version_id: Union[int, core.IntOut] = core.attr(int, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    snapshot_creation_timestamp: Union[str, core.StringOut] = core.attr(str, computed=True)

    snapshot_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        application_name: Union[str, core.StringOut],
        snapshot_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ApplicationSnapshot.Args(
                application_name=application_name,
                snapshot_name=snapshot_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_name: Union[str, core.StringOut] = core.arg()

        snapshot_name: Union[str, core.StringOut] = core.arg()
