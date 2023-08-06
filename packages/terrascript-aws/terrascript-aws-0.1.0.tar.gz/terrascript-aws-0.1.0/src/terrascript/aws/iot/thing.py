from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iot_thing", namespace="aws_iot")
class Thing(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    default_client_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    thing_type_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    version: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        thing_type_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Thing.Args(
                name=name,
                attributes=attributes,
                thing_type_name=thing_type_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        thing_type_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
