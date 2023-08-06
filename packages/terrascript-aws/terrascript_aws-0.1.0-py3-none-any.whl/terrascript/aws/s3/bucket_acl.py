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
class Grant(core.Schema):

    grantee: Optional[Grantee] = core.attr(Grantee, default=None)

    permission: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        permission: Union[str, core.StringOut],
        grantee: Optional[Grantee] = None,
    ):
        super().__init__(
            args=Grant.Args(
                permission=permission,
                grantee=grantee,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grantee: Optional[Grantee] = core.arg(default=None)

        permission: Union[str, core.StringOut] = core.arg()


@core.schema
class Owner(core.Schema):

    display_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        display_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Owner.Args(
                id=id,
                display_name=display_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        display_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        id: Union[str, core.StringOut] = core.arg()


@core.schema
class AccessControlPolicy(core.Schema):

    grant: Optional[Union[List[Grant], core.ArrayOut[Grant]]] = core.attr(
        Grant, default=None, kind=core.Kind.array
    )

    owner: Owner = core.attr(Owner)

    def __init__(
        self,
        *,
        owner: Owner,
        grant: Optional[Union[List[Grant], core.ArrayOut[Grant]]] = None,
    ):
        super().__init__(
            args=AccessControlPolicy.Args(
                owner=owner,
                grant=grant,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grant: Optional[Union[List[Grant], core.ArrayOut[Grant]]] = core.arg(default=None)

        owner: Owner = core.arg()


@core.resource(type="aws_s3_bucket_acl", namespace="aws_s3")
class BucketAcl(core.Resource):

    access_control_policy: Optional[AccessControlPolicy] = core.attr(
        AccessControlPolicy, default=None, computed=True
    )

    acl: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket: Union[str, core.StringOut] = core.attr(str)

    expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        access_control_policy: Optional[AccessControlPolicy] = None,
        acl: Optional[Union[str, core.StringOut]] = None,
        expected_bucket_owner: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketAcl.Args(
                bucket=bucket,
                access_control_policy=access_control_policy,
                acl=acl,
                expected_bucket_owner=expected_bucket_owner,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_control_policy: Optional[AccessControlPolicy] = core.arg(default=None)

        acl: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket: Union[str, core.StringOut] = core.arg()

        expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)
