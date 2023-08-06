from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class RedirectAllRequestsTo(core.Schema):

    host_name: Union[str, core.StringOut] = core.attr(str)

    protocol: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        host_name: Union[str, core.StringOut],
        protocol: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RedirectAllRequestsTo.Args(
                host_name=host_name,
                protocol=protocol,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host_name: Union[str, core.StringOut] = core.arg()

        protocol: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Redirect(core.Schema):

    host_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    http_redirect_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    protocol: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    replace_key_prefix_with: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    replace_key_with: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        host_name: Optional[Union[str, core.StringOut]] = None,
        http_redirect_code: Optional[Union[str, core.StringOut]] = None,
        protocol: Optional[Union[str, core.StringOut]] = None,
        replace_key_prefix_with: Optional[Union[str, core.StringOut]] = None,
        replace_key_with: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Redirect.Args(
                host_name=host_name,
                http_redirect_code=http_redirect_code,
                protocol=protocol,
                replace_key_prefix_with=replace_key_prefix_with,
                replace_key_with=replace_key_with,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        http_redirect_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        protocol: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        replace_key_prefix_with: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        replace_key_with: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Condition(core.Schema):

    http_error_code_returned_equals: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    key_prefix_equals: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        http_error_code_returned_equals: Optional[Union[str, core.StringOut]] = None,
        key_prefix_equals: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Condition.Args(
                http_error_code_returned_equals=http_error_code_returned_equals,
                key_prefix_equals=key_prefix_equals,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_error_code_returned_equals: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        key_prefix_equals: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RoutingRule(core.Schema):

    condition: Optional[Condition] = core.attr(Condition, default=None)

    redirect: Redirect = core.attr(Redirect)

    def __init__(
        self,
        *,
        redirect: Redirect,
        condition: Optional[Condition] = None,
    ):
        super().__init__(
            args=RoutingRule.Args(
                redirect=redirect,
                condition=condition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        condition: Optional[Condition] = core.arg(default=None)

        redirect: Redirect = core.arg()


@core.schema
class ErrorDocument(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ErrorDocument.Args(
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()


@core.schema
class IndexDocument(core.Schema):

    suffix: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        suffix: Union[str, core.StringOut],
    ):
        super().__init__(
            args=IndexDocument.Args(
                suffix=suffix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        suffix: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_s3_bucket_website_configuration", namespace="aws_s3")
class BucketWebsiteConfiguration(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    error_document: Optional[ErrorDocument] = core.attr(ErrorDocument, default=None)

    expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_document: Optional[IndexDocument] = core.attr(IndexDocument, default=None)

    redirect_all_requests_to: Optional[RedirectAllRequestsTo] = core.attr(
        RedirectAllRequestsTo, default=None
    )

    routing_rule: Optional[Union[List[RoutingRule], core.ArrayOut[RoutingRule]]] = core.attr(
        RoutingRule, default=None, computed=True, kind=core.Kind.array
    )

    routing_rules: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    website_domain: Union[str, core.StringOut] = core.attr(str, computed=True)

    website_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        error_document: Optional[ErrorDocument] = None,
        expected_bucket_owner: Optional[Union[str, core.StringOut]] = None,
        index_document: Optional[IndexDocument] = None,
        redirect_all_requests_to: Optional[RedirectAllRequestsTo] = None,
        routing_rule: Optional[Union[List[RoutingRule], core.ArrayOut[RoutingRule]]] = None,
        routing_rules: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketWebsiteConfiguration.Args(
                bucket=bucket,
                error_document=error_document,
                expected_bucket_owner=expected_bucket_owner,
                index_document=index_document,
                redirect_all_requests_to=redirect_all_requests_to,
                routing_rule=routing_rule,
                routing_rules=routing_rules,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        error_document: Optional[ErrorDocument] = core.arg(default=None)

        expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        index_document: Optional[IndexDocument] = core.arg(default=None)

        redirect_all_requests_to: Optional[RedirectAllRequestsTo] = core.arg(default=None)

        routing_rule: Optional[Union[List[RoutingRule], core.ArrayOut[RoutingRule]]] = core.arg(
            default=None
        )

        routing_rules: Optional[Union[str, core.StringOut]] = core.arg(default=None)
