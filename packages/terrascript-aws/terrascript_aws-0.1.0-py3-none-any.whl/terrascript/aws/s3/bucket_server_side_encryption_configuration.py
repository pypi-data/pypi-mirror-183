from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ApplyServerSideEncryptionByDefault(core.Schema):

    kms_master_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sse_algorithm: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        sse_algorithm: Union[str, core.StringOut],
        kms_master_key_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ApplyServerSideEncryptionByDefault.Args(
                sse_algorithm=sse_algorithm,
                kms_master_key_id=kms_master_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_master_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sse_algorithm: Union[str, core.StringOut] = core.arg()


@core.schema
class Rule(core.Schema):

    apply_server_side_encryption_by_default: Optional[
        ApplyServerSideEncryptionByDefault
    ] = core.attr(ApplyServerSideEncryptionByDefault, default=None)

    bucket_key_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        apply_server_side_encryption_by_default: Optional[
            ApplyServerSideEncryptionByDefault
        ] = None,
        bucket_key_enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Rule.Args(
                apply_server_side_encryption_by_default=apply_server_side_encryption_by_default,
                bucket_key_enabled=bucket_key_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        apply_server_side_encryption_by_default: Optional[
            ApplyServerSideEncryptionByDefault
        ] = core.arg(default=None)

        bucket_key_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.resource(type="aws_s3_bucket_server_side_encryption_configuration", namespace="aws_s3")
class BucketServerSideEncryptionConfiguration(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    rule: Union[List[Rule], core.ArrayOut[Rule]] = core.attr(Rule, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        rule: Union[List[Rule], core.ArrayOut[Rule]],
        expected_bucket_owner: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketServerSideEncryptionConfiguration.Args(
                bucket=bucket,
                rule=rule,
                expected_bucket_owner=expected_bucket_owner,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule: Union[List[Rule], core.ArrayOut[Rule]] = core.arg()
