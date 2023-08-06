from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_eks_addon", namespace="aws_eks")
class DsAddon(core.Data):

    addon_name: Union[str, core.StringOut] = core.attr(str)

    addon_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_name: Union[str, core.StringOut] = core.attr(str)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    modified_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_account_role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        addon_name: Union[str, core.StringOut],
        cluster_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAddon.Args(
                addon_name=addon_name,
                cluster_name=cluster_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        addon_name: Union[str, core.StringOut] = core.arg()

        cluster_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
