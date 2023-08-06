from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Idp(core.Schema):

    entity_id: Union[str, core.StringOut] = core.attr(str)

    metadata_content: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        entity_id: Union[str, core.StringOut],
        metadata_content: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Idp.Args(
                entity_id=entity_id,
                metadata_content=metadata_content,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        entity_id: Union[str, core.StringOut] = core.arg()

        metadata_content: Union[str, core.StringOut] = core.arg()


@core.schema
class SamlOptions(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    idp: Optional[Idp] = core.attr(Idp, default=None)

    master_backend_role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    master_user_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    roles_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    session_timeout_minutes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    subject_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        idp: Optional[Idp] = None,
        master_backend_role: Optional[Union[str, core.StringOut]] = None,
        master_user_name: Optional[Union[str, core.StringOut]] = None,
        roles_key: Optional[Union[str, core.StringOut]] = None,
        session_timeout_minutes: Optional[Union[int, core.IntOut]] = None,
        subject_key: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SamlOptions.Args(
                enabled=enabled,
                idp=idp,
                master_backend_role=master_backend_role,
                master_user_name=master_user_name,
                roles_key=roles_key,
                session_timeout_minutes=session_timeout_minutes,
                subject_key=subject_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        idp: Optional[Idp] = core.arg(default=None)

        master_backend_role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        master_user_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        roles_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        session_timeout_minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        subject_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_elasticsearch_domain_saml_options", namespace="aws_elasticsearch")
class DomainSamlOptions(core.Resource):

    domain_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    saml_options: Optional[SamlOptions] = core.attr(SamlOptions, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: Union[str, core.StringOut],
        saml_options: Optional[SamlOptions] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainSamlOptions.Args(
                domain_name=domain_name,
                saml_options=saml_options,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain_name: Union[str, core.StringOut] = core.arg()

        saml_options: Optional[SamlOptions] = core.arg(default=None)
