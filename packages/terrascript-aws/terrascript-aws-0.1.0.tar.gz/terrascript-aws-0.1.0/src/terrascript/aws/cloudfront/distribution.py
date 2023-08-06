from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class GeoRestriction(core.Schema):

    locations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    restriction_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        restriction_type: Union[str, core.StringOut],
        locations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=GeoRestriction.Args(
                restriction_type=restriction_type,
                locations=locations,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        locations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        restriction_type: Union[str, core.StringOut] = core.arg()


@core.schema
class Restrictions(core.Schema):

    geo_restriction: GeoRestriction = core.attr(GeoRestriction)

    def __init__(
        self,
        *,
        geo_restriction: GeoRestriction,
    ):
        super().__init__(
            args=Restrictions.Args(
                geo_restriction=geo_restriction,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        geo_restriction: GeoRestriction = core.arg()


@core.schema
class OriginShield(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    origin_shield_region: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        origin_shield_region: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OriginShield.Args(
                enabled=enabled,
                origin_shield_region=origin_shield_region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        origin_shield_region: Union[str, core.StringOut] = core.arg()


@core.schema
class S3OriginConfig(core.Schema):

    origin_access_identity: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        origin_access_identity: Union[str, core.StringOut],
    ):
        super().__init__(
            args=S3OriginConfig.Args(
                origin_access_identity=origin_access_identity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        origin_access_identity: Union[str, core.StringOut] = core.arg()


@core.schema
class CustomOriginConfig(core.Schema):

    http_port: Union[int, core.IntOut] = core.attr(int)

    https_port: Union[int, core.IntOut] = core.attr(int)

    origin_keepalive_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    origin_protocol_policy: Union[str, core.StringOut] = core.attr(str)

    origin_read_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    origin_ssl_protocols: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        http_port: Union[int, core.IntOut],
        https_port: Union[int, core.IntOut],
        origin_protocol_policy: Union[str, core.StringOut],
        origin_ssl_protocols: Union[List[str], core.ArrayOut[core.StringOut]],
        origin_keepalive_timeout: Optional[Union[int, core.IntOut]] = None,
        origin_read_timeout: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CustomOriginConfig.Args(
                http_port=http_port,
                https_port=https_port,
                origin_protocol_policy=origin_protocol_policy,
                origin_ssl_protocols=origin_ssl_protocols,
                origin_keepalive_timeout=origin_keepalive_timeout,
                origin_read_timeout=origin_read_timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_port: Union[int, core.IntOut] = core.arg()

        https_port: Union[int, core.IntOut] = core.arg()

        origin_keepalive_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        origin_protocol_policy: Union[str, core.StringOut] = core.arg()

        origin_read_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        origin_ssl_protocols: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class CustomHeader(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CustomHeader.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Origin(core.Schema):

    connection_attempts: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    connection_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    custom_header: Optional[Union[List[CustomHeader], core.ArrayOut[CustomHeader]]] = core.attr(
        CustomHeader, default=None, kind=core.Kind.array
    )

    custom_origin_config: Optional[CustomOriginConfig] = core.attr(CustomOriginConfig, default=None)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    origin_id: Union[str, core.StringOut] = core.attr(str)

    origin_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    origin_shield: Optional[OriginShield] = core.attr(OriginShield, default=None)

    s3_origin_config: Optional[S3OriginConfig] = core.attr(S3OriginConfig, default=None)

    def __init__(
        self,
        *,
        domain_name: Union[str, core.StringOut],
        origin_id: Union[str, core.StringOut],
        connection_attempts: Optional[Union[int, core.IntOut]] = None,
        connection_timeout: Optional[Union[int, core.IntOut]] = None,
        custom_header: Optional[Union[List[CustomHeader], core.ArrayOut[CustomHeader]]] = None,
        custom_origin_config: Optional[CustomOriginConfig] = None,
        origin_path: Optional[Union[str, core.StringOut]] = None,
        origin_shield: Optional[OriginShield] = None,
        s3_origin_config: Optional[S3OriginConfig] = None,
    ):
        super().__init__(
            args=Origin.Args(
                domain_name=domain_name,
                origin_id=origin_id,
                connection_attempts=connection_attempts,
                connection_timeout=connection_timeout,
                custom_header=custom_header,
                custom_origin_config=custom_origin_config,
                origin_path=origin_path,
                origin_shield=origin_shield,
                s3_origin_config=s3_origin_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_attempts: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        connection_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        custom_header: Optional[Union[List[CustomHeader], core.ArrayOut[CustomHeader]]] = core.arg(
            default=None
        )

        custom_origin_config: Optional[CustomOriginConfig] = core.arg(default=None)

        domain_name: Union[str, core.StringOut] = core.arg()

        origin_id: Union[str, core.StringOut] = core.arg()

        origin_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        origin_shield: Optional[OriginShield] = core.arg(default=None)

        s3_origin_config: Optional[S3OriginConfig] = core.arg(default=None)


@core.schema
class OrderedCacheBehaviorForwardedValuesCookies(core.Schema):

    forward: Union[str, core.StringOut] = core.attr(str)

    whitelisted_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        forward: Union[str, core.StringOut],
        whitelisted_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=OrderedCacheBehaviorForwardedValuesCookies.Args(
                forward=forward,
                whitelisted_names=whitelisted_names,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        forward: Union[str, core.StringOut] = core.arg()

        whitelisted_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class OrderedCacheBehaviorForwardedValues(core.Schema):

    cookies: OrderedCacheBehaviorForwardedValuesCookies = core.attr(
        OrderedCacheBehaviorForwardedValuesCookies
    )

    headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    query_string: Union[bool, core.BoolOut] = core.attr(bool)

    query_string_cache_keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cookies: OrderedCacheBehaviorForwardedValuesCookies,
        query_string: Union[bool, core.BoolOut],
        headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        query_string_cache_keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=OrderedCacheBehaviorForwardedValues.Args(
                cookies=cookies,
                query_string=query_string,
                headers=headers,
                query_string_cache_keys=query_string_cache_keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookies: OrderedCacheBehaviorForwardedValuesCookies = core.arg()

        headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        query_string: Union[bool, core.BoolOut] = core.arg()

        query_string_cache_keys: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)


@core.schema
class LambdaFunctionAssociation(core.Schema):

    event_type: Union[str, core.StringOut] = core.attr(str)

    include_body: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    lambda_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        event_type: Union[str, core.StringOut],
        lambda_arn: Union[str, core.StringOut],
        include_body: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=LambdaFunctionAssociation.Args(
                event_type=event_type,
                lambda_arn=lambda_arn,
                include_body=include_body,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_type: Union[str, core.StringOut] = core.arg()

        include_body: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        lambda_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class FunctionAssociation(core.Schema):

    event_type: Union[str, core.StringOut] = core.attr(str)

    function_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        event_type: Union[str, core.StringOut],
        function_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=FunctionAssociation.Args(
                event_type=event_type,
                function_arn=function_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_type: Union[str, core.StringOut] = core.arg()

        function_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class OrderedCacheBehavior(core.Schema):

    allowed_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    cache_policy_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cached_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    compress: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    default_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    field_level_encryption_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    forwarded_values: Optional[OrderedCacheBehaviorForwardedValues] = core.attr(
        OrderedCacheBehaviorForwardedValues, default=None
    )

    function_association: Optional[
        Union[List[FunctionAssociation], core.ArrayOut[FunctionAssociation]]
    ] = core.attr(FunctionAssociation, default=None, kind=core.Kind.array)

    lambda_function_association: Optional[
        Union[List[LambdaFunctionAssociation], core.ArrayOut[LambdaFunctionAssociation]]
    ] = core.attr(LambdaFunctionAssociation, default=None, kind=core.Kind.array)

    max_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    min_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    origin_request_policy_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    path_pattern: Union[str, core.StringOut] = core.attr(str)

    realtime_log_config_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    response_headers_policy_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    smooth_streaming: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    target_origin_id: Union[str, core.StringOut] = core.attr(str)

    trusted_key_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    trusted_signers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    viewer_protocol_policy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        allowed_methods: Union[List[str], core.ArrayOut[core.StringOut]],
        cached_methods: Union[List[str], core.ArrayOut[core.StringOut]],
        path_pattern: Union[str, core.StringOut],
        target_origin_id: Union[str, core.StringOut],
        viewer_protocol_policy: Union[str, core.StringOut],
        cache_policy_id: Optional[Union[str, core.StringOut]] = None,
        compress: Optional[Union[bool, core.BoolOut]] = None,
        default_ttl: Optional[Union[int, core.IntOut]] = None,
        field_level_encryption_id: Optional[Union[str, core.StringOut]] = None,
        forwarded_values: Optional[OrderedCacheBehaviorForwardedValues] = None,
        function_association: Optional[
            Union[List[FunctionAssociation], core.ArrayOut[FunctionAssociation]]
        ] = None,
        lambda_function_association: Optional[
            Union[List[LambdaFunctionAssociation], core.ArrayOut[LambdaFunctionAssociation]]
        ] = None,
        max_ttl: Optional[Union[int, core.IntOut]] = None,
        min_ttl: Optional[Union[int, core.IntOut]] = None,
        origin_request_policy_id: Optional[Union[str, core.StringOut]] = None,
        realtime_log_config_arn: Optional[Union[str, core.StringOut]] = None,
        response_headers_policy_id: Optional[Union[str, core.StringOut]] = None,
        smooth_streaming: Optional[Union[bool, core.BoolOut]] = None,
        trusted_key_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        trusted_signers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=OrderedCacheBehavior.Args(
                allowed_methods=allowed_methods,
                cached_methods=cached_methods,
                path_pattern=path_pattern,
                target_origin_id=target_origin_id,
                viewer_protocol_policy=viewer_protocol_policy,
                cache_policy_id=cache_policy_id,
                compress=compress,
                default_ttl=default_ttl,
                field_level_encryption_id=field_level_encryption_id,
                forwarded_values=forwarded_values,
                function_association=function_association,
                lambda_function_association=lambda_function_association,
                max_ttl=max_ttl,
                min_ttl=min_ttl,
                origin_request_policy_id=origin_request_policy_id,
                realtime_log_config_arn=realtime_log_config_arn,
                response_headers_policy_id=response_headers_policy_id,
                smooth_streaming=smooth_streaming,
                trusted_key_groups=trusted_key_groups,
                trusted_signers=trusted_signers,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allowed_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        cache_policy_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cached_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        compress: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        default_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        field_level_encryption_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        forwarded_values: Optional[OrderedCacheBehaviorForwardedValues] = core.arg(default=None)

        function_association: Optional[
            Union[List[FunctionAssociation], core.ArrayOut[FunctionAssociation]]
        ] = core.arg(default=None)

        lambda_function_association: Optional[
            Union[List[LambdaFunctionAssociation], core.ArrayOut[LambdaFunctionAssociation]]
        ] = core.arg(default=None)

        max_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        origin_request_policy_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        path_pattern: Union[str, core.StringOut] = core.arg()

        realtime_log_config_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        response_headers_policy_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        smooth_streaming: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        target_origin_id: Union[str, core.StringOut] = core.arg()

        trusted_key_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        trusted_signers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        viewer_protocol_policy: Union[str, core.StringOut] = core.arg()


@core.schema
class CustomErrorResponse(core.Schema):

    error_caching_min_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    error_code: Union[int, core.IntOut] = core.attr(int)

    response_code: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    response_page_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        error_code: Union[int, core.IntOut],
        error_caching_min_ttl: Optional[Union[int, core.IntOut]] = None,
        response_code: Optional[Union[int, core.IntOut]] = None,
        response_page_path: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CustomErrorResponse.Args(
                error_code=error_code,
                error_caching_min_ttl=error_caching_min_ttl,
                response_code=response_code,
                response_page_path=response_page_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_caching_min_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        error_code: Union[int, core.IntOut] = core.arg()

        response_code: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        response_page_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TrustedKeyGroupsItems(core.Schema):

    key_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_pair_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key_group_id: Union[str, core.StringOut],
        key_pair_ids: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=TrustedKeyGroupsItems.Args(
                key_group_id=key_group_id,
                key_pair_ids=key_pair_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_group_id: Union[str, core.StringOut] = core.arg()

        key_pair_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class TrustedKeyGroups(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    items: Union[List[TrustedKeyGroupsItems], core.ArrayOut[TrustedKeyGroupsItems]] = core.attr(
        TrustedKeyGroupsItems, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        items: Union[List[TrustedKeyGroupsItems], core.ArrayOut[TrustedKeyGroupsItems]],
    ):
        super().__init__(
            args=TrustedKeyGroups.Args(
                enabled=enabled,
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        items: Union[List[TrustedKeyGroupsItems], core.ArrayOut[TrustedKeyGroupsItems]] = core.arg()


@core.schema
class FailoverCriteria(core.Schema):

    status_codes: Union[List[int], core.ArrayOut[core.IntOut]] = core.attr(
        int, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        status_codes: Union[List[int], core.ArrayOut[core.IntOut]],
    ):
        super().__init__(
            args=FailoverCriteria.Args(
                status_codes=status_codes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status_codes: Union[List[int], core.ArrayOut[core.IntOut]] = core.arg()


@core.schema
class Member(core.Schema):

    origin_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        origin_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Member.Args(
                origin_id=origin_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        origin_id: Union[str, core.StringOut] = core.arg()


@core.schema
class OriginGroup(core.Schema):

    failover_criteria: FailoverCriteria = core.attr(FailoverCriteria)

    member: Union[List[Member], core.ArrayOut[Member]] = core.attr(Member, kind=core.Kind.array)

    origin_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        failover_criteria: FailoverCriteria,
        member: Union[List[Member], core.ArrayOut[Member]],
        origin_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OriginGroup.Args(
                failover_criteria=failover_criteria,
                member=member,
                origin_id=origin_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        failover_criteria: FailoverCriteria = core.arg()

        member: Union[List[Member], core.ArrayOut[Member]] = core.arg()

        origin_id: Union[str, core.StringOut] = core.arg()


@core.schema
class TrustedSignersItems(core.Schema):

    aws_account_number: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_pair_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        aws_account_number: Union[str, core.StringOut],
        key_pair_ids: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=TrustedSignersItems.Args(
                aws_account_number=aws_account_number,
                key_pair_ids=key_pair_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_account_number: Union[str, core.StringOut] = core.arg()

        key_pair_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class TrustedSigners(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    items: Union[List[TrustedSignersItems], core.ArrayOut[TrustedSignersItems]] = core.attr(
        TrustedSignersItems, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        items: Union[List[TrustedSignersItems], core.ArrayOut[TrustedSignersItems]],
    ):
        super().__init__(
            args=TrustedSigners.Args(
                enabled=enabled,
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        items: Union[List[TrustedSignersItems], core.ArrayOut[TrustedSignersItems]] = core.arg()


@core.schema
class DefaultCacheBehaviorForwardedValuesCookies(core.Schema):

    forward: Union[str, core.StringOut] = core.attr(str)

    whitelisted_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        forward: Union[str, core.StringOut],
        whitelisted_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=DefaultCacheBehaviorForwardedValuesCookies.Args(
                forward=forward,
                whitelisted_names=whitelisted_names,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        forward: Union[str, core.StringOut] = core.arg()

        whitelisted_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class DefaultCacheBehaviorForwardedValues(core.Schema):

    cookies: DefaultCacheBehaviorForwardedValuesCookies = core.attr(
        DefaultCacheBehaviorForwardedValuesCookies
    )

    headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    query_string: Union[bool, core.BoolOut] = core.attr(bool)

    query_string_cache_keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cookies: DefaultCacheBehaviorForwardedValuesCookies,
        query_string: Union[bool, core.BoolOut],
        headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        query_string_cache_keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=DefaultCacheBehaviorForwardedValues.Args(
                cookies=cookies,
                query_string=query_string,
                headers=headers,
                query_string_cache_keys=query_string_cache_keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookies: DefaultCacheBehaviorForwardedValuesCookies = core.arg()

        headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        query_string: Union[bool, core.BoolOut] = core.arg()

        query_string_cache_keys: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)


@core.schema
class DefaultCacheBehavior(core.Schema):

    allowed_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    cache_policy_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cached_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    compress: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    default_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    field_level_encryption_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    forwarded_values: Optional[DefaultCacheBehaviorForwardedValues] = core.attr(
        DefaultCacheBehaviorForwardedValues, default=None
    )

    function_association: Optional[
        Union[List[FunctionAssociation], core.ArrayOut[FunctionAssociation]]
    ] = core.attr(FunctionAssociation, default=None, kind=core.Kind.array)

    lambda_function_association: Optional[
        Union[List[LambdaFunctionAssociation], core.ArrayOut[LambdaFunctionAssociation]]
    ] = core.attr(LambdaFunctionAssociation, default=None, kind=core.Kind.array)

    max_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    min_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    origin_request_policy_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    realtime_log_config_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    response_headers_policy_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    smooth_streaming: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    target_origin_id: Union[str, core.StringOut] = core.attr(str)

    trusted_key_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    trusted_signers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    viewer_protocol_policy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        allowed_methods: Union[List[str], core.ArrayOut[core.StringOut]],
        cached_methods: Union[List[str], core.ArrayOut[core.StringOut]],
        target_origin_id: Union[str, core.StringOut],
        viewer_protocol_policy: Union[str, core.StringOut],
        cache_policy_id: Optional[Union[str, core.StringOut]] = None,
        compress: Optional[Union[bool, core.BoolOut]] = None,
        default_ttl: Optional[Union[int, core.IntOut]] = None,
        field_level_encryption_id: Optional[Union[str, core.StringOut]] = None,
        forwarded_values: Optional[DefaultCacheBehaviorForwardedValues] = None,
        function_association: Optional[
            Union[List[FunctionAssociation], core.ArrayOut[FunctionAssociation]]
        ] = None,
        lambda_function_association: Optional[
            Union[List[LambdaFunctionAssociation], core.ArrayOut[LambdaFunctionAssociation]]
        ] = None,
        max_ttl: Optional[Union[int, core.IntOut]] = None,
        min_ttl: Optional[Union[int, core.IntOut]] = None,
        origin_request_policy_id: Optional[Union[str, core.StringOut]] = None,
        realtime_log_config_arn: Optional[Union[str, core.StringOut]] = None,
        response_headers_policy_id: Optional[Union[str, core.StringOut]] = None,
        smooth_streaming: Optional[Union[bool, core.BoolOut]] = None,
        trusted_key_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        trusted_signers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=DefaultCacheBehavior.Args(
                allowed_methods=allowed_methods,
                cached_methods=cached_methods,
                target_origin_id=target_origin_id,
                viewer_protocol_policy=viewer_protocol_policy,
                cache_policy_id=cache_policy_id,
                compress=compress,
                default_ttl=default_ttl,
                field_level_encryption_id=field_level_encryption_id,
                forwarded_values=forwarded_values,
                function_association=function_association,
                lambda_function_association=lambda_function_association,
                max_ttl=max_ttl,
                min_ttl=min_ttl,
                origin_request_policy_id=origin_request_policy_id,
                realtime_log_config_arn=realtime_log_config_arn,
                response_headers_policy_id=response_headers_policy_id,
                smooth_streaming=smooth_streaming,
                trusted_key_groups=trusted_key_groups,
                trusted_signers=trusted_signers,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allowed_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        cache_policy_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cached_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        compress: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        default_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        field_level_encryption_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        forwarded_values: Optional[DefaultCacheBehaviorForwardedValues] = core.arg(default=None)

        function_association: Optional[
            Union[List[FunctionAssociation], core.ArrayOut[FunctionAssociation]]
        ] = core.arg(default=None)

        lambda_function_association: Optional[
            Union[List[LambdaFunctionAssociation], core.ArrayOut[LambdaFunctionAssociation]]
        ] = core.arg(default=None)

        max_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        origin_request_policy_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        realtime_log_config_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        response_headers_policy_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        smooth_streaming: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        target_origin_id: Union[str, core.StringOut] = core.arg()

        trusted_key_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        trusted_signers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        viewer_protocol_policy: Union[str, core.StringOut] = core.arg()


@core.schema
class ViewerCertificate(core.Schema):

    acm_certificate_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudfront_default_certificate: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    iam_certificate_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    minimum_protocol_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssl_support_method: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        acm_certificate_arn: Optional[Union[str, core.StringOut]] = None,
        cloudfront_default_certificate: Optional[Union[bool, core.BoolOut]] = None,
        iam_certificate_id: Optional[Union[str, core.StringOut]] = None,
        minimum_protocol_version: Optional[Union[str, core.StringOut]] = None,
        ssl_support_method: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ViewerCertificate.Args(
                acm_certificate_arn=acm_certificate_arn,
                cloudfront_default_certificate=cloudfront_default_certificate,
                iam_certificate_id=iam_certificate_id,
                minimum_protocol_version=minimum_protocol_version,
                ssl_support_method=ssl_support_method,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acm_certificate_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudfront_default_certificate: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        iam_certificate_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        minimum_protocol_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssl_support_method: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class LoggingConfig(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str)

    include_cookies: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        include_cookies: Optional[Union[bool, core.BoolOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LoggingConfig.Args(
                bucket=bucket,
                include_cookies=include_cookies,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        include_cookies: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_cloudfront_distribution", namespace="aws_cloudfront")
class Distribution(core.Resource):

    aliases: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    caller_reference: Union[str, core.StringOut] = core.attr(str, computed=True)

    comment: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    custom_error_response: Optional[
        Union[List[CustomErrorResponse], core.ArrayOut[CustomErrorResponse]]
    ] = core.attr(CustomErrorResponse, default=None, kind=core.Kind.array)

    default_cache_behavior: DefaultCacheBehavior = core.attr(DefaultCacheBehavior)

    default_root_object: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    etag: Union[str, core.StringOut] = core.attr(str, computed=True)

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    http_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    in_progress_validation_batches: Union[int, core.IntOut] = core.attr(int, computed=True)

    is_ipv6_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    last_modified_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    logging_config: Optional[LoggingConfig] = core.attr(LoggingConfig, default=None)

    ordered_cache_behavior: Optional[
        Union[List[OrderedCacheBehavior], core.ArrayOut[OrderedCacheBehavior]]
    ] = core.attr(OrderedCacheBehavior, default=None, kind=core.Kind.array)

    origin: Union[List[Origin], core.ArrayOut[Origin]] = core.attr(Origin, kind=core.Kind.array)

    origin_group: Optional[Union[List[OriginGroup], core.ArrayOut[OriginGroup]]] = core.attr(
        OriginGroup, default=None, kind=core.Kind.array
    )

    price_class: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    restrictions: Restrictions = core.attr(Restrictions)

    retain_on_delete: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    trusted_key_groups: Union[List[TrustedKeyGroups], core.ArrayOut[TrustedKeyGroups]] = core.attr(
        TrustedKeyGroups, computed=True, kind=core.Kind.array
    )

    trusted_signers: Union[List[TrustedSigners], core.ArrayOut[TrustedSigners]] = core.attr(
        TrustedSigners, computed=True, kind=core.Kind.array
    )

    viewer_certificate: ViewerCertificate = core.attr(ViewerCertificate)

    wait_for_deployment: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    web_acl_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        default_cache_behavior: DefaultCacheBehavior,
        enabled: Union[bool, core.BoolOut],
        origin: Union[List[Origin], core.ArrayOut[Origin]],
        restrictions: Restrictions,
        viewer_certificate: ViewerCertificate,
        aliases: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        comment: Optional[Union[str, core.StringOut]] = None,
        custom_error_response: Optional[
            Union[List[CustomErrorResponse], core.ArrayOut[CustomErrorResponse]]
        ] = None,
        default_root_object: Optional[Union[str, core.StringOut]] = None,
        http_version: Optional[Union[str, core.StringOut]] = None,
        is_ipv6_enabled: Optional[Union[bool, core.BoolOut]] = None,
        logging_config: Optional[LoggingConfig] = None,
        ordered_cache_behavior: Optional[
            Union[List[OrderedCacheBehavior], core.ArrayOut[OrderedCacheBehavior]]
        ] = None,
        origin_group: Optional[Union[List[OriginGroup], core.ArrayOut[OriginGroup]]] = None,
        price_class: Optional[Union[str, core.StringOut]] = None,
        retain_on_delete: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        wait_for_deployment: Optional[Union[bool, core.BoolOut]] = None,
        web_acl_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Distribution.Args(
                default_cache_behavior=default_cache_behavior,
                enabled=enabled,
                origin=origin,
                restrictions=restrictions,
                viewer_certificate=viewer_certificate,
                aliases=aliases,
                comment=comment,
                custom_error_response=custom_error_response,
                default_root_object=default_root_object,
                http_version=http_version,
                is_ipv6_enabled=is_ipv6_enabled,
                logging_config=logging_config,
                ordered_cache_behavior=ordered_cache_behavior,
                origin_group=origin_group,
                price_class=price_class,
                retain_on_delete=retain_on_delete,
                tags=tags,
                tags_all=tags_all,
                wait_for_deployment=wait_for_deployment,
                web_acl_id=web_acl_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aliases: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        comment: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        custom_error_response: Optional[
            Union[List[CustomErrorResponse], core.ArrayOut[CustomErrorResponse]]
        ] = core.arg(default=None)

        default_cache_behavior: DefaultCacheBehavior = core.arg()

        default_root_object: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Union[bool, core.BoolOut] = core.arg()

        http_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        is_ipv6_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        logging_config: Optional[LoggingConfig] = core.arg(default=None)

        ordered_cache_behavior: Optional[
            Union[List[OrderedCacheBehavior], core.ArrayOut[OrderedCacheBehavior]]
        ] = core.arg(default=None)

        origin: Union[List[Origin], core.ArrayOut[Origin]] = core.arg()

        origin_group: Optional[Union[List[OriginGroup], core.ArrayOut[OriginGroup]]] = core.arg(
            default=None
        )

        price_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        restrictions: Restrictions = core.arg()

        retain_on_delete: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        viewer_certificate: ViewerCertificate = core.arg()

        wait_for_deployment: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        web_acl_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
