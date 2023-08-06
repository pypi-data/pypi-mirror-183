from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Ec2Config(core.Schema):

    security_group_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    subnet_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        security_group_arns: Union[List[str], core.ArrayOut[core.StringOut]],
        subnet_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Ec2Config.Args(
                security_group_arns=security_group_arns,
                subnet_arn=subnet_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnet_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_datasync_location_efs", namespace="aws_datasync")
class LocationEfs(core.Resource):

    access_point_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    ec2_config: Ec2Config = core.attr(Ec2Config)

    efs_file_system_arn: Union[str, core.StringOut] = core.attr(str)

    file_system_access_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    in_transit_encryption: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    subdirectory: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    uri: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        ec2_config: Ec2Config,
        efs_file_system_arn: Union[str, core.StringOut],
        access_point_arn: Optional[Union[str, core.StringOut]] = None,
        file_system_access_role_arn: Optional[Union[str, core.StringOut]] = None,
        in_transit_encryption: Optional[Union[str, core.StringOut]] = None,
        subdirectory: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LocationEfs.Args(
                ec2_config=ec2_config,
                efs_file_system_arn=efs_file_system_arn,
                access_point_arn=access_point_arn,
                file_system_access_role_arn=file_system_access_role_arn,
                in_transit_encryption=in_transit_encryption,
                subdirectory=subdirectory,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_point_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ec2_config: Ec2Config = core.arg()

        efs_file_system_arn: Union[str, core.StringOut] = core.arg()

        file_system_access_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        in_transit_encryption: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subdirectory: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
