from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AclConfiguration(core.Schema):

    s3_acl_option: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        s3_acl_option: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AclConfiguration.Args(
                s3_acl_option=s3_acl_option,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_acl_option: Union[str, core.StringOut] = core.arg()


@core.schema
class EncryptionConfiguration(core.Schema):

    encryption_option: Union[str, core.StringOut] = core.attr(str)

    kms_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        encryption_option: Union[str, core.StringOut],
        kms_key: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                encryption_option=encryption_option,
                kms_key=kms_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_option: Union[str, core.StringOut] = core.arg()

        kms_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_athena_database", namespace="aws_athena")
class Database(core.Resource):

    acl_configuration: Optional[AclConfiguration] = core.attr(AclConfiguration, default=None)

    bucket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    comment: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encryption_configuration: Optional[EncryptionConfiguration] = core.attr(
        EncryptionConfiguration, default=None
    )

    expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    force_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        acl_configuration: Optional[AclConfiguration] = None,
        bucket: Optional[Union[str, core.StringOut]] = None,
        comment: Optional[Union[str, core.StringOut]] = None,
        encryption_configuration: Optional[EncryptionConfiguration] = None,
        expected_bucket_owner: Optional[Union[str, core.StringOut]] = None,
        force_destroy: Optional[Union[bool, core.BoolOut]] = None,
        properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Database.Args(
                name=name,
                acl_configuration=acl_configuration,
                bucket=bucket,
                comment=comment,
                encryption_configuration=encryption_configuration,
                expected_bucket_owner=expected_bucket_owner,
                force_destroy=force_destroy,
                properties=properties,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        acl_configuration: Optional[AclConfiguration] = core.arg(default=None)

        bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        comment: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encryption_configuration: Optional[EncryptionConfiguration] = core.arg(default=None)

        expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        force_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
