from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class SecretBlk(core.Schema):

    context: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    grant_tokens: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    payload: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        payload: Union[str, core.StringOut],
        context: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        grant_tokens: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=SecretBlk.Args(
                name=name,
                payload=payload,
                context=context,
                grant_tokens=grant_tokens,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        context: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        grant_tokens: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        payload: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_kms_secret", namespace="aws_kms")
class DsSecret(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    secret: Union[List[SecretBlk], core.ArrayOut[SecretBlk]] = core.attr(
        SecretBlk, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        secret: Union[List[SecretBlk], core.ArrayOut[SecretBlk]],
    ):
        super().__init__(
            name=data_name,
            args=DsSecret.Args(
                secret=secret,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        secret: Union[List[SecretBlk], core.ArrayOut[SecretBlk]] = core.arg()
