from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_chime_voice_connector_termination", namespace="aws_chime")
class VoiceConnectorTermination(core.Resource):

    calling_regions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    cidr_allow_list: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    cps_limit: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    default_phone_number: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    disabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    voice_connector_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        calling_regions: Union[List[str], core.ArrayOut[core.StringOut]],
        cidr_allow_list: Union[List[str], core.ArrayOut[core.StringOut]],
        voice_connector_id: Union[str, core.StringOut],
        cps_limit: Optional[Union[int, core.IntOut]] = None,
        default_phone_number: Optional[Union[str, core.StringOut]] = None,
        disabled: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VoiceConnectorTermination.Args(
                calling_regions=calling_regions,
                cidr_allow_list=cidr_allow_list,
                voice_connector_id=voice_connector_id,
                cps_limit=cps_limit,
                default_phone_number=default_phone_number,
                disabled=disabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        calling_regions: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        cidr_allow_list: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        cps_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        default_phone_number: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        disabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        voice_connector_id: Union[str, core.StringOut] = core.arg()
