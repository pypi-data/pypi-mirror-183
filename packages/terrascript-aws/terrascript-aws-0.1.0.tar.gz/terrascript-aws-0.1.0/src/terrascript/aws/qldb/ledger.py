from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_qldb_ledger", namespace="aws_qldb")
class Ledger(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    deletion_protection: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    permissions_mode: Union[str, core.StringOut] = core.attr(str)

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
        permissions_mode: Union[str, core.StringOut],
        deletion_protection: Optional[Union[bool, core.BoolOut]] = None,
        kms_key: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ledger.Args(
                permissions_mode=permissions_mode,
                deletion_protection=deletion_protection,
                kms_key=kms_key,
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
        deletion_protection: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        kms_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        permissions_mode: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
