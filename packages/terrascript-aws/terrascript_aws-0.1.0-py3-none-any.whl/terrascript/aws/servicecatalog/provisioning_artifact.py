from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_servicecatalog_provisioning_artifact", namespace="aws_servicecatalog")
class ProvisioningArtifact(core.Resource):

    accept_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    active: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    disable_template_validation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    guidance: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    product_id: Union[str, core.StringOut] = core.attr(str)

    template_physical_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    template_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        product_id: Union[str, core.StringOut],
        accept_language: Optional[Union[str, core.StringOut]] = None,
        active: Optional[Union[bool, core.BoolOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        disable_template_validation: Optional[Union[bool, core.BoolOut]] = None,
        guidance: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        template_physical_id: Optional[Union[str, core.StringOut]] = None,
        template_url: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProvisioningArtifact.Args(
                product_id=product_id,
                accept_language=accept_language,
                active=active,
                description=description,
                disable_template_validation=disable_template_validation,
                guidance=guidance,
                name=name,
                template_physical_id=template_physical_id,
                template_url=template_url,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        active: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        disable_template_validation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        guidance: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        product_id: Union[str, core.StringOut] = core.arg()

        template_physical_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        template_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
