from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class PreProvisioningHook(core.Schema):

    payload_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    target_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        target_arn: Union[str, core.StringOut],
        payload_version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=PreProvisioningHook.Args(
                target_arn=target_arn,
                payload_version=payload_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        payload_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_iot_provisioning_template", namespace="aws_iot")
class ProvisioningTemplate(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_version_id: Union[int, core.IntOut] = core.attr(int, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    pre_provisioning_hook: Optional[PreProvisioningHook] = core.attr(
        PreProvisioningHook, default=None
    )

    provisioning_role_arn: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    template_body: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        provisioning_role_arn: Union[str, core.StringOut],
        template_body: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        pre_provisioning_hook: Optional[PreProvisioningHook] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProvisioningTemplate.Args(
                name=name,
                provisioning_role_arn=provisioning_role_arn,
                template_body=template_body,
                description=description,
                enabled=enabled,
                pre_provisioning_hook=pre_provisioning_hook,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        pre_provisioning_hook: Optional[PreProvisioningHook] = core.arg(default=None)

        provisioning_role_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        template_body: Union[str, core.StringOut] = core.arg()
