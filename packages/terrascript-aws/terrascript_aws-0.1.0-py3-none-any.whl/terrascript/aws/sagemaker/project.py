from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ProvisioningParameter(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ProvisioningParameter.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ServiceCatalogProvisioningDetails(core.Schema):

    path_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    product_id: Union[str, core.StringOut] = core.attr(str)

    provisioning_artifact_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    provisioning_parameter: Optional[
        Union[List[ProvisioningParameter], core.ArrayOut[ProvisioningParameter]]
    ] = core.attr(ProvisioningParameter, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        product_id: Union[str, core.StringOut],
        path_id: Optional[Union[str, core.StringOut]] = None,
        provisioning_artifact_id: Optional[Union[str, core.StringOut]] = None,
        provisioning_parameter: Optional[
            Union[List[ProvisioningParameter], core.ArrayOut[ProvisioningParameter]]
        ] = None,
    ):
        super().__init__(
            args=ServiceCatalogProvisioningDetails.Args(
                product_id=product_id,
                path_id=path_id,
                provisioning_artifact_id=provisioning_artifact_id,
                provisioning_parameter=provisioning_parameter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        path_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        product_id: Union[str, core.StringOut] = core.arg()

        provisioning_artifact_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        provisioning_parameter: Optional[
            Union[List[ProvisioningParameter], core.ArrayOut[ProvisioningParameter]]
        ] = core.arg(default=None)


@core.resource(type="aws_sagemaker_project", namespace="aws_sagemaker")
class Project(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    project_description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    project_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    project_name: Union[str, core.StringOut] = core.attr(str)

    service_catalog_provisioning_details: ServiceCatalogProvisioningDetails = core.attr(
        ServiceCatalogProvisioningDetails
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        project_name: Union[str, core.StringOut],
        service_catalog_provisioning_details: ServiceCatalogProvisioningDetails,
        project_description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Project.Args(
                project_name=project_name,
                service_catalog_provisioning_details=service_catalog_provisioning_details,
                project_description=project_description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        project_description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        project_name: Union[str, core.StringOut] = core.arg()

        service_catalog_provisioning_details: ServiceCatalogProvisioningDetails = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
