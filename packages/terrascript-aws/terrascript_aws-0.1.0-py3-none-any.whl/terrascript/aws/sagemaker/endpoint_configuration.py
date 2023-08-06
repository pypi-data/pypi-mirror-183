from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ClientConfig(core.Schema):

    max_concurrent_invocations_per_instance: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    def __init__(
        self,
        *,
        max_concurrent_invocations_per_instance: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ClientConfig.Args(
                max_concurrent_invocations_per_instance=max_concurrent_invocations_per_instance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_concurrent_invocations_per_instance: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )


@core.schema
class NotificationConfig(core.Schema):

    error_topic: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    success_topic: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        error_topic: Optional[Union[str, core.StringOut]] = None,
        success_topic: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=NotificationConfig.Args(
                error_topic=error_topic,
                success_topic=success_topic,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_topic: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        success_topic: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class OutputConfig(core.Schema):

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    notification_config: Optional[NotificationConfig] = core.attr(NotificationConfig, default=None)

    s3_output_path: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        s3_output_path: Union[str, core.StringOut],
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        notification_config: Optional[NotificationConfig] = None,
    ):
        super().__init__(
            args=OutputConfig.Args(
                s3_output_path=s3_output_path,
                kms_key_id=kms_key_id,
                notification_config=notification_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        notification_config: Optional[NotificationConfig] = core.arg(default=None)

        s3_output_path: Union[str, core.StringOut] = core.arg()


@core.schema
class AsyncInferenceConfig(core.Schema):

    client_config: Optional[ClientConfig] = core.attr(ClientConfig, default=None)

    output_config: OutputConfig = core.attr(OutputConfig)

    def __init__(
        self,
        *,
        output_config: OutputConfig,
        client_config: Optional[ClientConfig] = None,
    ):
        super().__init__(
            args=AsyncInferenceConfig.Args(
                output_config=output_config,
                client_config=client_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_config: Optional[ClientConfig] = core.arg(default=None)

        output_config: OutputConfig = core.arg()


@core.schema
class CaptureOptions(core.Schema):

    capture_mode: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        capture_mode: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CaptureOptions.Args(
                capture_mode=capture_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capture_mode: Union[str, core.StringOut] = core.arg()


@core.schema
class CaptureContentTypeHeader(core.Schema):

    csv_content_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    json_content_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        csv_content_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        json_content_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=CaptureContentTypeHeader.Args(
                csv_content_types=csv_content_types,
                json_content_types=json_content_types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        csv_content_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        json_content_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class DataCaptureConfig(core.Schema):

    capture_content_type_header: Optional[CaptureContentTypeHeader] = core.attr(
        CaptureContentTypeHeader, default=None
    )

    capture_options: Union[List[CaptureOptions], core.ArrayOut[CaptureOptions]] = core.attr(
        CaptureOptions, kind=core.Kind.array
    )

    destination_s3_uri: Union[str, core.StringOut] = core.attr(str)

    enable_capture: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    initial_sampling_percentage: Union[int, core.IntOut] = core.attr(int)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        capture_options: Union[List[CaptureOptions], core.ArrayOut[CaptureOptions]],
        destination_s3_uri: Union[str, core.StringOut],
        initial_sampling_percentage: Union[int, core.IntOut],
        capture_content_type_header: Optional[CaptureContentTypeHeader] = None,
        enable_capture: Optional[Union[bool, core.BoolOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DataCaptureConfig.Args(
                capture_options=capture_options,
                destination_s3_uri=destination_s3_uri,
                initial_sampling_percentage=initial_sampling_percentage,
                capture_content_type_header=capture_content_type_header,
                enable_capture=enable_capture,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capture_content_type_header: Optional[CaptureContentTypeHeader] = core.arg(default=None)

        capture_options: Union[List[CaptureOptions], core.ArrayOut[CaptureOptions]] = core.arg()

        destination_s3_uri: Union[str, core.StringOut] = core.arg()

        enable_capture: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        initial_sampling_percentage: Union[int, core.IntOut] = core.arg()

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ServerlessConfig(core.Schema):

    max_concurrency: Union[int, core.IntOut] = core.attr(int)

    memory_size_in_mb: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        max_concurrency: Union[int, core.IntOut],
        memory_size_in_mb: Union[int, core.IntOut],
    ):
        super().__init__(
            args=ServerlessConfig.Args(
                max_concurrency=max_concurrency,
                memory_size_in_mb=memory_size_in_mb,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_concurrency: Union[int, core.IntOut] = core.arg()

        memory_size_in_mb: Union[int, core.IntOut] = core.arg()


@core.schema
class ProductionVariants(core.Schema):

    accelerator_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    initial_instance_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    initial_variant_weight: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    instance_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    model_name: Union[str, core.StringOut] = core.attr(str)

    serverless_config: Optional[ServerlessConfig] = core.attr(ServerlessConfig, default=None)

    variant_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        model_name: Union[str, core.StringOut],
        accelerator_type: Optional[Union[str, core.StringOut]] = None,
        initial_instance_count: Optional[Union[int, core.IntOut]] = None,
        initial_variant_weight: Optional[Union[float, core.FloatOut]] = None,
        instance_type: Optional[Union[str, core.StringOut]] = None,
        serverless_config: Optional[ServerlessConfig] = None,
        variant_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ProductionVariants.Args(
                model_name=model_name,
                accelerator_type=accelerator_type,
                initial_instance_count=initial_instance_count,
                initial_variant_weight=initial_variant_weight,
                instance_type=instance_type,
                serverless_config=serverless_config,
                variant_name=variant_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accelerator_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        initial_instance_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        initial_variant_weight: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        model_name: Union[str, core.StringOut] = core.arg()

        serverless_config: Optional[ServerlessConfig] = core.arg(default=None)

        variant_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_sagemaker_endpoint_configuration", namespace="aws_sagemaker")
class EndpointConfiguration(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    async_inference_config: Optional[AsyncInferenceConfig] = core.attr(
        AsyncInferenceConfig, default=None
    )

    data_capture_config: Optional[DataCaptureConfig] = core.attr(DataCaptureConfig, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    production_variants: Union[
        List[ProductionVariants], core.ArrayOut[ProductionVariants]
    ] = core.attr(ProductionVariants, kind=core.Kind.array)

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
        production_variants: Union[List[ProductionVariants], core.ArrayOut[ProductionVariants]],
        async_inference_config: Optional[AsyncInferenceConfig] = None,
        data_capture_config: Optional[DataCaptureConfig] = None,
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointConfiguration.Args(
                production_variants=production_variants,
                async_inference_config=async_inference_config,
                data_capture_config=data_capture_config,
                kms_key_arn=kms_key_arn,
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
        async_inference_config: Optional[AsyncInferenceConfig] = core.arg(default=None)

        data_capture_config: Optional[DataCaptureConfig] = core.arg(default=None)

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        production_variants: Union[
            List[ProductionVariants], core.ArrayOut[ProductionVariants]
        ] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
