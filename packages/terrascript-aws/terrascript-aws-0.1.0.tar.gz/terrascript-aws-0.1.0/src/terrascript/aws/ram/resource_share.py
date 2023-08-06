from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ram_resource_share", namespace="aws_ram")
class ResourceShare(core.Resource):
    """
    (Optional) Indicates whether principals outside your organization can be associated with a resource
    share.
    """

    allow_external_principals: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    """
    The Amazon Resource Name (ARN) of the resource share.
    """
    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the resource share.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The name of the resource share.
    """
    name: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) Specifies the Amazon Resource Names (ARNs) of the RAM permission to associate with the re
    source share. If you do not specify an ARN for the permission, RAM automatically attaches the defaul
    t version of the permission for each resource type. You can associate only one permission with each
    resource type included in the resource share.
    """
    permission_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A map of tags to assign to the resource share. If configured with a provider [`default_ta
    gs` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_t
    ags-configuration-block) present, tags with matching keys will overwrite those defined at the provid
    er-level.
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        allow_external_principals: Optional[Union[bool, core.BoolOut]] = None,
        permission_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceShare.Args(
                name=name,
                allow_external_principals=allow_external_principals,
                permission_arns=permission_arns,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allow_external_principals: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        permission_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
