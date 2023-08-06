from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lambda_layer_version", namespace="aws_lambda")
class LayerVersion(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    compatible_architectures: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    compatible_runtimes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    filename: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    layer_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    layer_name: Union[str, core.StringOut] = core.attr(str)

    license_info: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_bucket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_object_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    signing_job_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    signing_profile_version_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    skip_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    source_code_hash: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    source_code_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        layer_name: Union[str, core.StringOut],
        compatible_architectures: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        compatible_runtimes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        filename: Optional[Union[str, core.StringOut]] = None,
        license_info: Optional[Union[str, core.StringOut]] = None,
        s3_bucket: Optional[Union[str, core.StringOut]] = None,
        s3_key: Optional[Union[str, core.StringOut]] = None,
        s3_object_version: Optional[Union[str, core.StringOut]] = None,
        skip_destroy: Optional[Union[bool, core.BoolOut]] = None,
        source_code_hash: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LayerVersion.Args(
                layer_name=layer_name,
                compatible_architectures=compatible_architectures,
                compatible_runtimes=compatible_runtimes,
                description=description,
                filename=filename,
                license_info=license_info,
                s3_bucket=s3_bucket,
                s3_key=s3_key,
                s3_object_version=s3_object_version,
                skip_destroy=skip_destroy,
                source_code_hash=source_code_hash,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        compatible_architectures: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        compatible_runtimes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        filename: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        layer_name: Union[str, core.StringOut] = core.arg()

        license_info: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_object_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        skip_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        source_code_hash: Optional[Union[str, core.StringOut]] = core.arg(default=None)
