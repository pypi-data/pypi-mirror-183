from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_kms_ciphertext", namespace="aws_kms")
class Ciphertext(core.Resource):

    ciphertext_blob: Union[str, core.StringOut] = core.attr(str, computed=True)

    context: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_id: Union[str, core.StringOut] = core.attr(str)

    plaintext: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        key_id: Union[str, core.StringOut],
        plaintext: Union[str, core.StringOut],
        context: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ciphertext.Args(
                key_id=key_id,
                plaintext=plaintext,
                context=context,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        context: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        key_id: Union[str, core.StringOut] = core.arg()

        plaintext: Union[str, core.StringOut] = core.arg()
