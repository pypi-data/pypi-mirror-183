from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.data(type="aws_imagebuilder_component", namespace="aws_imagebuilder")
class DsComponent(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str)

    change_description: Union[str, core.StringOut] = core.attr(str, computed=True)

    data: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_created: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform: Union[str, core.StringOut] = core.attr(str, computed=True)

    supported_os_versions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsComponent.Args(
                arn=arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
