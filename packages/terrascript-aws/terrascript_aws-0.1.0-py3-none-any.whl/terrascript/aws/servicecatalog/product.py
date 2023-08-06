from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ProvisioningArtifactParameters(core.Schema):

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    disable_template_validation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    template_physical_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    template_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        description: Optional[Union[str, core.StringOut]] = None,
        disable_template_validation: Optional[Union[bool, core.BoolOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        template_physical_id: Optional[Union[str, core.StringOut]] = None,
        template_url: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ProvisioningArtifactParameters.Args(
                description=description,
                disable_template_validation=disable_template_validation,
                name=name,
                template_physical_id=template_physical_id,
                template_url=template_url,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        disable_template_validation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        template_physical_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        template_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_servicecatalog_product", namespace="aws_servicecatalog")
class Product(core.Resource):

    accept_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    distributor: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    has_default_path: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    owner: Union[str, core.StringOut] = core.attr(str)

    provisioning_artifact_parameters: ProvisioningArtifactParameters = core.attr(
        ProvisioningArtifactParameters
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    support_description: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    support_email: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    support_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        owner: Union[str, core.StringOut],
        provisioning_artifact_parameters: ProvisioningArtifactParameters,
        type: Union[str, core.StringOut],
        accept_language: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        distributor: Optional[Union[str, core.StringOut]] = None,
        support_description: Optional[Union[str, core.StringOut]] = None,
        support_email: Optional[Union[str, core.StringOut]] = None,
        support_url: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Product.Args(
                name=name,
                owner=owner,
                provisioning_artifact_parameters=provisioning_artifact_parameters,
                type=type,
                accept_language=accept_language,
                description=description,
                distributor=distributor,
                support_description=support_description,
                support_email=support_email,
                support_url=support_url,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        distributor: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        owner: Union[str, core.StringOut] = core.arg()

        provisioning_artifact_parameters: ProvisioningArtifactParameters = core.arg()

        support_description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        support_email: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        support_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Union[str, core.StringOut] = core.arg()
