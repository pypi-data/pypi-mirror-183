from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EndpointDetails(core.Schema):

    address_allocation_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    vpc_endpoint_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    vpc_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        address_allocation_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        vpc_endpoint_id: Optional[Union[str, core.StringOut]] = None,
        vpc_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EndpointDetails.Args(
                address_allocation_ids=address_allocation_ids,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address_allocation_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_endpoint_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class OnUpload(core.Schema):

    execution_role: Union[str, core.StringOut] = core.attr(str)

    workflow_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        execution_role: Union[str, core.StringOut],
        workflow_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OnUpload.Args(
                execution_role=execution_role,
                workflow_id=workflow_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        execution_role: Union[str, core.StringOut] = core.arg()

        workflow_id: Union[str, core.StringOut] = core.arg()


@core.schema
class WorkflowDetails(core.Schema):

    on_upload: Optional[OnUpload] = core.attr(OnUpload, default=None)

    def __init__(
        self,
        *,
        on_upload: Optional[OnUpload] = None,
    ):
        super().__init__(
            args=WorkflowDetails.Args(
                on_upload=on_upload,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        on_upload: Optional[OnUpload] = core.arg(default=None)


@core.resource(type="aws_transfer_server", namespace="aws_transfer")
class Server(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    directory_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    domain: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint_details: Optional[EndpointDetails] = core.attr(EndpointDetails, default=None)

    endpoint_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    force_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    function: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    host_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    host_key_fingerprint: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity_provider_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    invocation_role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    logging_role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    post_authentication_login_banner: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    pre_authentication_login_banner: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    protocols: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    security_policy_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    workflow_details: Optional[WorkflowDetails] = core.attr(WorkflowDetails, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate: Optional[Union[str, core.StringOut]] = None,
        directory_id: Optional[Union[str, core.StringOut]] = None,
        domain: Optional[Union[str, core.StringOut]] = None,
        endpoint_details: Optional[EndpointDetails] = None,
        endpoint_type: Optional[Union[str, core.StringOut]] = None,
        force_destroy: Optional[Union[bool, core.BoolOut]] = None,
        function: Optional[Union[str, core.StringOut]] = None,
        host_key: Optional[Union[str, core.StringOut]] = None,
        identity_provider_type: Optional[Union[str, core.StringOut]] = None,
        invocation_role: Optional[Union[str, core.StringOut]] = None,
        logging_role: Optional[Union[str, core.StringOut]] = None,
        post_authentication_login_banner: Optional[Union[str, core.StringOut]] = None,
        pre_authentication_login_banner: Optional[Union[str, core.StringOut]] = None,
        protocols: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        security_policy_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        url: Optional[Union[str, core.StringOut]] = None,
        workflow_details: Optional[WorkflowDetails] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Server.Args(
                certificate=certificate,
                directory_id=directory_id,
                domain=domain,
                endpoint_details=endpoint_details,
                endpoint_type=endpoint_type,
                force_destroy=force_destroy,
                function=function,
                host_key=host_key,
                identity_provider_type=identity_provider_type,
                invocation_role=invocation_role,
                logging_role=logging_role,
                post_authentication_login_banner=post_authentication_login_banner,
                pre_authentication_login_banner=pre_authentication_login_banner,
                protocols=protocols,
                security_policy_name=security_policy_name,
                tags=tags,
                tags_all=tags_all,
                url=url,
                workflow_details=workflow_details,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        directory_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        domain: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        endpoint_details: Optional[EndpointDetails] = core.arg(default=None)

        endpoint_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        force_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        function: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        host_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identity_provider_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        invocation_role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        logging_role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        post_authentication_login_banner: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        pre_authentication_login_banner: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        protocols: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        security_policy_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        workflow_details: Optional[WorkflowDetails] = core.arg(default=None)
