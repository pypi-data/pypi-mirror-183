from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class SnapshotDeliveryProperties(core.Schema):

    delivery_frequency: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        delivery_frequency: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SnapshotDeliveryProperties.Args(
                delivery_frequency=delivery_frequency,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delivery_frequency: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_config_delivery_channel", namespace="aws_config")
class DeliveryChannel(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_bucket_name: Union[str, core.StringOut] = core.attr(str)

    s3_key_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    snapshot_delivery_properties: Optional[SnapshotDeliveryProperties] = core.attr(
        SnapshotDeliveryProperties, default=None
    )

    sns_topic_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        s3_bucket_name: Union[str, core.StringOut],
        name: Optional[Union[str, core.StringOut]] = None,
        s3_key_prefix: Optional[Union[str, core.StringOut]] = None,
        s3_kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        snapshot_delivery_properties: Optional[SnapshotDeliveryProperties] = None,
        sns_topic_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DeliveryChannel.Args(
                s3_bucket_name=s3_bucket_name,
                name=name,
                s3_key_prefix=s3_key_prefix,
                s3_kms_key_arn=s3_kms_key_arn,
                snapshot_delivery_properties=snapshot_delivery_properties,
                sns_topic_arn=sns_topic_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_bucket_name: Union[str, core.StringOut] = core.arg()

        s3_key_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        snapshot_delivery_properties: Optional[SnapshotDeliveryProperties] = core.arg(default=None)

        sns_topic_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)
