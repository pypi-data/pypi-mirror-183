from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_kms_ciphertext", namespace="aws_kms")
class DsCiphertext(core.Data):

    ciphertext_blob: Union[str, core.StringOut] = core.attr(str, computed=True)

    context: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_id: Union[str, core.StringOut] = core.attr(str)

    plaintext: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        key_id: Union[str, core.StringOut],
        plaintext: Union[str, core.StringOut],
        context: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCiphertext.Args(
                key_id=key_id,
                plaintext=plaintext,
                context=context,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        context: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        key_id: Union[str, core.StringOut] = core.arg()

        plaintext: Union[str, core.StringOut] = core.arg()
