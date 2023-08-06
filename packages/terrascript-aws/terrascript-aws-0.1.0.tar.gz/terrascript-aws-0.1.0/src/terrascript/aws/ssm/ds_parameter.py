from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_ssm_parameter", namespace="aws_ssm")
class DsParameter(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    value: Union[str, core.StringOut] = core.attr(str, computed=True)

    version: Union[int, core.IntOut] = core.attr(int, computed=True)

    with_decryption: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        with_decryption: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsParameter.Args(
                name=name,
                with_decryption=with_decryption,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        with_decryption: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
