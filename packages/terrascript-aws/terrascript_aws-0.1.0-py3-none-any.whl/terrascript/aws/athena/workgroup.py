from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AclConfiguration(core.Schema):

    s3_acl_option: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        s3_acl_option: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AclConfiguration.Args(
                s3_acl_option=s3_acl_option,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_acl_option: Union[str, core.StringOut] = core.arg()


@core.schema
class EncryptionConfiguration(core.Schema):

    encryption_option: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        encryption_option: Optional[Union[str, core.StringOut]] = None,
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                encryption_option=encryption_option,
                kms_key_arn=kms_key_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_option: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ResultConfiguration(core.Schema):

    acl_configuration: Optional[AclConfiguration] = core.attr(AclConfiguration, default=None)

    encryption_configuration: Optional[EncryptionConfiguration] = core.attr(
        EncryptionConfiguration, default=None
    )

    expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    output_location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        acl_configuration: Optional[AclConfiguration] = None,
        encryption_configuration: Optional[EncryptionConfiguration] = None,
        expected_bucket_owner: Optional[Union[str, core.StringOut]] = None,
        output_location: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ResultConfiguration.Args(
                acl_configuration=acl_configuration,
                encryption_configuration=encryption_configuration,
                expected_bucket_owner=expected_bucket_owner,
                output_location=output_location,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acl_configuration: Optional[AclConfiguration] = core.arg(default=None)

        encryption_configuration: Optional[EncryptionConfiguration] = core.arg(default=None)

        expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        output_location: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class EngineVersion(core.Schema):

    effective_engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    selected_engine_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        effective_engine_version: Union[str, core.StringOut],
        selected_engine_version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EngineVersion.Args(
                effective_engine_version=effective_engine_version,
                selected_engine_version=selected_engine_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        effective_engine_version: Union[str, core.StringOut] = core.arg()

        selected_engine_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Configuration(core.Schema):

    bytes_scanned_cutoff_per_query: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    enforce_workgroup_configuration: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    engine_version: Optional[EngineVersion] = core.attr(EngineVersion, default=None)

    publish_cloudwatch_metrics_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    requester_pays_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    result_configuration: Optional[ResultConfiguration] = core.attr(
        ResultConfiguration, default=None
    )

    def __init__(
        self,
        *,
        bytes_scanned_cutoff_per_query: Optional[Union[int, core.IntOut]] = None,
        enforce_workgroup_configuration: Optional[Union[bool, core.BoolOut]] = None,
        engine_version: Optional[EngineVersion] = None,
        publish_cloudwatch_metrics_enabled: Optional[Union[bool, core.BoolOut]] = None,
        requester_pays_enabled: Optional[Union[bool, core.BoolOut]] = None,
        result_configuration: Optional[ResultConfiguration] = None,
    ):
        super().__init__(
            args=Configuration.Args(
                bytes_scanned_cutoff_per_query=bytes_scanned_cutoff_per_query,
                enforce_workgroup_configuration=enforce_workgroup_configuration,
                engine_version=engine_version,
                publish_cloudwatch_metrics_enabled=publish_cloudwatch_metrics_enabled,
                requester_pays_enabled=requester_pays_enabled,
                result_configuration=result_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bytes_scanned_cutoff_per_query: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        enforce_workgroup_configuration: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        engine_version: Optional[EngineVersion] = core.arg(default=None)

        publish_cloudwatch_metrics_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        requester_pays_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        result_configuration: Optional[ResultConfiguration] = core.arg(default=None)


@core.resource(type="aws_athena_workgroup", namespace="aws_athena")
class Workgroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    configuration: Optional[Configuration] = core.attr(Configuration, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    force_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        name: Union[str, core.StringOut],
        configuration: Optional[Configuration] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        force_destroy: Optional[Union[bool, core.BoolOut]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workgroup.Args(
                name=name,
                configuration=configuration,
                description=description,
                force_destroy=force_destroy,
                state=state,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        configuration: Optional[Configuration] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        force_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
