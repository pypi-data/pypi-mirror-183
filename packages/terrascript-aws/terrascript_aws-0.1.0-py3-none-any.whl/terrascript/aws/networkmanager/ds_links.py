from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.data(type="aws_networkmanager_links", namespace="aws_networkmanager")
class DsLinks(core.Data):

    global_network_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    provider_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    site_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        global_network_id: Union[str, core.StringOut],
        provider_name: Optional[Union[str, core.StringOut]] = None,
        site_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLinks.Args(
                global_network_id=global_network_id,
                provider_name=provider_name,
                site_id=site_id,
                tags=tags,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        global_network_id: Union[str, core.StringOut] = core.arg()

        provider_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        site_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
