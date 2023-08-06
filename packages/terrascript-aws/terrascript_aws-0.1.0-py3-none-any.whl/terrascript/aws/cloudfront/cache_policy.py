from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Headers(core.Schema):

    items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Headers.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class HeadersConfig(core.Schema):

    header_behavior: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    headers: Optional[Headers] = core.attr(Headers, default=None)

    def __init__(
        self,
        *,
        header_behavior: Optional[Union[str, core.StringOut]] = None,
        headers: Optional[Headers] = None,
    ):
        super().__init__(
            args=HeadersConfig.Args(
                header_behavior=header_behavior,
                headers=headers,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        header_behavior: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        headers: Optional[Headers] = core.arg(default=None)


@core.schema
class QueryStrings(core.Schema):

    items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=QueryStrings.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class QueryStringsConfig(core.Schema):

    query_string_behavior: Union[str, core.StringOut] = core.attr(str)

    query_strings: Optional[QueryStrings] = core.attr(QueryStrings, default=None)

    def __init__(
        self,
        *,
        query_string_behavior: Union[str, core.StringOut],
        query_strings: Optional[QueryStrings] = None,
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

        query_strings: Optional[QueryStrings] = core.arg(default=None)


@core.schema
class Cookies(core.Schema):

    items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Cookies.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class CookiesConfig(core.Schema):

    cookie_behavior: Union[str, core.StringOut] = core.attr(str)

    cookies: Optional[Cookies] = core.attr(Cookies, default=None)

    def __init__(
        self,
        *,
        cookie_behavior: Union[str, core.StringOut],
        cookies: Optional[Cookies] = None,
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

        cookies: Optional[Cookies] = core.arg(default=None)


@core.schema
class ParametersInCacheKeyAndForwardedToOrigin(core.Schema):

    cookies_config: CookiesConfig = core.attr(CookiesConfig)

    enable_accept_encoding_brotli: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    enable_accept_encoding_gzip: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    headers_config: HeadersConfig = core.attr(HeadersConfig)

    query_strings_config: QueryStringsConfig = core.attr(QueryStringsConfig)

    def __init__(
        self,
        *,
        cookies_config: CookiesConfig,
        headers_config: HeadersConfig,
        query_strings_config: QueryStringsConfig,
        enable_accept_encoding_brotli: Optional[Union[bool, core.BoolOut]] = None,
        enable_accept_encoding_gzip: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=ParametersInCacheKeyAndForwardedToOrigin.Args(
                cookies_config=cookies_config,
                headers_config=headers_config,
                query_strings_config=query_strings_config,
                enable_accept_encoding_brotli=enable_accept_encoding_brotli,
                enable_accept_encoding_gzip=enable_accept_encoding_gzip,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookies_config: CookiesConfig = core.arg()

        enable_accept_encoding_brotli: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_accept_encoding_gzip: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        headers_config: HeadersConfig = core.arg()

        query_strings_config: QueryStringsConfig = core.arg()


@core.resource(type="aws_cloudfront_cache_policy", namespace="aws_cloudfront")
class CachePolicy(core.Resource):

    comment: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    default_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    etag: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    max_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    parameters_in_cache_key_and_forwarded_to_origin: ParametersInCacheKeyAndForwardedToOrigin = (
        core.attr(ParametersInCacheKeyAndForwardedToOrigin)
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        parameters_in_cache_key_and_forwarded_to_origin: ParametersInCacheKeyAndForwardedToOrigin,
        comment: Optional[Union[str, core.StringOut]] = None,
        default_ttl: Optional[Union[int, core.IntOut]] = None,
        max_ttl: Optional[Union[int, core.IntOut]] = None,
        min_ttl: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CachePolicy.Args(
                name=name,
                parameters_in_cache_key_and_forwarded_to_origin=parameters_in_cache_key_and_forwarded_to_origin,
                comment=comment,
                default_ttl=default_ttl,
                max_ttl=max_ttl,
                min_ttl=min_ttl,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        max_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        parameters_in_cache_key_and_forwarded_to_origin: ParametersInCacheKeyAndForwardedToOrigin = (
            core.arg()
        )
