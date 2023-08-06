from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cognito_user", namespace="aws_cognito")
class User(core.Resource):

    attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    client_metadata: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    creation_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    desired_delivery_mediums: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    force_alias_creation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    message_action: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mfa_setting_list: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    preferred_mfa_setting: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    sub: Union[str, core.StringOut] = core.attr(str, computed=True)

    temporary_password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_pool_id: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    validation_data: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        user_pool_id: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
        attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        client_metadata: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        desired_delivery_mediums: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        force_alias_creation: Optional[Union[bool, core.BoolOut]] = None,
        message_action: Optional[Union[str, core.StringOut]] = None,
        password: Optional[Union[str, core.StringOut]] = None,
        temporary_password: Optional[Union[str, core.StringOut]] = None,
        validation_data: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                user_pool_id=user_pool_id,
                username=username,
                attributes=attributes,
                client_metadata=client_metadata,
                desired_delivery_mediums=desired_delivery_mediums,
                enabled=enabled,
                force_alias_creation=force_alias_creation,
                message_action=message_action,
                password=password,
                temporary_password=temporary_password,
                validation_data=validation_data,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attributes: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        client_metadata: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        desired_delivery_mediums: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        force_alias_creation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        message_action: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        temporary_password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_pool_id: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()

        validation_data: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
