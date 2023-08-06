from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_glue_dev_endpoint", namespace="aws_glue")
class DevEndpoint(core.Resource):
    """
    (Optional) A map of arguments used to configure the endpoint.
    """

    arguments: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    The ARN of the endpoint.
    """
    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The AWS availability zone where this endpoint is located.
    """
    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) Path to one or more Java Jars in an S3 bucket that should be loaded in this endpoint.
    """
    extra_jars_s3_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Optional) Path(s) to one or more Python libraries in an S3 bucket that should be loaded in this end
    point. Multiple values must be complete paths separated by a comma.
    """
    extra_python_libs_s3_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    The reason for a current failure in this endpoint.
    """
    failure_reason: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) -  Specifies the versions of Python and Apache Spark to use. Defaults to AWS Glue version
    0.9.
    """
    glue_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The name of this endpoint. It must be unique in your account.
    """
    name: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) The number of AWS Glue Data Processing Units (DPUs) to allocate to this endpoint. Conflic
    ts with `worker_type`.
    """
    number_of_nodes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    """
    (Optional) The number of workers of a defined worker type that are allocated to this endpoint. This
    field is available only when you choose worker type G.1X or G.2X.
    """
    number_of_workers: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    """
    A private IP address to access the endpoint within a VPC, if this endpoint is created within one.
    """
    private_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The public IP address used by this endpoint. The PublicAddress field is present only when you create
    a non-VPC endpoint.
    """
    public_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) The public key to be used by this endpoint for authentication.
    """
    public_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Optional) A list of public keys to be used by this endpoint for authentication.
    """
    public_keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) The IAM role for this endpoint.
    """
    role_arn: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) The name of the Security Configuration structure to be used with this endpoint.
    """
    security_configuration: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Optional) Security group IDs for the security groups to be used by this endpoint.
    """
    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The current status of this endpoint.
    """
    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) The subnet ID for the new endpoint to use.
    """
    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    he ID of the VPC used by this endpoint.
    """
    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) The type of predefined worker that is allocated to this endpoint. Accepts a value of Stan
    dard, G.1X, or G.2X.
    """
    worker_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    The YARN endpoint address used by this endpoint.
    """
    yarn_endpoint_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The Apache Zeppelin port for the remote Apache Spark interpreter.
    """
    zeppelin_remote_spark_interpreter_port: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        arguments: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        extra_jars_s3_path: Optional[Union[str, core.StringOut]] = None,
        extra_python_libs_s3_path: Optional[Union[str, core.StringOut]] = None,
        glue_version: Optional[Union[str, core.StringOut]] = None,
        number_of_nodes: Optional[Union[int, core.IntOut]] = None,
        number_of_workers: Optional[Union[int, core.IntOut]] = None,
        public_key: Optional[Union[str, core.StringOut]] = None,
        public_keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        security_configuration: Optional[Union[str, core.StringOut]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        worker_type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DevEndpoint.Args(
                name=name,
                role_arn=role_arn,
                arguments=arguments,
                extra_jars_s3_path=extra_jars_s3_path,
                extra_python_libs_s3_path=extra_python_libs_s3_path,
                glue_version=glue_version,
                number_of_nodes=number_of_nodes,
                number_of_workers=number_of_workers,
                public_key=public_key,
                public_keys=public_keys,
                security_configuration=security_configuration,
                security_group_ids=security_group_ids,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                worker_type=worker_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arguments: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        extra_jars_s3_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        extra_python_libs_s3_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        glue_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        number_of_nodes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        number_of_workers: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        public_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        public_keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        role_arn: Union[str, core.StringOut] = core.arg()

        security_configuration: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        worker_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
