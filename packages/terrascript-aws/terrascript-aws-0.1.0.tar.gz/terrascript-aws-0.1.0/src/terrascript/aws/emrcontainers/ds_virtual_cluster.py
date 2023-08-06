from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EksInfo(core.Schema):

    namespace: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        namespace: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EksInfo.Args(
                namespace=namespace,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        namespace: Union[str, core.StringOut] = core.arg()


@core.schema
class Info(core.Schema):

    eks_info: Union[List[EksInfo], core.ArrayOut[EksInfo]] = core.attr(
        EksInfo, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        eks_info: Union[List[EksInfo], core.ArrayOut[EksInfo]],
    ):
        super().__init__(
            args=Info.Args(
                eks_info=eks_info,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eks_info: Union[List[EksInfo], core.ArrayOut[EksInfo]] = core.arg()


@core.schema
class ContainerProvider(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    info: Union[List[Info], core.ArrayOut[Info]] = core.attr(
        Info, computed=True, kind=core.Kind.array
    )

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        info: Union[List[Info], core.ArrayOut[Info]],
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

        info: Union[List[Info], core.ArrayOut[Info]] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_emrcontainers_virtual_cluster", namespace="aws_emrcontainers")
class DsVirtualCluster(core.Data):
    """
    The Amazon Resource Name (ARN) of the cluster.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    Nested attribute containing information about the underlying container provider (EKS cluster) for yo
    ur EMR Containers cluster.
    """
    container_provider: Union[
        List[ContainerProvider], core.ArrayOut[ContainerProvider]
    ] = core.attr(ContainerProvider, computed=True, kind=core.Kind.array)

    """
    The Unix epoch time stamp in seconds for when the cluster was created.
    """
    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The ID of the cluster.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The name of the cluster.
    """
    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The status of the EKS cluster. One of `RUNNING`, `TERMINATING`, `TERMINATED`, `ARRESTED`.
    """
    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    Key-value mapping of resource tags.
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) The ID of the cluster.
    """
    virtual_cluster_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        virtual_cluster_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsVirtualCluster.Args(
                virtual_cluster_id=virtual_cluster_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        virtual_cluster_id: Union[str, core.StringOut] = core.arg()
