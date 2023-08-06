from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ServerTimingHeadersConfig(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    sampling_rate: Union[float, core.FloatOut] = core.attr(float)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        sampling_rate: Union[float, core.FloatOut],
    ):
        super().__init__(
            args=ServerTimingHeadersConfig.Args(
                enabled=enabled,
                sampling_rate=sampling_rate,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        sampling_rate: Union[float, core.FloatOut] = core.arg()


@core.schema
class AccessControlAllowHeaders(core.Schema):

    items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AccessControlAllowHeaders.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class AccessControlAllowMethods(core.Schema):

    items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AccessControlAllowMethods.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class AccessControlAllowOrigins(core.Schema):

    items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AccessControlAllowOrigins.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class AccessControlExposeHeaders(core.Schema):

    items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AccessControlExposeHeaders.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class CorsConfig(core.Schema):

    access_control_allow_credentials: Union[bool, core.BoolOut] = core.attr(bool)

    access_control_allow_headers: AccessControlAllowHeaders = core.attr(AccessControlAllowHeaders)

    access_control_allow_methods: AccessControlAllowMethods = core.attr(AccessControlAllowMethods)

    access_control_allow_origins: AccessControlAllowOrigins = core.attr(AccessControlAllowOrigins)

    access_control_expose_headers: Optional[AccessControlExposeHeaders] = core.attr(
        AccessControlExposeHeaders, default=None
    )

    access_control_max_age_sec: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    origin_override: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        access_control_allow_credentials: Union[bool, core.BoolOut],
        access_control_allow_headers: AccessControlAllowHeaders,
        access_control_allow_methods: AccessControlAllowMethods,
        access_control_allow_origins: AccessControlAllowOrigins,
        origin_override: Union[bool, core.BoolOut],
        access_control_expose_headers: Optional[AccessControlExposeHeaders] = None,
        access_control_max_age_sec: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CorsConfig.Args(
                access_control_allow_credentials=access_control_allow_credentials,
                access_control_allow_headers=access_control_allow_headers,
                access_control_allow_methods=access_control_allow_methods,
                access_control_allow_origins=access_control_allow_origins,
                origin_override=origin_override,
                access_control_expose_headers=access_control_expose_headers,
                access_control_max_age_sec=access_control_max_age_sec,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_allow_credentials: Union[bool, core.BoolOut] = core.arg()

        access_control_allow_headers: AccessControlAllowHeaders = core.arg()

        access_control_allow_methods: AccessControlAllowMethods = core.arg()

        access_control_allow_origins: AccessControlAllowOrigins = core.arg()

        access_control_expose_headers: Optional[AccessControlExposeHeaders] = core.arg(default=None)

        access_control_max_age_sec: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        origin_override: Union[bool, core.BoolOut] = core.arg()


@core.schema
class Items(core.Schema):

    header: Union[str, core.StringOut] = core.attr(str)

    override: Union[bool, core.BoolOut] = core.attr(bool)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        header: Union[str, core.StringOut],
        override: Union[bool, core.BoolOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Items.Args(
                header=header,
                override=override,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        header: Union[str, core.StringOut] = core.arg()

        override: Union[bool, core.BoolOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class CustomHeadersConfig(core.Schema):

    items: Optional[Union[List[Items], core.ArrayOut[Items]]] = core.attr(
        Items, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Optional[Union[List[Items], core.ArrayOut[Items]]] = None,
    ):
        super().__init__(
            args=CustomHeadersConfig.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Optional[Union[List[Items], core.ArrayOut[Items]]] = core.arg(default=None)


@core.schema
class ReferrerPolicy(core.Schema):

    override: Union[bool, core.BoolOut] = core.attr(bool)

    referrer_policy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        override: Union[bool, core.BoolOut],
        referrer_policy: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ReferrerPolicy.Args(
                override=override,
                referrer_policy=referrer_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        override: Union[bool, core.BoolOut] = core.arg()

        referrer_policy: Union[str, core.StringOut] = core.arg()


@core.schema
class StrictTransportSecurity(core.Schema):

    access_control_max_age_sec: Union[int, core.IntOut] = core.attr(int)

    include_subdomains: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    override: Union[bool, core.BoolOut] = core.attr(bool)

    preload: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        access_control_max_age_sec: Union[int, core.IntOut],
        override: Union[bool, core.BoolOut],
        include_subdomains: Optional[Union[bool, core.BoolOut]] = None,
        preload: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=StrictTransportSecurity.Args(
                access_control_max_age_sec=access_control_max_age_sec,
                override=override,
                include_subdomains=include_subdomains,
                preload=preload,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_max_age_sec: Union[int, core.IntOut] = core.arg()

        include_subdomains: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        override: Union[bool, core.BoolOut] = core.arg()

        preload: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class XssProtection(core.Schema):

    mode_block: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    override: Union[bool, core.BoolOut] = core.attr(bool)

    protection: Union[bool, core.BoolOut] = core.attr(bool)

    report_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        override: Union[bool, core.BoolOut],
        protection: Union[bool, core.BoolOut],
        mode_block: Optional[Union[bool, core.BoolOut]] = None,
        report_uri: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=XssProtection.Args(
                override=override,
                protection=protection,
                mode_block=mode_block,
                report_uri=report_uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mode_block: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        override: Union[bool, core.BoolOut] = core.arg()

        protection: Union[bool, core.BoolOut] = core.arg()

        report_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ContentSecurityPolicy(core.Schema):

    content_security_policy: Union[str, core.StringOut] = core.attr(str)

    override: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        content_security_policy: Union[str, core.StringOut],
        override: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=ContentSecurityPolicy.Args(
                content_security_policy=content_security_policy,
                override=override,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_security_policy: Union[str, core.StringOut] = core.arg()

        override: Union[bool, core.BoolOut] = core.arg()


@core.schema
class ContentTypeOptions(core.Schema):

    override: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        override: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=ContentTypeOptions.Args(
                override=override,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        override: Union[bool, core.BoolOut] = core.arg()


@core.schema
class FrameOptions(core.Schema):

    frame_option: Union[str, core.StringOut] = core.attr(str)

    override: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        frame_option: Union[str, core.StringOut],
        override: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=FrameOptions.Args(
                frame_option=frame_option,
                override=override,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        frame_option: Union[str, core.StringOut] = core.arg()

        override: Union[bool, core.BoolOut] = core.arg()


@core.schema
class SecurityHeadersConfig(core.Schema):

    content_security_policy: Optional[ContentSecurityPolicy] = core.attr(
        ContentSecurityPolicy, default=None
    )

    content_type_options: Optional[ContentTypeOptions] = core.attr(ContentTypeOptions, default=None)

    frame_options: Optional[FrameOptions] = core.attr(FrameOptions, default=None)

    referrer_policy: Optional[ReferrerPolicy] = core.attr(ReferrerPolicy, default=None)

    strict_transport_security: Optional[StrictTransportSecurity] = core.attr(
        StrictTransportSecurity, default=None
    )

    xss_protection: Optional[XssProtection] = core.attr(XssProtection, default=None)

    def __init__(
        self,
        *,
        content_security_policy: Optional[ContentSecurityPolicy] = None,
        content_type_options: Optional[ContentTypeOptions] = None,
        frame_options: Optional[FrameOptions] = None,
        referrer_policy: Optional[ReferrerPolicy] = None,
        strict_transport_security: Optional[StrictTransportSecurity] = None,
        xss_protection: Optional[XssProtection] = None,
    ):
        super().__init__(
            args=SecurityHeadersConfig.Args(
                content_security_policy=content_security_policy,
                content_type_options=content_type_options,
                frame_options=frame_options,
                referrer_policy=referrer_policy,
                strict_transport_security=strict_transport_security,
                xss_protection=xss_protection,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_security_policy: Optional[ContentSecurityPolicy] = core.arg(default=None)

        content_type_options: Optional[ContentTypeOptions] = core.arg(default=None)

        frame_options: Optional[FrameOptions] = core.arg(default=None)

        referrer_policy: Optional[ReferrerPolicy] = core.arg(default=None)

        strict_transport_security: Optional[StrictTransportSecurity] = core.arg(default=None)

        xss_protection: Optional[XssProtection] = core.arg(default=None)


@core.resource(type="aws_cloudfront_response_headers_policy", namespace="aws_cloudfront")
class ResponseHeadersPolicy(core.Resource):

    comment: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cors_config: Optional[CorsConfig] = core.attr(CorsConfig, default=None)

    custom_headers_config: Optional[CustomHeadersConfig] = core.attr(
        CustomHeadersConfig, default=None
    )

    etag: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    security_headers_config: Optional[SecurityHeadersConfig] = core.attr(
        SecurityHeadersConfig, default=None
    )

    server_timing_headers_config: Optional[ServerTimingHeadersConfig] = core.attr(
        ServerTimingHeadersConfig, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        comment: Optional[Union[str, core.StringOut]] = None,
        cors_config: Optional[CorsConfig] = None,
        custom_headers_config: Optional[CustomHeadersConfig] = None,
        etag: Optional[Union[str, core.StringOut]] = None,
        security_headers_config: Optional[SecurityHeadersConfig] = None,
        server_timing_headers_config: Optional[ServerTimingHeadersConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResponseHeadersPolicy.Args(
                name=name,
                comment=comment,
                cors_config=cors_config,
                custom_headers_config=custom_headers_config,
                etag=etag,
                security_headers_config=security_headers_config,
                server_timing_headers_config=server_timing_headers_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cors_config: Optional[CorsConfig] = core.arg(default=None)

        custom_headers_config: Optional[CustomHeadersConfig] = core.arg(default=None)

        etag: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        security_headers_config: Optional[SecurityHeadersConfig] = core.arg(default=None)

        server_timing_headers_config: Optional[ServerTimingHeadersConfig] = core.arg(default=None)
