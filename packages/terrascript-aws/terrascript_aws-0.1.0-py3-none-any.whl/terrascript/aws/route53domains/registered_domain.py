from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class TechContact(core.Schema):

    address_line_1: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    address_line_2: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    city: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    contact_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    country_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    email: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    extra_params: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    fax: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    first_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    last_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    organization_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    phone_number: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    zip_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        address_line_1: Optional[Union[str, core.StringOut]] = None,
        address_line_2: Optional[Union[str, core.StringOut]] = None,
        city: Optional[Union[str, core.StringOut]] = None,
        contact_type: Optional[Union[str, core.StringOut]] = None,
        country_code: Optional[Union[str, core.StringOut]] = None,
        email: Optional[Union[str, core.StringOut]] = None,
        extra_params: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        fax: Optional[Union[str, core.StringOut]] = None,
        first_name: Optional[Union[str, core.StringOut]] = None,
        last_name: Optional[Union[str, core.StringOut]] = None,
        organization_name: Optional[Union[str, core.StringOut]] = None,
        phone_number: Optional[Union[str, core.StringOut]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
        zip_code: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=TechContact.Args(
                address_line_1=address_line_1,
                address_line_2=address_line_2,
                city=city,
                contact_type=contact_type,
                country_code=country_code,
                email=email,
                extra_params=extra_params,
                fax=fax,
                first_name=first_name,
                last_name=last_name,
                organization_name=organization_name,
                phone_number=phone_number,
                state=state,
                zip_code=zip_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address_line_1: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        address_line_2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        city: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        contact_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        country_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        email: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        extra_params: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        fax: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        first_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        last_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        organization_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        phone_number: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        zip_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RegistrantContact(core.Schema):

    address_line_1: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    address_line_2: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    city: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    contact_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    country_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    email: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    extra_params: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    fax: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    first_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    last_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    organization_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    phone_number: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    zip_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        address_line_1: Optional[Union[str, core.StringOut]] = None,
        address_line_2: Optional[Union[str, core.StringOut]] = None,
        city: Optional[Union[str, core.StringOut]] = None,
        contact_type: Optional[Union[str, core.StringOut]] = None,
        country_code: Optional[Union[str, core.StringOut]] = None,
        email: Optional[Union[str, core.StringOut]] = None,
        extra_params: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        fax: Optional[Union[str, core.StringOut]] = None,
        first_name: Optional[Union[str, core.StringOut]] = None,
        last_name: Optional[Union[str, core.StringOut]] = None,
        organization_name: Optional[Union[str, core.StringOut]] = None,
        phone_number: Optional[Union[str, core.StringOut]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
        zip_code: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RegistrantContact.Args(
                address_line_1=address_line_1,
                address_line_2=address_line_2,
                city=city,
                contact_type=contact_type,
                country_code=country_code,
                email=email,
                extra_params=extra_params,
                fax=fax,
                first_name=first_name,
                last_name=last_name,
                organization_name=organization_name,
                phone_number=phone_number,
                state=state,
                zip_code=zip_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address_line_1: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        address_line_2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        city: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        contact_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        country_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        email: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        extra_params: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        fax: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        first_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        last_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        organization_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        phone_number: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        zip_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AdminContact(core.Schema):

    address_line_1: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    address_line_2: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    city: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    contact_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    country_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    email: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    extra_params: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    fax: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    first_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    last_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    organization_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    phone_number: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    zip_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        address_line_1: Optional[Union[str, core.StringOut]] = None,
        address_line_2: Optional[Union[str, core.StringOut]] = None,
        city: Optional[Union[str, core.StringOut]] = None,
        contact_type: Optional[Union[str, core.StringOut]] = None,
        country_code: Optional[Union[str, core.StringOut]] = None,
        email: Optional[Union[str, core.StringOut]] = None,
        extra_params: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        fax: Optional[Union[str, core.StringOut]] = None,
        first_name: Optional[Union[str, core.StringOut]] = None,
        last_name: Optional[Union[str, core.StringOut]] = None,
        organization_name: Optional[Union[str, core.StringOut]] = None,
        phone_number: Optional[Union[str, core.StringOut]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
        zip_code: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AdminContact.Args(
                address_line_1=address_line_1,
                address_line_2=address_line_2,
                city=city,
                contact_type=contact_type,
                country_code=country_code,
                email=email,
                extra_params=extra_params,
                fax=fax,
                first_name=first_name,
                last_name=last_name,
                organization_name=organization_name,
                phone_number=phone_number,
                state=state,
                zip_code=zip_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address_line_1: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        address_line_2: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        city: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        contact_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        country_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        email: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        extra_params: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        fax: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        first_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        last_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        organization_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        phone_number: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        zip_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class NameServer(core.Schema):

    glue_ips: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        glue_ips: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=NameServer.Args(
                name=name,
                glue_ips=glue_ips,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        glue_ips: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_route53domains_registered_domain", namespace="aws_route53domains")
class RegisteredDomain(core.Resource):

    abuse_contact_email: Union[str, core.StringOut] = core.attr(str, computed=True)

    abuse_contact_phone: Union[str, core.StringOut] = core.attr(str, computed=True)

    admin_contact: Optional[AdminContact] = core.attr(AdminContact, default=None, computed=True)

    admin_privacy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    auto_renew: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    creation_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    expiration_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name_server: Optional[Union[List[NameServer], core.ArrayOut[NameServer]]] = core.attr(
        NameServer, default=None, computed=True, kind=core.Kind.array
    )

    registrant_contact: Optional[RegistrantContact] = core.attr(
        RegistrantContact, default=None, computed=True
    )

    registrant_privacy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    registrar_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    registrar_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    reseller: Union[str, core.StringOut] = core.attr(str, computed=True)

    status_list: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tech_contact: Optional[TechContact] = core.attr(TechContact, default=None, computed=True)

    tech_privacy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    transfer_lock: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    whois_server: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: Union[str, core.StringOut],
        admin_contact: Optional[AdminContact] = None,
        admin_privacy: Optional[Union[bool, core.BoolOut]] = None,
        auto_renew: Optional[Union[bool, core.BoolOut]] = None,
        name_server: Optional[Union[List[NameServer], core.ArrayOut[NameServer]]] = None,
        registrant_contact: Optional[RegistrantContact] = None,
        registrant_privacy: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tech_contact: Optional[TechContact] = None,
        tech_privacy: Optional[Union[bool, core.BoolOut]] = None,
        transfer_lock: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RegisteredDomain.Args(
                domain_name=domain_name,
                admin_contact=admin_contact,
                admin_privacy=admin_privacy,
                auto_renew=auto_renew,
                name_server=name_server,
                registrant_contact=registrant_contact,
                registrant_privacy=registrant_privacy,
                tags=tags,
                tags_all=tags_all,
                tech_contact=tech_contact,
                tech_privacy=tech_privacy,
                transfer_lock=transfer_lock,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        admin_contact: Optional[AdminContact] = core.arg(default=None)

        admin_privacy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        auto_renew: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        domain_name: Union[str, core.StringOut] = core.arg()

        name_server: Optional[Union[List[NameServer], core.ArrayOut[NameServer]]] = core.arg(
            default=None
        )

        registrant_contact: Optional[RegistrantContact] = core.arg(default=None)

        registrant_privacy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        tech_contact: Optional[TechContact] = core.arg(default=None)

        tech_privacy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        transfer_lock: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
