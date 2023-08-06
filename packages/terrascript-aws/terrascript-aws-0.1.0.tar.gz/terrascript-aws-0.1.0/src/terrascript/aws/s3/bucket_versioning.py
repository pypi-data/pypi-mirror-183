from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class VersioningConfiguration(core.Schema):

    mfa_delete: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    status: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        status: Union[str, core.StringOut],
        mfa_delete: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=VersioningConfiguration.Args(
                status=status,
                mfa_delete=mfa_delete,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mfa_delete: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        status: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_s3_bucket_versioning", namespace="aws_s3")
class BucketVersioning(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    mfa: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    versioning_configuration: VersioningConfiguration = core.attr(VersioningConfiguration)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        versioning_configuration: VersioningConfiguration,
        expected_bucket_owner: Optional[Union[str, core.StringOut]] = None,
        mfa: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketVersioning.Args(
                bucket=bucket,
                versioning_configuration=versioning_configuration,
                expected_bucket_owner=expected_bucket_owner,
                mfa=mfa,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mfa: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        versioning_configuration: VersioningConfiguration = core.arg()
