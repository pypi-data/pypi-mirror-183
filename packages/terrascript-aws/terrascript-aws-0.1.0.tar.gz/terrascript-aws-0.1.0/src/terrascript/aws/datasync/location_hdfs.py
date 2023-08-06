from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class NameNode(core.Schema):

    hostname: Union[str, core.StringOut] = core.attr(str)

    port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        hostname: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=NameNode.Args(
                hostname=hostname,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hostname: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class QopConfiguration(core.Schema):

    data_transfer_protection: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rpc_protection: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        data_transfer_protection: Optional[Union[str, core.StringOut]] = None,
        rpc_protection: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=QopConfiguration.Args(
                data_transfer_protection=data_transfer_protection,
                rpc_protection=rpc_protection,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_transfer_protection: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rpc_protection: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_datasync_location_hdfs", namespace="aws_datasync")
class LocationHdfs(core.Resource):

    agent_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authentication_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    block_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kerberos_keytab: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kerberos_krb5_conf: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kerberos_principal: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kms_key_provider_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name_node: Union[List[NameNode], core.ArrayOut[NameNode]] = core.attr(
        NameNode, kind=core.Kind.array
    )

    qop_configuration: Optional[QopConfiguration] = core.attr(QopConfiguration, default=None)

    replication_factor: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    simple_user: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        agent_arns: Union[List[str], core.ArrayOut[core.StringOut]],
        name_node: Union[List[NameNode], core.ArrayOut[NameNode]],
        authentication_type: Optional[Union[str, core.StringOut]] = None,
        block_size: Optional[Union[int, core.IntOut]] = None,
        kerberos_keytab: Optional[Union[str, core.StringOut]] = None,
        kerberos_krb5_conf: Optional[Union[str, core.StringOut]] = None,
        kerberos_principal: Optional[Union[str, core.StringOut]] = None,
        kms_key_provider_uri: Optional[Union[str, core.StringOut]] = None,
        qop_configuration: Optional[QopConfiguration] = None,
        replication_factor: Optional[Union[int, core.IntOut]] = None,
        simple_user: Optional[Union[str, core.StringOut]] = None,
        subdirectory: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LocationHdfs.Args(
                agent_arns=agent_arns,
                name_node=name_node,
                authentication_type=authentication_type,
                block_size=block_size,
                kerberos_keytab=kerberos_keytab,
                kerberos_krb5_conf=kerberos_krb5_conf,
                kerberos_principal=kerberos_principal,
                kms_key_provider_uri=kms_key_provider_uri,
                qop_configuration=qop_configuration,
                replication_factor=replication_factor,
                simple_user=simple_user,
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
        agent_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        authentication_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        block_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        kerberos_keytab: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kerberos_krb5_conf: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kerberos_principal: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_provider_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_node: Union[List[NameNode], core.ArrayOut[NameNode]] = core.arg()

        qop_configuration: Optional[QopConfiguration] = core.arg(default=None)

        replication_factor: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        simple_user: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subdirectory: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
