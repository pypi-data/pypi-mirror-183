from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class InstanceMetadataOptions(core.Schema):

    http_put_response_hop_limit: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    http_tokens: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        http_put_response_hop_limit: Optional[Union[int, core.IntOut]] = None,
        http_tokens: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InstanceMetadataOptions.Args(
                http_put_response_hop_limit=http_put_response_hop_limit,
                http_tokens=http_tokens,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_put_response_hop_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        http_tokens: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class S3Logs(core.Schema):

    s3_bucket_name: Union[str, core.StringOut] = core.attr(str)

    s3_key_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_bucket_name: Union[str, core.StringOut],
        s3_key_prefix: Optional[Union[str, core.StringOut]] = None,
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

        s3_key_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Logging(core.Schema):

    s3_logs: S3Logs = core.attr(S3Logs)

    def __init__(
        self,
        *,
        s3_logs: S3Logs,
    ):
        super().__init__(
            args=Logging.Args(
                s3_logs=s3_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_logs: S3Logs = core.arg()


@core.resource(type="aws_imagebuilder_infrastructure_configuration", namespace="aws_imagebuilder")
class InfrastructureConfiguration(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_created: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_updated: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_metadata_options: Optional[InstanceMetadataOptions] = core.attr(
        InstanceMetadataOptions, default=None
    )

    instance_profile_name: Union[str, core.StringOut] = core.attr(str)

    instance_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    key_pair: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    logging: Optional[Logging] = core.attr(Logging, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    resource_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    sns_topic_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    terminate_instance_on_failure: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        instance_profile_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        instance_metadata_options: Optional[InstanceMetadataOptions] = None,
        instance_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        key_pair: Optional[Union[str, core.StringOut]] = None,
        logging: Optional[Logging] = None,
        resource_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        sns_topic_arn: Optional[Union[str, core.StringOut]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        terminate_instance_on_failure: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=InfrastructureConfiguration.Args(
                instance_profile_name=instance_profile_name,
                name=name,
                description=description,
                instance_metadata_options=instance_metadata_options,
                instance_types=instance_types,
                key_pair=key_pair,
                logging=logging,
                resource_tags=resource_tags,
                security_group_ids=security_group_ids,
                sns_topic_arn=sns_topic_arn,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                terminate_instance_on_failure=terminate_instance_on_failure,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_metadata_options: Optional[InstanceMetadataOptions] = core.arg(default=None)

        instance_profile_name: Union[str, core.StringOut] = core.arg()

        instance_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        key_pair: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        logging: Optional[Logging] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        resource_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        sns_topic_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        terminate_instance_on_failure: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
