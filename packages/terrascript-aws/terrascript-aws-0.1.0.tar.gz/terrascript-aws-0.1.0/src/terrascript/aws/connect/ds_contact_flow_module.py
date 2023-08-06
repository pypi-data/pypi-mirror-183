from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_connect_contact_flow_module", namespace="aws_connect")
class DsContactFlowModule(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    contact_flow_module_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    content: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: Union[str, core.StringOut],
        contact_flow_module_id: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsContactFlowModule.Args(
                instance_id=instance_id,
                contact_flow_module_id=contact_flow_module_id,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        contact_flow_module_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_id: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
