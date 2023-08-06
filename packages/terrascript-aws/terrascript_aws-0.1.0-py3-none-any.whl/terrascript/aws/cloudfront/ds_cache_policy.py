from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Headers(core.Schema):

    items: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Headers.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class HeadersConfig(core.Schema):

    header_behavior: Union[str, core.StringOut] = core.attr(str, computed=True)

    headers: Union[List[Headers], core.ArrayOut[Headers]] = core.attr(
        Headers, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        header_behavior: Union[str, core.StringOut],
        headers: Union[List[Headers], core.ArrayOut[Headers]],
    ):
        super().__init__(
            args=HeadersConfig.Args(
                header_behavior=header_behavior,
                headers=headers,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        header_behavior: Union[str, core.StringOut] = core.arg()

        headers: Union[List[Headers], core.ArrayOut[Headers]] = core.arg()


@core.schema
class QueryStrings(core.Schema):

    items: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=QueryStrings.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class QueryStringsConfig(core.Schema):

    query_string_behavior: Union[str, core.StringOut] = core.attr(str, computed=True)

    query_strings: Union[List[QueryStrings], core.ArrayOut[QueryStrings]] = core.attr(
        QueryStrings, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        query_string_behavior: Union[str, core.StringOut],
        query_strings: Union[List[QueryStrings], core.ArrayOut[QueryStrings]],
    ):
        super().__init__(
            args=QueryStringsConfig.Args(
                query_string_behavior=query_string_behavior,
                query_strings=query_strings,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        query_string_behavior: Union[str, core.StringOut] = core.arg()

        query_strings: Union[List[QueryStrings], core.ArrayOut[QueryStrings]] = core.arg()


@core.schema
class Cookies(core.Schema):

    items: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Cookies.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class CookiesConfig(core.Schema):

    cookie_behavior: Union[str, core.StringOut] = core.attr(str, computed=True)

    cookies: Union[List[Cookies], core.ArrayOut[Cookies]] = core.attr(
        Cookies, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cookie_behavior: Union[str, core.StringOut],
        cookies: Union[List[Cookies], core.ArrayOut[Cookies]],
    ):
        super().__init__(
            args=CookiesConfig.Args(
                cookie_behavior=cookie_behavior,
                cookies=cookies,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookie_behavior: Union[str, core.StringOut] = core.arg()

        cookies: Union[List[Cookies], core.ArrayOut[Cookies]] = core.arg()


@core.schema
class ParametersInCacheKeyAndForwardedToOrigin(core.Schema):

    cookies_config: Union[List[CookiesConfig], core.ArrayOut[CookiesConfig]] = core.attr(
        CookiesConfig, computed=True, kind=core.Kind.array
    )

    enable_accept_encoding_brotli: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    enable_accept_encoding_gzip: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    headers_config: Union[List[HeadersConfig], core.ArrayOut[HeadersConfig]] = core.attr(
        HeadersConfig, computed=True, kind=core.Kind.array
    )

    query_strings_config: Union[
        List[QueryStringsConfig], core.ArrayOut[QueryStringsConfig]
    ] = core.attr(QueryStringsConfig, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        cookies_config: Union[List[CookiesConfig], core.ArrayOut[CookiesConfig]],
        enable_accept_encoding_brotli: Union[bool, core.BoolOut],
        enable_accept_encoding_gzip: Union[bool, core.BoolOut],
        headers_config: Union[List[HeadersConfig], core.ArrayOut[HeadersConfig]],
        query_strings_config: Union[List[QueryStringsConfig], core.ArrayOut[QueryStringsConfig]],
    ):
        super().__init__(
            args=ParametersInCacheKeyAndForwardedToOrigin.Args(
                cookies_config=cookies_config,
                enable_accept_encoding_brotli=enable_accept_encoding_brotli,
                enable_accept_encoding_gzip=enable_accept_encoding_gzip,
                headers_config=headers_config,
                query_strings_config=query_strings_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookies_config: Union[List[CookiesConfig], core.ArrayOut[CookiesConfig]] = core.arg()

        enable_accept_encoding_brotli: Union[bool, core.BoolOut] = core.arg()

        enable_accept_encoding_gzip: Union[bool, core.BoolOut] = core.arg()

        headers_config: Union[List[HeadersConfig], core.ArrayOut[HeadersConfig]] = core.arg()

        query_strings_config: Union[
            List[QueryStringsConfig], core.ArrayOut[QueryStringsConfig]
        ] = core.arg()


@core.data(type="aws_cloudfront_cache_policy", namespace="aws_cloudfront")
class DsCachePolicy(core.Data):

    comment: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_ttl: Union[int, core.IntOut] = core.attr(int, computed=True)

    etag: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_ttl: Union[int, core.IntOut] = core.attr(int, computed=True)

    min_ttl: Union[int, core.IntOut] = core.attr(int, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    parameters_in_cache_key_and_forwarded_to_origin: Union[
        List[ParametersInCacheKeyAndForwardedToOrigin],
        core.ArrayOut[ParametersInCacheKeyAndForwardedToOrigin],
    ] = core.attr(ParametersInCacheKeyAndForwardedToOrigin, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        data_name: str,
        *,
        id: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCachePolicy.Args(
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
