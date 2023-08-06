from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_lambda_layer_version", namespace="aws_lambda")
class DsLayerVersion(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    compatible_architecture: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    compatible_architectures: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    compatible_runtime: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    compatible_runtimes: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    layer_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    layer_name: Union[str, core.StringOut] = core.attr(str)

    license_info: Union[str, core.StringOut] = core.attr(str, computed=True)

    signing_job_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    signing_profile_version_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_code_hash: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_code_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    version: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        layer_name: Union[str, core.StringOut],
        compatible_architecture: Optional[Union[str, core.StringOut]] = None,
        compatible_runtime: Optional[Union[str, core.StringOut]] = None,
        version: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLayerVersion.Args(
                layer_name=layer_name,
                compatible_architecture=compatible_architecture,
                compatible_runtime=compatible_runtime,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compatible_architecture: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        compatible_runtime: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        layer_name: Union[str, core.StringOut] = core.arg()

        version: Optional[Union[int, core.IntOut]] = core.arg(default=None)
