from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Vpc(core.Schema):

    security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        security_groups: Union[List[str], core.ArrayOut[core.StringOut]],
        subnets: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Vpc.Args(
                security_groups=security_groups,
                subnets=subnets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class ApacheKafkaCluster(core.Schema):

    bootstrap_servers: Union[str, core.StringOut] = core.attr(str)

    vpc: Vpc = core.attr(Vpc)

    def __init__(
        self,
        *,
        bootstrap_servers: Union[str, core.StringOut],
        vpc: Vpc,
    ):
        super().__init__(
            args=ApacheKafkaCluster.Args(
                bootstrap_servers=bootstrap_servers,
                vpc=vpc,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bootstrap_servers: Union[str, core.StringOut] = core.arg()

        vpc: Vpc = core.arg()


@core.schema
class KafkaCluster(core.Schema):

    apache_kafka_cluster: ApacheKafkaCluster = core.attr(ApacheKafkaCluster)

    def __init__(
        self,
        *,
        apache_kafka_cluster: ApacheKafkaCluster,
    ):
        super().__init__(
            args=KafkaCluster.Args(
                apache_kafka_cluster=apache_kafka_cluster,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        apache_kafka_cluster: ApacheKafkaCluster = core.arg()


@core.schema
class KafkaClusterClientAuthentication(core.Schema):

    authentication_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        authentication_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=KafkaClusterClientAuthentication.Args(
                authentication_type=authentication_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ScaleOutPolicy(core.Schema):

    cpu_utilization_percentage: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    def __init__(
        self,
        *,
        cpu_utilization_percentage: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ScaleOutPolicy.Args(
                cpu_utilization_percentage=cpu_utilization_percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu_utilization_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class ScaleInPolicy(core.Schema):

    cpu_utilization_percentage: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    def __init__(
        self,
        *,
        cpu_utilization_percentage: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ScaleInPolicy.Args(
                cpu_utilization_percentage=cpu_utilization_percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu_utilization_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class Autoscaling(core.Schema):

    max_worker_count: Union[int, core.IntOut] = core.attr(int)

    mcu_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min_worker_count: Union[int, core.IntOut] = core.attr(int)

    scale_in_policy: Optional[ScaleInPolicy] = core.attr(ScaleInPolicy, default=None, computed=True)

    scale_out_policy: Optional[ScaleOutPolicy] = core.attr(
        ScaleOutPolicy, default=None, computed=True
    )

    def __init__(
        self,
        *,
        max_worker_count: Union[int, core.IntOut],
        min_worker_count: Union[int, core.IntOut],
        mcu_count: Optional[Union[int, core.IntOut]] = None,
        scale_in_policy: Optional[ScaleInPolicy] = None,
        scale_out_policy: Optional[ScaleOutPolicy] = None,
    ):
        super().__init__(
            args=Autoscaling.Args(
                max_worker_count=max_worker_count,
                min_worker_count=min_worker_count,
                mcu_count=mcu_count,
                scale_in_policy=scale_in_policy,
                scale_out_policy=scale_out_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_worker_count: Union[int, core.IntOut] = core.arg()

        mcu_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min_worker_count: Union[int, core.IntOut] = core.arg()

        scale_in_policy: Optional[ScaleInPolicy] = core.arg(default=None)

        scale_out_policy: Optional[ScaleOutPolicy] = core.arg(default=None)


@core.schema
class ProvisionedCapacity(core.Schema):

    mcu_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    worker_count: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        worker_count: Union[int, core.IntOut],
        mcu_count: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ProvisionedCapacity.Args(
                worker_count=worker_count,
                mcu_count=mcu_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mcu_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        worker_count: Union[int, core.IntOut] = core.arg()


@core.schema
class Capacity(core.Schema):

    autoscaling: Optional[Autoscaling] = core.attr(Autoscaling, default=None)

    provisioned_capacity: Optional[ProvisionedCapacity] = core.attr(
        ProvisionedCapacity, default=None
    )

    def __init__(
        self,
        *,
        autoscaling: Optional[Autoscaling] = None,
        provisioned_capacity: Optional[ProvisionedCapacity] = None,
    ):
        super().__init__(
            args=Capacity.Args(
                autoscaling=autoscaling,
                provisioned_capacity=provisioned_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        autoscaling: Optional[Autoscaling] = core.arg(default=None)

        provisioned_capacity: Optional[ProvisionedCapacity] = core.arg(default=None)


@core.schema
class KafkaClusterEncryptionInTransit(core.Schema):

    encryption_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        encryption_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=KafkaClusterEncryptionInTransit.Args(
                encryption_type=encryption_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class WorkerConfiguration(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str)

    revision: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        revision: Union[int, core.IntOut],
    ):
        super().__init__(
            args=WorkerConfiguration.Args(
                arn=arn,
                revision=revision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        revision: Union[int, core.IntOut] = core.arg()


@core.schema
class CustomPlugin(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str)

    revision: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        revision: Union[int, core.IntOut],
    ):
        super().__init__(
            args=CustomPlugin.Args(
                arn=arn,
                revision=revision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        revision: Union[int, core.IntOut] = core.arg()


@core.schema
class Plugin(core.Schema):

    custom_plugin: CustomPlugin = core.attr(CustomPlugin)

    def __init__(
        self,
        *,
        custom_plugin: CustomPlugin,
    ):
        super().__init__(
            args=Plugin.Args(
                custom_plugin=custom_plugin,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_plugin: CustomPlugin = core.arg()


@core.schema
class CloudwatchLogs(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    log_group: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        log_group: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CloudwatchLogs.Args(
                enabled=enabled,
                log_group=log_group,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        log_group: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Firehose(core.Schema):

    delivery_stream: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        delivery_stream: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Firehose.Args(
                enabled=enabled,
                delivery_stream=delivery_stream,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delivery_stream: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class S3(core.Schema):

    bucket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        bucket: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3.Args(
                enabled=enabled,
                bucket=bucket,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Union[bool, core.BoolOut] = core.arg()

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class WorkerLogDelivery(core.Schema):

    cloudwatch_logs: Optional[CloudwatchLogs] = core.attr(CloudwatchLogs, default=None)

    firehose: Optional[Firehose] = core.attr(Firehose, default=None)

    s3: Optional[S3] = core.attr(S3, default=None)

    def __init__(
        self,
        *,
        cloudwatch_logs: Optional[CloudwatchLogs] = None,
        firehose: Optional[Firehose] = None,
        s3: Optional[S3] = None,
    ):
        super().__init__(
            args=WorkerLogDelivery.Args(
                cloudwatch_logs=cloudwatch_logs,
                firehose=firehose,
                s3=s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_logs: Optional[CloudwatchLogs] = core.arg(default=None)

        firehose: Optional[Firehose] = core.arg(default=None)

        s3: Optional[S3] = core.arg(default=None)


@core.schema
class LogDelivery(core.Schema):

    worker_log_delivery: WorkerLogDelivery = core.attr(WorkerLogDelivery)

    def __init__(
        self,
        *,
        worker_log_delivery: WorkerLogDelivery,
    ):
        super().__init__(
            args=LogDelivery.Args(
                worker_log_delivery=worker_log_delivery,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        worker_log_delivery: WorkerLogDelivery = core.arg()


@core.resource(type="aws_mskconnect_connector", namespace="aws_managed_streaming_for_kafka_connect")
class MskconnectConnector(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    capacity: Capacity = core.attr(Capacity)

    connector_configuration: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.map
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kafka_cluster: KafkaCluster = core.attr(KafkaCluster)

    kafka_cluster_client_authentication: KafkaClusterClientAuthentication = core.attr(
        KafkaClusterClientAuthentication
    )

    kafka_cluster_encryption_in_transit: KafkaClusterEncryptionInTransit = core.attr(
        KafkaClusterEncryptionInTransit
    )

    kafkaconnect_version: Union[str, core.StringOut] = core.attr(str)

    log_delivery: Optional[LogDelivery] = core.attr(LogDelivery, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    plugin: Union[List[Plugin], core.ArrayOut[Plugin]] = core.attr(Plugin, kind=core.Kind.array)

    service_execution_role_arn: Union[str, core.StringOut] = core.attr(str)

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    worker_configuration: Optional[WorkerConfiguration] = core.attr(
        WorkerConfiguration, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        capacity: Capacity,
        connector_configuration: Union[Dict[str, str], core.MapOut[core.StringOut]],
        kafka_cluster: KafkaCluster,
        kafka_cluster_client_authentication: KafkaClusterClientAuthentication,
        kafka_cluster_encryption_in_transit: KafkaClusterEncryptionInTransit,
        kafkaconnect_version: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        plugin: Union[List[Plugin], core.ArrayOut[Plugin]],
        service_execution_role_arn: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        log_delivery: Optional[LogDelivery] = None,
        worker_configuration: Optional[WorkerConfiguration] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskconnectConnector.Args(
                capacity=capacity,
                connector_configuration=connector_configuration,
                kafka_cluster=kafka_cluster,
                kafka_cluster_client_authentication=kafka_cluster_client_authentication,
                kafka_cluster_encryption_in_transit=kafka_cluster_encryption_in_transit,
                kafkaconnect_version=kafkaconnect_version,
                name=name,
                plugin=plugin,
                service_execution_role_arn=service_execution_role_arn,
                description=description,
                log_delivery=log_delivery,
                worker_configuration=worker_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity: Capacity = core.arg()

        connector_configuration: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kafka_cluster: KafkaCluster = core.arg()

        kafka_cluster_client_authentication: KafkaClusterClientAuthentication = core.arg()

        kafka_cluster_encryption_in_transit: KafkaClusterEncryptionInTransit = core.arg()

        kafkaconnect_version: Union[str, core.StringOut] = core.arg()

        log_delivery: Optional[LogDelivery] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        plugin: Union[List[Plugin], core.ArrayOut[Plugin]] = core.arg()

        service_execution_role_arn: Union[str, core.StringOut] = core.arg()

        worker_configuration: Optional[WorkerConfiguration] = core.arg(default=None)
