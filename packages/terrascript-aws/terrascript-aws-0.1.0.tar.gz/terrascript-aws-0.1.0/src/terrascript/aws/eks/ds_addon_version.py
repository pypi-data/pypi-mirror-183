from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_eks_addon_version", namespace="aws_eks")
class DsAddonVersion(core.Data):

    addon_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kubernetes_version: Union[str, core.StringOut] = core.attr(str)

    most_recent: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        addon_name: Union[str, core.StringOut],
        kubernetes_version: Union[str, core.StringOut],
        most_recent: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAddonVersion.Args(
                addon_name=addon_name,
                kubernetes_version=kubernetes_version,
                most_recent=most_recent,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        addon_name: Union[str, core.StringOut] = core.arg()

        kubernetes_version: Union[str, core.StringOut] = core.arg()

        most_recent: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
