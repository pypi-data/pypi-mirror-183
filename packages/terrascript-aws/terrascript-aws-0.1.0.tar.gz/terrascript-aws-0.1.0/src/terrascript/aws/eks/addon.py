from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_eks_addon", namespace="aws_eks")
class Addon(core.Resource):

    addon_name: Union[str, core.StringOut] = core.attr(str)

    addon_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_name: Union[str, core.StringOut] = core.attr(str)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    modified_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    preserve: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    resolve_conflicts: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    service_account_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        addon_name: Union[str, core.StringOut],
        cluster_name: Union[str, core.StringOut],
        addon_version: Optional[Union[str, core.StringOut]] = None,
        preserve: Optional[Union[bool, core.BoolOut]] = None,
        resolve_conflicts: Optional[Union[str, core.StringOut]] = None,
        service_account_role_arn: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Addon.Args(
                addon_name=addon_name,
                cluster_name=cluster_name,
                addon_version=addon_version,
                preserve=preserve,
                resolve_conflicts=resolve_conflicts,
                service_account_role_arn=service_account_role_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        addon_name: Union[str, core.StringOut] = core.arg()

        addon_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_name: Union[str, core.StringOut] = core.arg()

        preserve: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        resolve_conflicts: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_account_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
