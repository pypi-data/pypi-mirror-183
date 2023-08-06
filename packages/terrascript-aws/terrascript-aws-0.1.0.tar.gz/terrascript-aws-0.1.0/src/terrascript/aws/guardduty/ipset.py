from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_guardduty_ipset", namespace="aws_guardduty")
class Ipset(core.Resource):

    activate: Union[bool, core.BoolOut] = core.attr(bool)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    detector_id: Union[str, core.StringOut] = core.attr(str)

    format: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    location: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

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
        activate: Union[bool, core.BoolOut],
        detector_id: Union[str, core.StringOut],
        format: Union[str, core.StringOut],
        location: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ipset.Args(
                activate=activate,
                detector_id=detector_id,
                format=format,
                location=location,
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        activate: Union[bool, core.BoolOut] = core.arg()

        detector_id: Union[str, core.StringOut] = core.arg()

        format: Union[str, core.StringOut] = core.arg()

        location: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
