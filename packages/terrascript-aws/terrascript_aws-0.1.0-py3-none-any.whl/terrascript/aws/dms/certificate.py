from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dms_certificate", namespace="aws_dms")
class Certificate(core.Resource):

    certificate_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_id: Union[str, core.StringOut] = core.attr(str)

    certificate_pem: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    certificate_wallet: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        certificate_id: Union[str, core.StringOut],
        certificate_pem: Optional[Union[str, core.StringOut]] = None,
        certificate_wallet: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Certificate.Args(
                certificate_id=certificate_id,
                certificate_pem=certificate_pem,
                certificate_wallet=certificate_wallet,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_id: Union[str, core.StringOut] = core.arg()

        certificate_pem: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        certificate_wallet: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
