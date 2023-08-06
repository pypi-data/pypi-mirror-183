from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Network(core.Schema):

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Network.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.schema
class IdentityProvider(core.Schema):

    saml_metadata: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        saml_metadata: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=IdentityProvider.Args(
                saml_metadata=saml_metadata,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        saml_metadata: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_worklink_fleet", namespace="aws_worklink")
class Fleet(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    audit_stream_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    company_code: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    device_ca_certificate: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    display_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity_provider: Optional[IdentityProvider] = core.attr(IdentityProvider, default=None)

    last_updated_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    network: Optional[Network] = core.attr(Network, default=None)

    optimize_for_end_user_location: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        audit_stream_arn: Optional[Union[str, core.StringOut]] = None,
        device_ca_certificate: Optional[Union[str, core.StringOut]] = None,
        display_name: Optional[Union[str, core.StringOut]] = None,
        identity_provider: Optional[IdentityProvider] = None,
        network: Optional[Network] = None,
        optimize_for_end_user_location: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Fleet.Args(
                name=name,
                audit_stream_arn=audit_stream_arn,
                device_ca_certificate=device_ca_certificate,
                display_name=display_name,
                identity_provider=identity_provider,
                network=network,
                optimize_for_end_user_location=optimize_for_end_user_location,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        audit_stream_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        device_ca_certificate: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        display_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identity_provider: Optional[IdentityProvider] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        network: Optional[Network] = core.arg(default=None)

        optimize_for_end_user_location: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
