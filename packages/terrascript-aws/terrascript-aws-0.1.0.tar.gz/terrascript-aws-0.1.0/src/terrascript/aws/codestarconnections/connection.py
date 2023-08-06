from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_codestarconnections_connection", namespace="aws_codestarconnections")
class Connection(core.Resource):
    """
    The codestar connection ARN.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The codestar connection status. Possible values are `PENDING`, `AVAILABLE` and `ERROR`.
    """
    connection_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) The Amazon Resource Name (ARN) of the host associated with the connection. Conflicts with
    provider_type`
    """
    host_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    The codestar connection ARN.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The name of the connection to be created. The name must be unique in the calling AWS acco
    unt. Changing `name` will create a new resource.
    """
    name: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) The name of the external provider where your third-party code repository is configured. V
    alid values are `Bitbucket`, `GitHub` or `GitHubEnterpriseServer`. Changing `provider_type` will cre
    ate a new resource. Conflicts with `host_arn`
    """
    provider_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Map of key-value resource tags to associate with the resource. If configured with a provi
    der [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/lates
    t/docs#default_tags-configuration-block) present, tags with matching keys will overwrite those defin
    ed at the provider-level.
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
        host_arn: Optional[Union[str, core.StringOut]] = None,
        provider_type: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Connection.Args(
                name=name,
                host_arn=host_arn,
                provider_type=provider_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        host_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        provider_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
