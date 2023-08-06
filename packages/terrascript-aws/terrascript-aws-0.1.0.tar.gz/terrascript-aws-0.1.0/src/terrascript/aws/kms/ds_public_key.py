from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_kms_public_key", namespace="aws_kms")
class DsPublicKey(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_master_key_spec: Union[str, core.StringOut] = core.attr(str, computed=True)

    encryption_algorithms: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    grant_tokens: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_id: Union[str, core.StringOut] = core.attr(str)

    key_usage: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_key_pem: Union[str, core.StringOut] = core.attr(str, computed=True)

    signing_algorithms: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        key_id: Union[str, core.StringOut],
        grant_tokens: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPublicKey.Args(
                key_id=key_id,
                grant_tokens=grant_tokens,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grant_tokens: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        key_id: Union[str, core.StringOut] = core.arg()
