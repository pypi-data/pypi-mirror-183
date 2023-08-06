from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ReservationPlanSettings(core.Schema):

    commitment: Union[str, core.StringOut] = core.attr(str)

    renewal_type: Union[str, core.StringOut] = core.attr(str)

    reserved_slots: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        commitment: Union[str, core.StringOut],
        renewal_type: Union[str, core.StringOut],
        reserved_slots: Union[int, core.IntOut],
    ):
        super().__init__(
            args=ReservationPlanSettings.Args(
                commitment=commitment,
                renewal_type=renewal_type,
                reserved_slots=reserved_slots,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        commitment: Union[str, core.StringOut] = core.arg()

        renewal_type: Union[str, core.StringOut] = core.arg()

        reserved_slots: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_media_convert_queue", namespace="aws_elemental_mediaconvert")
class MediaConvertQueue(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    pricing_plan: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    reservation_plan_settings: Optional[ReservationPlanSettings] = core.attr(
        ReservationPlanSettings, default=None, computed=True
    )

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        pricing_plan: Optional[Union[str, core.StringOut]] = None,
        reservation_plan_settings: Optional[ReservationPlanSettings] = None,
        status: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MediaConvertQueue.Args(
                name=name,
                description=description,
                pricing_plan=pricing_plan,
                reservation_plan_settings=reservation_plan_settings,
                status=status,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        pricing_plan: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        reservation_plan_settings: Optional[ReservationPlanSettings] = core.arg(default=None)

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
