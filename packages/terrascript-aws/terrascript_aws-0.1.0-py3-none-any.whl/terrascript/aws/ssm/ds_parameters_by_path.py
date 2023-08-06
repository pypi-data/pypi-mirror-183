from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_ssm_parameters_by_path", namespace="aws_ssm")
class DsParametersByPath(core.Data):

    arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    path: Union[str, core.StringOut] = core.attr(str)

    recursive: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    with_decryption: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        path: Union[str, core.StringOut],
        recursive: Optional[Union[bool, core.BoolOut]] = None,
        with_decryption: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsParametersByPath.Args(
                path=path,
                recursive=recursive,
                with_decryption=with_decryption,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        path: Union[str, core.StringOut] = core.arg()

        recursive: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        with_decryption: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
