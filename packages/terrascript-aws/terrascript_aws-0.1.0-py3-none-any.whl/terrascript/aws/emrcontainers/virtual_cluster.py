from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EksInfo(core.Schema):

    namespace: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        namespace: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EksInfo.Args(
                namespace=namespace,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        namespace: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Info(core.Schema):

    eks_info: EksInfo = core.attr(EksInfo)

    def __init__(
        self,
        *,
        eks_info: EksInfo,
    ):
        super().__init__(
            args=Info.Args(
                eks_info=eks_info,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eks_info: EksInfo = core.arg()


@core.schema
class ContainerProvider(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str)

    info: Info = core.attr(Info)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        info: Info,
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ContainerProvider.Args(
                id=id,
                info=info,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        info: Info = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_emrcontainers_virtual_cluster", namespace="aws_emrcontainers")
class VirtualCluster(core.Resource):
    """
    ARN of the cluster.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) Configuration block for the container provider associated with your cluster.
    """
    container_provider: ContainerProvider = core.attr(ContainerProvider)

    """
    The name of the container provider that is running your EMR Containers cluster
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) Key-value mapping of resource tags. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        container_provider: ContainerProvider,
        name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VirtualCluster.Args(
                container_provider=container_provider,
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        container_provider: ContainerProvider = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
