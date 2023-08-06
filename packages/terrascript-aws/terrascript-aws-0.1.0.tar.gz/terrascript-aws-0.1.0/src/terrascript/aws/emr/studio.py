from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_emr_studio", namespace="aws_emr")
class Studio(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auth_mode: Union[str, core.StringOut] = core.attr(str)

    default_s3_location: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    engine_security_group_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    idp_auth_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    idp_relay_state_parameter_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    name: Union[str, core.StringOut] = core.attr(str)

    service_role: Union[str, core.StringOut] = core.attr(str)

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    url: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    workspace_security_group_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        auth_mode: Union[str, core.StringOut],
        default_s3_location: Union[str, core.StringOut],
        engine_security_group_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        service_role: Union[str, core.StringOut],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_id: Union[str, core.StringOut],
        workspace_security_group_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        idp_auth_url: Optional[Union[str, core.StringOut]] = None,
        idp_relay_state_parameter_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        user_role: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Studio.Args(
                auth_mode=auth_mode,
                default_s3_location=default_s3_location,
                engine_security_group_id=engine_security_group_id,
                name=name,
                service_role=service_role,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
                workspace_security_group_id=workspace_security_group_id,
                description=description,
                idp_auth_url=idp_auth_url,
                idp_relay_state_parameter_name=idp_relay_state_parameter_name,
                tags=tags,
                tags_all=tags_all,
                user_role=user_role,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auth_mode: Union[str, core.StringOut] = core.arg()

        default_s3_location: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine_security_group_id: Union[str, core.StringOut] = core.arg()

        idp_auth_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        idp_relay_state_parameter_name: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        service_role: Union[str, core.StringOut] = core.arg()

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_id: Union[str, core.StringOut] = core.arg()

        workspace_security_group_id: Union[str, core.StringOut] = core.arg()
