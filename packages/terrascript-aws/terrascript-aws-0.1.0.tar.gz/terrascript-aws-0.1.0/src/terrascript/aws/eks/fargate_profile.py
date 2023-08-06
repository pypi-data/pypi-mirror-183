from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Selector(core.Schema):

    labels: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    namespace: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        namespace: Union[str, core.StringOut],
        labels: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Selector.Args(
                namespace=namespace,
                labels=labels,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        labels: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        namespace: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_eks_fargate_profile", namespace="aws_eks")
class FargateProfile(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_name: Union[str, core.StringOut] = core.attr(str)

    fargate_profile_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    pod_execution_role_arn: Union[str, core.StringOut] = core.attr(str)

    selector: Union[List[Selector], core.ArrayOut[Selector]] = core.attr(
        Selector, kind=core.Kind.array
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_name: Union[str, core.StringOut],
        fargate_profile_name: Union[str, core.StringOut],
        pod_execution_role_arn: Union[str, core.StringOut],
        selector: Union[List[Selector], core.ArrayOut[Selector]],
        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FargateProfile.Args(
                cluster_name=cluster_name,
                fargate_profile_name=fargate_profile_name,
                pod_execution_role_arn=pod_execution_role_arn,
                selector=selector,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_name: Union[str, core.StringOut] = core.arg()

        fargate_profile_name: Union[str, core.StringOut] = core.arg()

        pod_execution_role_arn: Union[str, core.StringOut] = core.arg()

        selector: Union[List[Selector], core.ArrayOut[Selector]] = core.arg()

        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
