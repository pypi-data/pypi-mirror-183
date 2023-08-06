from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=VpcConfig.Args(
                subnet_ids=subnet_ids,
                security_group_ids=security_group_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Iam(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=Iam.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class Sasl(core.Schema):

    iam: Iam = core.attr(Iam)

    def __init__(
        self,
        *,
        iam: Iam,
    ):
        super().__init__(
            args=Sasl.Args(
                iam=iam,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iam: Iam = core.arg()


@core.schema
class ClientAuthentication(core.Schema):

    sasl: Sasl = core.attr(Sasl)

    def __init__(
        self,
        *,
        sasl: Sasl,
    ):
        super().__init__(
            args=ClientAuthentication.Args(
                sasl=sasl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        sasl: Sasl = core.arg()


@core.resource(type="aws_msk_serverless_cluster", namespace="aws_managed_streaming_for_kafka")
class MskServerlessCluster(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    client_authentication: ClientAuthentication = core.attr(ClientAuthentication)

    cluster_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_config: Union[List[VpcConfig], core.ArrayOut[VpcConfig]] = core.attr(
        VpcConfig, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        client_authentication: ClientAuthentication,
        cluster_name: Union[str, core.StringOut],
        vpc_config: Union[List[VpcConfig], core.ArrayOut[VpcConfig]],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskServerlessCluster.Args(
                client_authentication=client_authentication,
                cluster_name=cluster_name,
                vpc_config=vpc_config,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        client_authentication: ClientAuthentication = core.arg()

        cluster_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_config: Union[List[VpcConfig], core.ArrayOut[VpcConfig]] = core.arg()
