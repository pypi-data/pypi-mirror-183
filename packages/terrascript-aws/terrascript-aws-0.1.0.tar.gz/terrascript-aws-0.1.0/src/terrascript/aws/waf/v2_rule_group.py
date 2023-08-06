from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CustomResponseBody(core.Schema):

    content: Union[str, core.StringOut] = core.attr(str)

    content_type: Union[str, core.StringOut] = core.attr(str)

    key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        content: Union[str, core.StringOut],
        content_type: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CustomResponseBody.Args(
                content=content,
                content_type=content_type,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content: Union[str, core.StringOut] = core.arg()

        content_type: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()


@core.schema
class RuleLabel(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RuleLabel.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()


@core.schema
class SingleQueryArgument(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SingleQueryArgument.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()


@core.schema
class UriPath(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class AllQueryArguments(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class Body(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class Method(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class QueryString(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class SingleHeader(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SingleHeader.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()


@core.schema
class FieldToMatch(core.Schema):

    all_query_arguments: Optional[AllQueryArguments] = core.attr(AllQueryArguments, default=None)

    body: Optional[Body] = core.attr(Body, default=None)

    method: Optional[Method] = core.attr(Method, default=None)

    query_string: Optional[QueryString] = core.attr(QueryString, default=None)

    single_header: Optional[SingleHeader] = core.attr(SingleHeader, default=None)

    single_query_argument: Optional[SingleQueryArgument] = core.attr(
        SingleQueryArgument, default=None
    )

    uri_path: Optional[UriPath] = core.attr(UriPath, default=None)

    def __init__(
        self,
        *,
        all_query_arguments: Optional[AllQueryArguments] = None,
        body: Optional[Body] = None,
        method: Optional[Method] = None,
        query_string: Optional[QueryString] = None,
        single_header: Optional[SingleHeader] = None,
        single_query_argument: Optional[SingleQueryArgument] = None,
        uri_path: Optional[UriPath] = None,
    ):
        super().__init__(
            args=FieldToMatch.Args(
                all_query_arguments=all_query_arguments,
                body=body,
                method=method,
                query_string=query_string,
                single_header=single_header,
                single_query_argument=single_query_argument,
                uri_path=uri_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        all_query_arguments: Optional[AllQueryArguments] = core.arg(default=None)

        body: Optional[Body] = core.arg(default=None)

        method: Optional[Method] = core.arg(default=None)

        query_string: Optional[QueryString] = core.arg(default=None)

        single_header: Optional[SingleHeader] = core.arg(default=None)

        single_query_argument: Optional[SingleQueryArgument] = core.arg(default=None)

        uri_path: Optional[UriPath] = core.arg(default=None)


@core.schema
class TextTransformation(core.Schema):

    priority: Union[int, core.IntOut] = core.attr(int)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        priority: Union[int, core.IntOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TextTransformation.Args(
                priority=priority,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        priority: Union[int, core.IntOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class SqliMatchStatement(core.Schema):

    field_to_match: Optional[FieldToMatch] = core.attr(FieldToMatch, default=None)

    text_transformation: Union[
        List[TextTransformation], core.ArrayOut[TextTransformation]
    ] = core.attr(TextTransformation, kind=core.Kind.array)

    def __init__(
        self,
        *,
        text_transformation: Union[List[TextTransformation], core.ArrayOut[TextTransformation]],
        field_to_match: Optional[FieldToMatch] = None,
    ):
        super().__init__(
            args=SqliMatchStatement.Args(
                text_transformation=text_transformation,
                field_to_match=field_to_match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: Optional[FieldToMatch] = core.arg(default=None)

        text_transformation: Union[
            List[TextTransformation], core.ArrayOut[TextTransformation]
        ] = core.arg()


@core.schema
class XssMatchStatement(core.Schema):

    field_to_match: Optional[FieldToMatch] = core.attr(FieldToMatch, default=None)

    text_transformation: Union[
        List[TextTransformation], core.ArrayOut[TextTransformation]
    ] = core.attr(TextTransformation, kind=core.Kind.array)

    def __init__(
        self,
        *,
        text_transformation: Union[List[TextTransformation], core.ArrayOut[TextTransformation]],
        field_to_match: Optional[FieldToMatch] = None,
    ):
        super().__init__(
            args=XssMatchStatement.Args(
                text_transformation=text_transformation,
                field_to_match=field_to_match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: Optional[FieldToMatch] = core.arg(default=None)

        text_transformation: Union[
            List[TextTransformation], core.ArrayOut[TextTransformation]
        ] = core.arg()


@core.schema
class ByteMatchStatement(core.Schema):

    field_to_match: Optional[FieldToMatch] = core.attr(FieldToMatch, default=None)

    positional_constraint: Union[str, core.StringOut] = core.attr(str)

    search_string: Union[str, core.StringOut] = core.attr(str)

    text_transformation: Union[
        List[TextTransformation], core.ArrayOut[TextTransformation]
    ] = core.attr(TextTransformation, kind=core.Kind.array)

    def __init__(
        self,
        *,
        positional_constraint: Union[str, core.StringOut],
        search_string: Union[str, core.StringOut],
        text_transformation: Union[List[TextTransformation], core.ArrayOut[TextTransformation]],
        field_to_match: Optional[FieldToMatch] = None,
    ):
        super().__init__(
            args=ByteMatchStatement.Args(
                positional_constraint=positional_constraint,
                search_string=search_string,
                text_transformation=text_transformation,
                field_to_match=field_to_match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: Optional[FieldToMatch] = core.arg(default=None)

        positional_constraint: Union[str, core.StringOut] = core.arg()

        search_string: Union[str, core.StringOut] = core.arg()

        text_transformation: Union[
            List[TextTransformation], core.ArrayOut[TextTransformation]
        ] = core.arg()


@core.schema
class ForwardedIpConfig(core.Schema):

    fallback_behavior: Union[str, core.StringOut] = core.attr(str)

    header_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        fallback_behavior: Union[str, core.StringOut],
        header_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ForwardedIpConfig.Args(
                fallback_behavior=fallback_behavior,
                header_name=header_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        fallback_behavior: Union[str, core.StringOut] = core.arg()

        header_name: Union[str, core.StringOut] = core.arg()


@core.schema
class GeoMatchStatement(core.Schema):

    country_codes: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    forwarded_ip_config: Optional[ForwardedIpConfig] = core.attr(ForwardedIpConfig, default=None)

    def __init__(
        self,
        *,
        country_codes: Union[List[str], core.ArrayOut[core.StringOut]],
        forwarded_ip_config: Optional[ForwardedIpConfig] = None,
    ):
        super().__init__(
            args=GeoMatchStatement.Args(
                country_codes=country_codes,
                forwarded_ip_config=forwarded_ip_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        country_codes: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        forwarded_ip_config: Optional[ForwardedIpConfig] = core.arg(default=None)


@core.schema
class IpSetForwardedIpConfig(core.Schema):

    fallback_behavior: Union[str, core.StringOut] = core.attr(str)

    header_name: Union[str, core.StringOut] = core.attr(str)

    position: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        fallback_behavior: Union[str, core.StringOut],
        header_name: Union[str, core.StringOut],
        position: Union[str, core.StringOut],
    ):
        super().__init__(
            args=IpSetForwardedIpConfig.Args(
                fallback_behavior=fallback_behavior,
                header_name=header_name,
                position=position,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        fallback_behavior: Union[str, core.StringOut] = core.arg()

        header_name: Union[str, core.StringOut] = core.arg()

        position: Union[str, core.StringOut] = core.arg()


@core.schema
class IpSetReferenceStatement(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str)

    ip_set_forwarded_ip_config: Optional[IpSetForwardedIpConfig] = core.attr(
        IpSetForwardedIpConfig, default=None
    )

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        ip_set_forwarded_ip_config: Optional[IpSetForwardedIpConfig] = None,
    ):
        super().__init__(
            args=IpSetReferenceStatement.Args(
                arn=arn,
                ip_set_forwarded_ip_config=ip_set_forwarded_ip_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        ip_set_forwarded_ip_config: Optional[IpSetForwardedIpConfig] = core.arg(default=None)


@core.schema
class LabelMatchStatement(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    scope: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        scope: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LabelMatchStatement.Args(
                key=key,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        scope: Union[str, core.StringOut] = core.arg()


@core.schema
class RegexPatternSetReferenceStatement(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str)

    field_to_match: Optional[FieldToMatch] = core.attr(FieldToMatch, default=None)

    text_transformation: Union[
        List[TextTransformation], core.ArrayOut[TextTransformation]
    ] = core.attr(TextTransformation, kind=core.Kind.array)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        text_transformation: Union[List[TextTransformation], core.ArrayOut[TextTransformation]],
        field_to_match: Optional[FieldToMatch] = None,
    ):
        super().__init__(
            args=RegexPatternSetReferenceStatement.Args(
                arn=arn,
                text_transformation=text_transformation,
                field_to_match=field_to_match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        field_to_match: Optional[FieldToMatch] = core.arg(default=None)

        text_transformation: Union[
            List[TextTransformation], core.ArrayOut[TextTransformation]
        ] = core.arg()


@core.schema
class SizeConstraintStatement(core.Schema):

    comparison_operator: Union[str, core.StringOut] = core.attr(str)

    field_to_match: Optional[FieldToMatch] = core.attr(FieldToMatch, default=None)

    size: Union[int, core.IntOut] = core.attr(int)

    text_transformation: Union[
        List[TextTransformation], core.ArrayOut[TextTransformation]
    ] = core.attr(TextTransformation, kind=core.Kind.array)

    def __init__(
        self,
        *,
        comparison_operator: Union[str, core.StringOut],
        size: Union[int, core.IntOut],
        text_transformation: Union[List[TextTransformation], core.ArrayOut[TextTransformation]],
        field_to_match: Optional[FieldToMatch] = None,
    ):
        super().__init__(
            args=SizeConstraintStatement.Args(
                comparison_operator=comparison_operator,
                size=size,
                text_transformation=text_transformation,
                field_to_match=field_to_match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison_operator: Union[str, core.StringOut] = core.arg()

        field_to_match: Optional[FieldToMatch] = core.arg(default=None)

        size: Union[int, core.IntOut] = core.arg()

        text_transformation: Union[
            List[TextTransformation], core.ArrayOut[TextTransformation]
        ] = core.arg()


@core.schema
class RuleStatementAndStatementStatementAndStatementStatement(core.Schema):

    byte_match_statement: Optional[ByteMatchStatement] = core.attr(ByteMatchStatement, default=None)

    geo_match_statement: Optional[GeoMatchStatement] = core.attr(GeoMatchStatement, default=None)

    ip_set_reference_statement: Optional[IpSetReferenceStatement] = core.attr(
        IpSetReferenceStatement, default=None
    )

    label_match_statement: Optional[LabelMatchStatement] = core.attr(
        LabelMatchStatement, default=None
    )

    regex_pattern_set_reference_statement: Optional[RegexPatternSetReferenceStatement] = core.attr(
        RegexPatternSetReferenceStatement, default=None
    )

    size_constraint_statement: Optional[SizeConstraintStatement] = core.attr(
        SizeConstraintStatement, default=None
    )

    sqli_match_statement: Optional[SqliMatchStatement] = core.attr(SqliMatchStatement, default=None)

    xss_match_statement: Optional[XssMatchStatement] = core.attr(XssMatchStatement, default=None)

    def __init__(
        self,
        *,
        byte_match_statement: Optional[ByteMatchStatement] = None,
        geo_match_statement: Optional[GeoMatchStatement] = None,
        ip_set_reference_statement: Optional[IpSetReferenceStatement] = None,
        label_match_statement: Optional[LabelMatchStatement] = None,
        regex_pattern_set_reference_statement: Optional[RegexPatternSetReferenceStatement] = None,
        size_constraint_statement: Optional[SizeConstraintStatement] = None,
        sqli_match_statement: Optional[SqliMatchStatement] = None,
        xss_match_statement: Optional[XssMatchStatement] = None,
    ):
        super().__init__(
            args=RuleStatementAndStatementStatementAndStatementStatement.Args(
                byte_match_statement=byte_match_statement,
                geo_match_statement=geo_match_statement,
                ip_set_reference_statement=ip_set_reference_statement,
                label_match_statement=label_match_statement,
                regex_pattern_set_reference_statement=regex_pattern_set_reference_statement,
                size_constraint_statement=size_constraint_statement,
                sqli_match_statement=sqli_match_statement,
                xss_match_statement=xss_match_statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        byte_match_statement: Optional[ByteMatchStatement] = core.arg(default=None)

        geo_match_statement: Optional[GeoMatchStatement] = core.arg(default=None)

        ip_set_reference_statement: Optional[IpSetReferenceStatement] = core.arg(default=None)

        label_match_statement: Optional[LabelMatchStatement] = core.arg(default=None)

        regex_pattern_set_reference_statement: Optional[
            RegexPatternSetReferenceStatement
        ] = core.arg(default=None)

        size_constraint_statement: Optional[SizeConstraintStatement] = core.arg(default=None)

        sqli_match_statement: Optional[SqliMatchStatement] = core.arg(default=None)

        xss_match_statement: Optional[XssMatchStatement] = core.arg(default=None)


@core.schema
class RuleStatementAndStatementStatementAndStatement(core.Schema):

    statement: Union[
        List[RuleStatementAndStatementStatementAndStatementStatement],
        core.ArrayOut[RuleStatementAndStatementStatementAndStatementStatement],
    ] = core.attr(RuleStatementAndStatementStatementAndStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: Union[
            List[RuleStatementAndStatementStatementAndStatementStatement],
            core.ArrayOut[RuleStatementAndStatementStatementAndStatementStatement],
        ],
    ):
        super().__init__(
            args=RuleStatementAndStatementStatementAndStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: Union[
            List[RuleStatementAndStatementStatementAndStatementStatement],
            core.ArrayOut[RuleStatementAndStatementStatementAndStatementStatement],
        ] = core.arg()


@core.schema
class RuleStatementAndStatementStatementNotStatement(core.Schema):

    statement: Union[
        List[RuleStatementAndStatementStatementAndStatementStatement],
        core.ArrayOut[RuleStatementAndStatementStatementAndStatementStatement],
    ] = core.attr(RuleStatementAndStatementStatementAndStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: Union[
            List[RuleStatementAndStatementStatementAndStatementStatement],
            core.ArrayOut[RuleStatementAndStatementStatementAndStatementStatement],
        ],
    ):
        super().__init__(
            args=RuleStatementAndStatementStatementNotStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: Union[
            List[RuleStatementAndStatementStatementAndStatementStatement],
            core.ArrayOut[RuleStatementAndStatementStatementAndStatementStatement],
        ] = core.arg()


@core.schema
class RuleStatementAndStatementStatementOrStatement(core.Schema):

    statement: Union[
        List[RuleStatementAndStatementStatementAndStatementStatement],
        core.ArrayOut[RuleStatementAndStatementStatementAndStatementStatement],
    ] = core.attr(RuleStatementAndStatementStatementAndStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: Union[
            List[RuleStatementAndStatementStatementAndStatementStatement],
            core.ArrayOut[RuleStatementAndStatementStatementAndStatementStatement],
        ],
    ):
        super().__init__(
            args=RuleStatementAndStatementStatementOrStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: Union[
            List[RuleStatementAndStatementStatementAndStatementStatement],
            core.ArrayOut[RuleStatementAndStatementStatementAndStatementStatement],
        ] = core.arg()


@core.schema
class RuleStatementAndStatementStatement(core.Schema):

    and_statement: Optional[RuleStatementAndStatementStatementAndStatement] = core.attr(
        RuleStatementAndStatementStatementAndStatement, default=None
    )

    byte_match_statement: Optional[ByteMatchStatement] = core.attr(ByteMatchStatement, default=None)

    geo_match_statement: Optional[GeoMatchStatement] = core.attr(GeoMatchStatement, default=None)

    ip_set_reference_statement: Optional[IpSetReferenceStatement] = core.attr(
        IpSetReferenceStatement, default=None
    )

    label_match_statement: Optional[LabelMatchStatement] = core.attr(
        LabelMatchStatement, default=None
    )

    not_statement: Optional[RuleStatementAndStatementStatementNotStatement] = core.attr(
        RuleStatementAndStatementStatementNotStatement, default=None
    )

    or_statement: Optional[RuleStatementAndStatementStatementOrStatement] = core.attr(
        RuleStatementAndStatementStatementOrStatement, default=None
    )

    regex_pattern_set_reference_statement: Optional[RegexPatternSetReferenceStatement] = core.attr(
        RegexPatternSetReferenceStatement, default=None
    )

    size_constraint_statement: Optional[SizeConstraintStatement] = core.attr(
        SizeConstraintStatement, default=None
    )

    sqli_match_statement: Optional[SqliMatchStatement] = core.attr(SqliMatchStatement, default=None)

    xss_match_statement: Optional[XssMatchStatement] = core.attr(XssMatchStatement, default=None)

    def __init__(
        self,
        *,
        and_statement: Optional[RuleStatementAndStatementStatementAndStatement] = None,
        byte_match_statement: Optional[ByteMatchStatement] = None,
        geo_match_statement: Optional[GeoMatchStatement] = None,
        ip_set_reference_statement: Optional[IpSetReferenceStatement] = None,
        label_match_statement: Optional[LabelMatchStatement] = None,
        not_statement: Optional[RuleStatementAndStatementStatementNotStatement] = None,
        or_statement: Optional[RuleStatementAndStatementStatementOrStatement] = None,
        regex_pattern_set_reference_statement: Optional[RegexPatternSetReferenceStatement] = None,
        size_constraint_statement: Optional[SizeConstraintStatement] = None,
        sqli_match_statement: Optional[SqliMatchStatement] = None,
        xss_match_statement: Optional[XssMatchStatement] = None,
    ):
        super().__init__(
            args=RuleStatementAndStatementStatement.Args(
                and_statement=and_statement,
                byte_match_statement=byte_match_statement,
                geo_match_statement=geo_match_statement,
                ip_set_reference_statement=ip_set_reference_statement,
                label_match_statement=label_match_statement,
                not_statement=not_statement,
                or_statement=or_statement,
                regex_pattern_set_reference_statement=regex_pattern_set_reference_statement,
                size_constraint_statement=size_constraint_statement,
                sqli_match_statement=sqli_match_statement,
                xss_match_statement=xss_match_statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_statement: Optional[RuleStatementAndStatementStatementAndStatement] = core.arg(
            default=None
        )

        byte_match_statement: Optional[ByteMatchStatement] = core.arg(default=None)

        geo_match_statement: Optional[GeoMatchStatement] = core.arg(default=None)

        ip_set_reference_statement: Optional[IpSetReferenceStatement] = core.arg(default=None)

        label_match_statement: Optional[LabelMatchStatement] = core.arg(default=None)

        not_statement: Optional[RuleStatementAndStatementStatementNotStatement] = core.arg(
            default=None
        )

        or_statement: Optional[RuleStatementAndStatementStatementOrStatement] = core.arg(
            default=None
        )

        regex_pattern_set_reference_statement: Optional[
            RegexPatternSetReferenceStatement
        ] = core.arg(default=None)

        size_constraint_statement: Optional[SizeConstraintStatement] = core.arg(default=None)

        sqli_match_statement: Optional[SqliMatchStatement] = core.arg(default=None)

        xss_match_statement: Optional[XssMatchStatement] = core.arg(default=None)


@core.schema
class RuleStatementAndStatement(core.Schema):

    statement: Union[
        List[RuleStatementAndStatementStatement], core.ArrayOut[RuleStatementAndStatementStatement]
    ] = core.attr(RuleStatementAndStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: Union[
            List[RuleStatementAndStatementStatement],
            core.ArrayOut[RuleStatementAndStatementStatement],
        ],
    ):
        super().__init__(
            args=RuleStatementAndStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: Union[
            List[RuleStatementAndStatementStatement],
            core.ArrayOut[RuleStatementAndStatementStatement],
        ] = core.arg()


@core.schema
class RuleStatementOrStatement(core.Schema):

    statement: Union[
        List[RuleStatementAndStatementStatement], core.ArrayOut[RuleStatementAndStatementStatement]
    ] = core.attr(RuleStatementAndStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: Union[
            List[RuleStatementAndStatementStatement],
            core.ArrayOut[RuleStatementAndStatementStatement],
        ],
    ):
        super().__init__(
            args=RuleStatementOrStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: Union[
            List[RuleStatementAndStatementStatement],
            core.ArrayOut[RuleStatementAndStatementStatement],
        ] = core.arg()


@core.schema
class RuleStatementNotStatement(core.Schema):

    statement: Union[
        List[RuleStatementAndStatementStatement], core.ArrayOut[RuleStatementAndStatementStatement]
    ] = core.attr(RuleStatementAndStatementStatement, kind=core.Kind.array)

    def __init__(
        self,
        *,
        statement: Union[
            List[RuleStatementAndStatementStatement],
            core.ArrayOut[RuleStatementAndStatementStatement],
        ],
    ):
        super().__init__(
            args=RuleStatementNotStatement.Args(
                statement=statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        statement: Union[
            List[RuleStatementAndStatementStatement],
            core.ArrayOut[RuleStatementAndStatementStatement],
        ] = core.arg()


@core.schema
class RuleStatement(core.Schema):

    and_statement: Optional[RuleStatementAndStatement] = core.attr(
        RuleStatementAndStatement, default=None
    )

    byte_match_statement: Optional[ByteMatchStatement] = core.attr(ByteMatchStatement, default=None)

    geo_match_statement: Optional[GeoMatchStatement] = core.attr(GeoMatchStatement, default=None)

    ip_set_reference_statement: Optional[IpSetReferenceStatement] = core.attr(
        IpSetReferenceStatement, default=None
    )

    label_match_statement: Optional[LabelMatchStatement] = core.attr(
        LabelMatchStatement, default=None
    )

    not_statement: Optional[RuleStatementNotStatement] = core.attr(
        RuleStatementNotStatement, default=None
    )

    or_statement: Optional[RuleStatementOrStatement] = core.attr(
        RuleStatementOrStatement, default=None
    )

    regex_pattern_set_reference_statement: Optional[RegexPatternSetReferenceStatement] = core.attr(
        RegexPatternSetReferenceStatement, default=None
    )

    size_constraint_statement: Optional[SizeConstraintStatement] = core.attr(
        SizeConstraintStatement, default=None
    )

    sqli_match_statement: Optional[SqliMatchStatement] = core.attr(SqliMatchStatement, default=None)

    xss_match_statement: Optional[XssMatchStatement] = core.attr(XssMatchStatement, default=None)

    def __init__(
        self,
        *,
        and_statement: Optional[RuleStatementAndStatement] = None,
        byte_match_statement: Optional[ByteMatchStatement] = None,
        geo_match_statement: Optional[GeoMatchStatement] = None,
        ip_set_reference_statement: Optional[IpSetReferenceStatement] = None,
        label_match_statement: Optional[LabelMatchStatement] = None,
        not_statement: Optional[RuleStatementNotStatement] = None,
        or_statement: Optional[RuleStatementOrStatement] = None,
        regex_pattern_set_reference_statement: Optional[RegexPatternSetReferenceStatement] = None,
        size_constraint_statement: Optional[SizeConstraintStatement] = None,
        sqli_match_statement: Optional[SqliMatchStatement] = None,
        xss_match_statement: Optional[XssMatchStatement] = None,
    ):
        super().__init__(
            args=RuleStatement.Args(
                and_statement=and_statement,
                byte_match_statement=byte_match_statement,
                geo_match_statement=geo_match_statement,
                ip_set_reference_statement=ip_set_reference_statement,
                label_match_statement=label_match_statement,
                not_statement=not_statement,
                or_statement=or_statement,
                regex_pattern_set_reference_statement=regex_pattern_set_reference_statement,
                size_constraint_statement=size_constraint_statement,
                sqli_match_statement=sqli_match_statement,
                xss_match_statement=xss_match_statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_statement: Optional[RuleStatementAndStatement] = core.arg(default=None)

        byte_match_statement: Optional[ByteMatchStatement] = core.arg(default=None)

        geo_match_statement: Optional[GeoMatchStatement] = core.arg(default=None)

        ip_set_reference_statement: Optional[IpSetReferenceStatement] = core.arg(default=None)

        label_match_statement: Optional[LabelMatchStatement] = core.arg(default=None)

        not_statement: Optional[RuleStatementNotStatement] = core.arg(default=None)

        or_statement: Optional[RuleStatementOrStatement] = core.arg(default=None)

        regex_pattern_set_reference_statement: Optional[
            RegexPatternSetReferenceStatement
        ] = core.arg(default=None)

        size_constraint_statement: Optional[SizeConstraintStatement] = core.arg(default=None)

        sqli_match_statement: Optional[SqliMatchStatement] = core.arg(default=None)

        xss_match_statement: Optional[XssMatchStatement] = core.arg(default=None)


@core.schema
class VisibilityConfig(core.Schema):

    cloudwatch_metrics_enabled: Union[bool, core.BoolOut] = core.attr(bool)

    metric_name: Union[str, core.StringOut] = core.attr(str)

    sampled_requests_enabled: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        cloudwatch_metrics_enabled: Union[bool, core.BoolOut],
        metric_name: Union[str, core.StringOut],
        sampled_requests_enabled: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=VisibilityConfig.Args(
                cloudwatch_metrics_enabled=cloudwatch_metrics_enabled,
                metric_name=metric_name,
                sampled_requests_enabled=sampled_requests_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_metrics_enabled: Union[bool, core.BoolOut] = core.arg()

        metric_name: Union[str, core.StringOut] = core.arg()

        sampled_requests_enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class InsertHeader(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=InsertHeader.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class CustomRequestHandling(core.Schema):

    insert_header: Union[List[InsertHeader], core.ArrayOut[InsertHeader]] = core.attr(
        InsertHeader, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        insert_header: Union[List[InsertHeader], core.ArrayOut[InsertHeader]],
    ):
        super().__init__(
            args=CustomRequestHandling.Args(
                insert_header=insert_header,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        insert_header: Union[List[InsertHeader], core.ArrayOut[InsertHeader]] = core.arg()


@core.schema
class Allow(core.Schema):

    custom_request_handling: Optional[CustomRequestHandling] = core.attr(
        CustomRequestHandling, default=None
    )

    def __init__(
        self,
        *,
        custom_request_handling: Optional[CustomRequestHandling] = None,
    ):
        super().__init__(
            args=Allow.Args(
                custom_request_handling=custom_request_handling,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_request_handling: Optional[CustomRequestHandling] = core.arg(default=None)


@core.schema
class ResponseHeader(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResponseHeader.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class CustomResponse(core.Schema):

    custom_response_body_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    response_code: Union[int, core.IntOut] = core.attr(int)

    response_header: Optional[
        Union[List[ResponseHeader], core.ArrayOut[ResponseHeader]]
    ] = core.attr(ResponseHeader, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        response_code: Union[int, core.IntOut],
        custom_response_body_key: Optional[Union[str, core.StringOut]] = None,
        response_header: Optional[
            Union[List[ResponseHeader], core.ArrayOut[ResponseHeader]]
        ] = None,
    ):
        super().__init__(
            args=CustomResponse.Args(
                response_code=response_code,
                custom_response_body_key=custom_response_body_key,
                response_header=response_header,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_response_body_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        response_code: Union[int, core.IntOut] = core.arg()

        response_header: Optional[
            Union[List[ResponseHeader], core.ArrayOut[ResponseHeader]]
        ] = core.arg(default=None)


@core.schema
class Block(core.Schema):

    custom_response: Optional[CustomResponse] = core.attr(CustomResponse, default=None)

    def __init__(
        self,
        *,
        custom_response: Optional[CustomResponse] = None,
    ):
        super().__init__(
            args=Block.Args(
                custom_response=custom_response,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_response: Optional[CustomResponse] = core.arg(default=None)


@core.schema
class Count(core.Schema):

    custom_request_handling: Optional[CustomRequestHandling] = core.attr(
        CustomRequestHandling, default=None
    )

    def __init__(
        self,
        *,
        custom_request_handling: Optional[CustomRequestHandling] = None,
    ):
        super().__init__(
            args=Count.Args(
                custom_request_handling=custom_request_handling,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_request_handling: Optional[CustomRequestHandling] = core.arg(default=None)


@core.schema
class Action(core.Schema):

    allow: Optional[Allow] = core.attr(Allow, default=None)

    block: Optional[Block] = core.attr(Block, default=None)

    count: Optional[Count] = core.attr(Count, default=None)

    def __init__(
        self,
        *,
        allow: Optional[Allow] = None,
        block: Optional[Block] = None,
        count: Optional[Count] = None,
    ):
        super().__init__(
            args=Action.Args(
                allow=allow,
                block=block,
                count=count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow: Optional[Allow] = core.arg(default=None)

        block: Optional[Block] = core.arg(default=None)

        count: Optional[Count] = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    action: Action = core.attr(Action)

    name: Union[str, core.StringOut] = core.attr(str)

    priority: Union[int, core.IntOut] = core.attr(int)

    rule_label: Optional[Union[List[RuleLabel], core.ArrayOut[RuleLabel]]] = core.attr(
        RuleLabel, default=None, kind=core.Kind.array
    )

    statement: RuleStatement = core.attr(RuleStatement)

    visibility_config: VisibilityConfig = core.attr(VisibilityConfig)

    def __init__(
        self,
        *,
        action: Action,
        name: Union[str, core.StringOut],
        priority: Union[int, core.IntOut],
        statement: RuleStatement,
        visibility_config: VisibilityConfig,
        rule_label: Optional[Union[List[RuleLabel], core.ArrayOut[RuleLabel]]] = None,
    ):
        super().__init__(
            args=Rule.Args(
                action=action,
                name=name,
                priority=priority,
                statement=statement,
                visibility_config=visibility_config,
                rule_label=rule_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        priority: Union[int, core.IntOut] = core.arg()

        rule_label: Optional[Union[List[RuleLabel], core.ArrayOut[RuleLabel]]] = core.arg(
            default=None
        )

        statement: RuleStatement = core.arg()

        visibility_config: VisibilityConfig = core.arg()


@core.resource(type="aws_wafv2_rule_group", namespace="aws_waf")
class V2RuleGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    capacity: Union[int, core.IntOut] = core.attr(int)

    custom_response_body: Optional[
        Union[List[CustomResponseBody], core.ArrayOut[CustomResponseBody]]
    ] = core.attr(CustomResponseBody, default=None, kind=core.Kind.array)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lock_token: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    rule: Optional[Union[List[Rule], core.ArrayOut[Rule]]] = core.attr(
        Rule, default=None, kind=core.Kind.array
    )

    scope: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    visibility_config: VisibilityConfig = core.attr(VisibilityConfig)

    def __init__(
        self,
        resource_name: str,
        *,
        capacity: Union[int, core.IntOut],
        name: Union[str, core.StringOut],
        scope: Union[str, core.StringOut],
        visibility_config: VisibilityConfig,
        custom_response_body: Optional[
            Union[List[CustomResponseBody], core.ArrayOut[CustomResponseBody]]
        ] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        rule: Optional[Union[List[Rule], core.ArrayOut[Rule]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=V2RuleGroup.Args(
                capacity=capacity,
                name=name,
                scope=scope,
                visibility_config=visibility_config,
                custom_response_body=custom_response_body,
                description=description,
                rule=rule,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity: Union[int, core.IntOut] = core.arg()

        custom_response_body: Optional[
            Union[List[CustomResponseBody], core.ArrayOut[CustomResponseBody]]
        ] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        rule: Optional[Union[List[Rule], core.ArrayOut[Rule]]] = core.arg(default=None)

        scope: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        visibility_config: VisibilityConfig = core.arg()
