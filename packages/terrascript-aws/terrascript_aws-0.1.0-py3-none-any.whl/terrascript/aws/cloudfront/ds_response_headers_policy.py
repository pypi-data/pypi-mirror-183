from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ServerTimingHeadersConfig(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    sampling_rate: Union[float, core.FloatOut] = core.attr(float, computed=True)

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

    items: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=AccessControlAllowHeaders.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class AccessControlAllowMethods(core.Schema):

    items: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=AccessControlAllowMethods.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class AccessControlAllowOrigins(core.Schema):

    items: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=AccessControlAllowOrigins.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class AccessControlExposeHeaders(core.Schema):

    items: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=AccessControlExposeHeaders.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class CorsConfig(core.Schema):

    access_control_allow_credentials: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    access_control_allow_headers: Union[
        List[AccessControlAllowHeaders], core.ArrayOut[AccessControlAllowHeaders]
    ] = core.attr(AccessControlAllowHeaders, computed=True, kind=core.Kind.array)

    access_control_allow_methods: Union[
        List[AccessControlAllowMethods], core.ArrayOut[AccessControlAllowMethods]
    ] = core.attr(AccessControlAllowMethods, computed=True, kind=core.Kind.array)

    access_control_allow_origins: Union[
        List[AccessControlAllowOrigins], core.ArrayOut[AccessControlAllowOrigins]
    ] = core.attr(AccessControlAllowOrigins, computed=True, kind=core.Kind.array)

    access_control_expose_headers: Union[
        List[AccessControlExposeHeaders], core.ArrayOut[AccessControlExposeHeaders]
    ] = core.attr(AccessControlExposeHeaders, computed=True, kind=core.Kind.array)

    access_control_max_age_sec: Union[int, core.IntOut] = core.attr(int, computed=True)

    origin_override: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        access_control_allow_credentials: Union[bool, core.BoolOut],
        access_control_allow_headers: Union[
            List[AccessControlAllowHeaders], core.ArrayOut[AccessControlAllowHeaders]
        ],
        access_control_allow_methods: Union[
            List[AccessControlAllowMethods], core.ArrayOut[AccessControlAllowMethods]
        ],
        access_control_allow_origins: Union[
            List[AccessControlAllowOrigins], core.ArrayOut[AccessControlAllowOrigins]
        ],
        access_control_expose_headers: Union[
            List[AccessControlExposeHeaders], core.ArrayOut[AccessControlExposeHeaders]
        ],
        access_control_max_age_sec: Union[int, core.IntOut],
        origin_override: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=CorsConfig.Args(
                access_control_allow_credentials=access_control_allow_credentials,
                access_control_allow_headers=access_control_allow_headers,
                access_control_allow_methods=access_control_allow_methods,
                access_control_allow_origins=access_control_allow_origins,
                access_control_expose_headers=access_control_expose_headers,
                access_control_max_age_sec=access_control_max_age_sec,
                origin_override=origin_override,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_allow_credentials: Union[bool, core.BoolOut] = core.arg()

        access_control_allow_headers: Union[
            List[AccessControlAllowHeaders], core.ArrayOut[AccessControlAllowHeaders]
        ] = core.arg()

        access_control_allow_methods: Union[
            List[AccessControlAllowMethods], core.ArrayOut[AccessControlAllowMethods]
        ] = core.arg()

        access_control_allow_origins: Union[
            List[AccessControlAllowOrigins], core.ArrayOut[AccessControlAllowOrigins]
        ] = core.arg()

        access_control_expose_headers: Union[
            List[AccessControlExposeHeaders], core.ArrayOut[AccessControlExposeHeaders]
        ] = core.arg()

        access_control_max_age_sec: Union[int, core.IntOut] = core.arg()

        origin_override: Union[bool, core.BoolOut] = core.arg()


@core.schema
class Items(core.Schema):

    header: Union[str, core.StringOut] = core.attr(str, computed=True)

    override: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    value: Union[str, core.StringOut] = core.attr(str, computed=True)

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

    items: Union[List[Items], core.ArrayOut[Items]] = core.attr(
        Items, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Union[List[Items], core.ArrayOut[Items]],
    ):
        super().__init__(
            args=CustomHeadersConfig.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Union[List[Items], core.ArrayOut[Items]] = core.arg()


@core.schema
class XssProtection(core.Schema):

    mode_block: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    override: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    protection: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    report_uri: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        mode_block: Union[bool, core.BoolOut],
        override: Union[bool, core.BoolOut],
        protection: Union[bool, core.BoolOut],
        report_uri: Union[str, core.StringOut],
    ):
        super().__init__(
            args=XssProtection.Args(
                mode_block=mode_block,
                override=override,
                protection=protection,
                report_uri=report_uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mode_block: Union[bool, core.BoolOut] = core.arg()

        override: Union[bool, core.BoolOut] = core.arg()

        protection: Union[bool, core.BoolOut] = core.arg()

        report_uri: Union[str, core.StringOut] = core.arg()


@core.schema
class ContentSecurityPolicy(core.Schema):

    content_security_policy: Union[str, core.StringOut] = core.attr(str, computed=True)

    override: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

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

    override: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

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

    frame_option: Union[str, core.StringOut] = core.attr(str, computed=True)

    override: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

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
class ReferrerPolicy(core.Schema):

    override: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    referrer_policy: Union[str, core.StringOut] = core.attr(str, computed=True)

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

    access_control_max_age_sec: Union[int, core.IntOut] = core.attr(int, computed=True)

    include_subdomains: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    override: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    preload: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        access_control_max_age_sec: Union[int, core.IntOut],
        include_subdomains: Union[bool, core.BoolOut],
        override: Union[bool, core.BoolOut],
        preload: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=StrictTransportSecurity.Args(
                access_control_max_age_sec=access_control_max_age_sec,
                include_subdomains=include_subdomains,
                override=override,
                preload=preload,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_max_age_sec: Union[int, core.IntOut] = core.arg()

        include_subdomains: Union[bool, core.BoolOut] = core.arg()

        override: Union[bool, core.BoolOut] = core.arg()

        preload: Union[bool, core.BoolOut] = core.arg()


@core.schema
class SecurityHeadersConfig(core.Schema):

    content_security_policy: Union[
        List[ContentSecurityPolicy], core.ArrayOut[ContentSecurityPolicy]
    ] = core.attr(ContentSecurityPolicy, computed=True, kind=core.Kind.array)

    content_type_options: Union[
        List[ContentTypeOptions], core.ArrayOut[ContentTypeOptions]
    ] = core.attr(ContentTypeOptions, computed=True, kind=core.Kind.array)

    frame_options: Union[List[FrameOptions], core.ArrayOut[FrameOptions]] = core.attr(
        FrameOptions, computed=True, kind=core.Kind.array
    )

    referrer_policy: Union[List[ReferrerPolicy], core.ArrayOut[ReferrerPolicy]] = core.attr(
        ReferrerPolicy, computed=True, kind=core.Kind.array
    )

    strict_transport_security: Union[
        List[StrictTransportSecurity], core.ArrayOut[StrictTransportSecurity]
    ] = core.attr(StrictTransportSecurity, computed=True, kind=core.Kind.array)

    xss_protection: Union[List[XssProtection], core.ArrayOut[XssProtection]] = core.attr(
        XssProtection, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        content_security_policy: Union[
            List[ContentSecurityPolicy], core.ArrayOut[ContentSecurityPolicy]
        ],
        content_type_options: Union[List[ContentTypeOptions], core.ArrayOut[ContentTypeOptions]],
        frame_options: Union[List[FrameOptions], core.ArrayOut[FrameOptions]],
        referrer_policy: Union[List[ReferrerPolicy], core.ArrayOut[ReferrerPolicy]],
        strict_transport_security: Union[
            List[StrictTransportSecurity], core.ArrayOut[StrictTransportSecurity]
        ],
        xss_protection: Union[List[XssProtection], core.ArrayOut[XssProtection]],
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
        content_security_policy: Union[
            List[ContentSecurityPolicy], core.ArrayOut[ContentSecurityPolicy]
        ] = core.arg()

        content_type_options: Union[
            List[ContentTypeOptions], core.ArrayOut[ContentTypeOptions]
        ] = core.arg()

        frame_options: Union[List[FrameOptions], core.ArrayOut[FrameOptions]] = core.arg()

        referrer_policy: Union[List[ReferrerPolicy], core.ArrayOut[ReferrerPolicy]] = core.arg()

        strict_transport_security: Union[
            List[StrictTransportSecurity], core.ArrayOut[StrictTransportSecurity]
        ] = core.arg()

        xss_protection: Union[List[XssProtection], core.ArrayOut[XssProtection]] = core.arg()


@core.data(type="aws_cloudfront_response_headers_policy", namespace="aws_cloudfront")
class DsResponseHeadersPolicy(core.Data):

    comment: Union[str, core.StringOut] = core.attr(str, computed=True)

    cors_config: Union[List[CorsConfig], core.ArrayOut[CorsConfig]] = core.attr(
        CorsConfig, computed=True, kind=core.Kind.array
    )

    custom_headers_config: Union[
        List[CustomHeadersConfig], core.ArrayOut[CustomHeadersConfig]
    ] = core.attr(CustomHeadersConfig, computed=True, kind=core.Kind.array)

    etag: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    security_headers_config: Union[
        List[SecurityHeadersConfig], core.ArrayOut[SecurityHeadersConfig]
    ] = core.attr(SecurityHeadersConfig, computed=True, kind=core.Kind.array)

    server_timing_headers_config: Union[
        List[ServerTimingHeadersConfig], core.ArrayOut[ServerTimingHeadersConfig]
    ] = core.attr(ServerTimingHeadersConfig, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        data_name: str,
        *,
        id: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsResponseHeadersPolicy.Args(
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
