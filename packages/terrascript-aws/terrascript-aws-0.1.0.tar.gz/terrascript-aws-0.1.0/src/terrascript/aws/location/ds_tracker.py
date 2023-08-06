from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_location_tracker", namespace="aws_location")
class DsTracker(core.Data):

    create_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    position_filtering: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tracker_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    tracker_name: Union[str, core.StringOut] = core.attr(str)

    update_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        tracker_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsTracker.Args(
                tracker_name=tracker_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tracker_name: Union[str, core.StringOut] = core.arg()
