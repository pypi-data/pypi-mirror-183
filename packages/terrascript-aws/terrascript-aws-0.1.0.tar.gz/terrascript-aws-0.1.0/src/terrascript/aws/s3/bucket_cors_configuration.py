from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class CorsRule(core.Schema):

    allowed_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allowed_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    allowed_origins: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    expose_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_age_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        allowed_methods: Union[List[str], core.ArrayOut[core.StringOut]],
        allowed_origins: Union[List[str], core.ArrayOut[core.StringOut]],
        allowed_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        expose_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        max_age_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CorsRule.Args(
                allowed_methods=allowed_methods,
                allowed_origins=allowed_origins,
                allowed_headers=allowed_headers,
                expose_headers=expose_headers,
                id=id,
                max_age_seconds=max_age_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allowed_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        allowed_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        allowed_origins: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        expose_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_age_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_s3_bucket_cors_configuration", namespace="aws_s3")
class BucketCorsConfiguration(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    cors_rule: Union[List[CorsRule], core.ArrayOut[CorsRule]] = core.attr(
        CorsRule, kind=core.Kind.array
    )

    expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        cors_rule: Union[List[CorsRule], core.ArrayOut[CorsRule]],
        expected_bucket_owner: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketCorsConfiguration.Args(
                bucket=bucket,
                cors_rule=cors_rule,
                expected_bucket_owner=expected_bucket_owner,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        cors_rule: Union[List[CorsRule], core.ArrayOut[CorsRule]] = core.arg()

        expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)
