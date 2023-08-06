from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=VpcConfig.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class DomainJoinInfo(core.Schema):

    directory_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    organizational_unit_distinguished_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    def __init__(
        self,
        *,
        directory_name: Optional[Union[str, core.StringOut]] = None,
        organizational_unit_distinguished_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DomainJoinInfo.Args(
                directory_name=directory_name,
                organizational_unit_distinguished_name=organizational_unit_distinguished_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        directory_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        organizational_unit_distinguished_name: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )


@core.schema
class AccessEndpoint(core.Schema):

    endpoint_type: Union[str, core.StringOut] = core.attr(str)

    vpce_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        endpoint_type: Union[str, core.StringOut],
        vpce_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AccessEndpoint.Args(
                endpoint_type=endpoint_type,
                vpce_id=vpce_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_type: Union[str, core.StringOut] = core.arg()

        vpce_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_appstream_image_builder", namespace="aws_appstream")
class ImageBuilder(core.Resource):

    access_endpoint: Optional[
        Union[List[AccessEndpoint], core.ArrayOut[AccessEndpoint]]
    ] = core.attr(AccessEndpoint, default=None, kind=core.Kind.array)

    appstream_agent_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    display_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    domain_join_info: Optional[DomainJoinInfo] = core.attr(
        DomainJoinInfo, default=None, computed=True
    )

    enable_default_internet_access: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    iam_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    image_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    instance_type: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_config: Optional[VpcConfig] = core.attr(VpcConfig, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        access_endpoint: Optional[
            Union[List[AccessEndpoint], core.ArrayOut[AccessEndpoint]]
        ] = None,
        appstream_agent_version: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        display_name: Optional[Union[str, core.StringOut]] = None,
        domain_join_info: Optional[DomainJoinInfo] = None,
        enable_default_internet_access: Optional[Union[bool, core.BoolOut]] = None,
        iam_role_arn: Optional[Union[str, core.StringOut]] = None,
        image_arn: Optional[Union[str, core.StringOut]] = None,
        image_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_config: Optional[VpcConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ImageBuilder.Args(
                instance_type=instance_type,
                name=name,
                access_endpoint=access_endpoint,
                appstream_agent_version=appstream_agent_version,
                description=description,
                display_name=display_name,
                domain_join_info=domain_join_info,
                enable_default_internet_access=enable_default_internet_access,
                iam_role_arn=iam_role_arn,
                image_arn=image_arn,
                image_name=image_name,
                tags=tags,
                tags_all=tags_all,
                vpc_config=vpc_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_endpoint: Optional[
            Union[List[AccessEndpoint], core.ArrayOut[AccessEndpoint]]
        ] = core.arg(default=None)

        appstream_agent_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        display_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        domain_join_info: Optional[DomainJoinInfo] = core.arg(default=None)

        enable_default_internet_access: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        iam_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_type: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_config: Optional[VpcConfig] = core.arg(default=None)
