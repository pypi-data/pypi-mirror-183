from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_dx_connection", namespace="aws_direct_connect")
class DsDxConnection(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    aws_device: Union[str, core.StringOut] = core.attr(str, computed=True)

    bandwidth: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    location: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    owner_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    provider_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDxConnection.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
