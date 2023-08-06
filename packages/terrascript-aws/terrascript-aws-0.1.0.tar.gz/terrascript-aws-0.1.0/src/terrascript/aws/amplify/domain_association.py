from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class SubDomain(core.Schema):

    branch_name: Union[str, core.StringOut] = core.attr(str)

    dns_record: Union[str, core.StringOut] = core.attr(str, computed=True)

    prefix: Union[str, core.StringOut] = core.attr(str)

    verified: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        branch_name: Union[str, core.StringOut],
        dns_record: Union[str, core.StringOut],
        prefix: Union[str, core.StringOut],
        verified: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=SubDomain.Args(
                branch_name=branch_name,
                dns_record=dns_record,
                prefix=prefix,
                verified=verified,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        branch_name: Union[str, core.StringOut] = core.arg()

        dns_record: Union[str, core.StringOut] = core.arg()

        prefix: Union[str, core.StringOut] = core.arg()

        verified: Union[bool, core.BoolOut] = core.arg()


@core.resource(type="aws_amplify_domain_association", namespace="aws_amplify")
class DomainAssociation(core.Resource):

    app_id: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_verification_dns_record: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    sub_domain: Union[List[SubDomain], core.ArrayOut[SubDomain]] = core.attr(
        SubDomain, kind=core.Kind.array
    )

    wait_for_verification: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        app_id: Union[str, core.StringOut],
        domain_name: Union[str, core.StringOut],
        sub_domain: Union[List[SubDomain], core.ArrayOut[SubDomain]],
        wait_for_verification: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainAssociation.Args(
                app_id=app_id,
                domain_name=domain_name,
                sub_domain=sub_domain,
                wait_for_verification=wait_for_verification,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_id: Union[str, core.StringOut] = core.arg()

        domain_name: Union[str, core.StringOut] = core.arg()

        sub_domain: Union[List[SubDomain], core.ArrayOut[SubDomain]] = core.arg()

        wait_for_verification: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
