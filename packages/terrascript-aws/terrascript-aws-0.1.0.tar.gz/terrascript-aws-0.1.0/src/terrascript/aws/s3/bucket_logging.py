from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Grantee(core.Schema):

    display_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    email_address: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        display_name: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        email_address: Optional[Union[str, core.StringOut]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        uri: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Grantee.Args(
                display_name=display_name,
                type=type,
                email_address=email_address,
                id=id,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        display_name: Union[str, core.StringOut] = core.arg()

        email_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()

        uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TargetGrant(core.Schema):

    grantee: Grantee = core.attr(Grantee)

    permission: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        grantee: Grantee,
        permission: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TargetGrant.Args(
                grantee=grantee,
                permission=permission,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grantee: Grantee = core.arg()

        permission: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_s3_bucket_logging", namespace="aws_s3")
class BucketLogging(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    target_bucket: Union[str, core.StringOut] = core.attr(str)

    target_grant: Optional[Union[List[TargetGrant], core.ArrayOut[TargetGrant]]] = core.attr(
        TargetGrant, default=None, kind=core.Kind.array
    )

    target_prefix: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        target_bucket: Union[str, core.StringOut],
        target_prefix: Union[str, core.StringOut],
        expected_bucket_owner: Optional[Union[str, core.StringOut]] = None,
        target_grant: Optional[Union[List[TargetGrant], core.ArrayOut[TargetGrant]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketLogging.Args(
                bucket=bucket,
                target_bucket=target_bucket,
                target_prefix=target_prefix,
                expected_bucket_owner=expected_bucket_owner,
                target_grant=target_grant,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_bucket: Union[str, core.StringOut] = core.arg()

        target_grant: Optional[Union[List[TargetGrant], core.ArrayOut[TargetGrant]]] = core.arg(
            default=None
        )

        target_prefix: Union[str, core.StringOut] = core.arg()
