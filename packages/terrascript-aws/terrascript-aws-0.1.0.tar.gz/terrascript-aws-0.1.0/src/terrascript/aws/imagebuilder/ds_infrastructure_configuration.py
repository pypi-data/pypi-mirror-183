from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class InstanceMetadataOptions(core.Schema):

    http_put_response_hop_limit: Union[int, core.IntOut] = core.attr(int, computed=True)

    http_tokens: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        http_put_response_hop_limit: Union[int, core.IntOut],
        http_tokens: Union[str, core.StringOut],
    ):
        super().__init__(
            args=InstanceMetadataOptions.Args(
                http_put_response_hop_limit=http_put_response_hop_limit,
                http_tokens=http_tokens,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_put_response_hop_limit: Union[int, core.IntOut] = core.arg()

        http_tokens: Union[str, core.StringOut] = core.arg()


@core.schema
class S3Logs(core.Schema):

    s3_bucket_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    s3_key_prefix: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        s3_bucket_name: Union[str, core.StringOut],
        s3_key_prefix: Union[str, core.StringOut],
    ):
        super().__init__(
            args=S3Logs.Args(
                s3_bucket_name=s3_bucket_name,
                s3_key_prefix=s3_key_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_bucket_name: Union[str, core.StringOut] = core.arg()

        s3_key_prefix: Union[str, core.StringOut] = core.arg()


@core.schema
class Logging(core.Schema):

    s3_logs: Union[List[S3Logs], core.ArrayOut[S3Logs]] = core.attr(
        S3Logs, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        s3_logs: Union[List[S3Logs], core.ArrayOut[S3Logs]],
    ):
        super().__init__(
            args=Logging.Args(
                s3_logs=s3_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_logs: Union[List[S3Logs], core.ArrayOut[S3Logs]] = core.arg()


@core.data(type="aws_imagebuilder_infrastructure_configuration", namespace="aws_imagebuilder")
class DsInfrastructureConfiguration(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str)

    date_created: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_updated: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_metadata_options: Union[
        List[InstanceMetadataOptions], core.ArrayOut[InstanceMetadataOptions]
    ] = core.attr(InstanceMetadataOptions, computed=True, kind=core.Kind.array)

    instance_profile_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    key_pair: Union[str, core.StringOut] = core.attr(str, computed=True)

    logging: Union[List[Logging], core.ArrayOut[Logging]] = core.attr(
        Logging, computed=True, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    sns_topic_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    terminate_instance_on_failure: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Union[str, core.StringOut],
        resource_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsInfrastructureConfiguration.Args(
                arn=arn,
                resource_tags=resource_tags,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        resource_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
