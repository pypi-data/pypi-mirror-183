from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ActionCondition(core.Schema):

    action: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        action: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ActionCondition.Args(
                action=action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Union[str, core.StringOut] = core.arg()


@core.schema
class LabelNameCondition(core.Schema):

    label_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        label_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LabelNameCondition.Args(
                label_name=label_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        label_name: Union[str, core.StringOut] = core.arg()


@core.schema
class Condition(core.Schema):

    action_condition: Optional[ActionCondition] = core.attr(ActionCondition, default=None)

    label_name_condition: Optional[LabelNameCondition] = core.attr(LabelNameCondition, default=None)

    def __init__(
        self,
        *,
        action_condition: Optional[ActionCondition] = None,
        label_name_condition: Optional[LabelNameCondition] = None,
    ):
        super().__init__(
            args=Condition.Args(
                action_condition=action_condition,
                label_name_condition=label_name_condition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_condition: Optional[ActionCondition] = core.arg(default=None)

        label_name_condition: Optional[LabelNameCondition] = core.arg(default=None)


@core.schema
class Filter(core.Schema):

    behavior: Union[str, core.StringOut] = core.attr(str)

    condition: Union[List[Condition], core.ArrayOut[Condition]] = core.attr(
        Condition, kind=core.Kind.array
    )

    requirement: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        behavior: Union[str, core.StringOut],
        condition: Union[List[Condition], core.ArrayOut[Condition]],
        requirement: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                behavior=behavior,
                condition=condition,
                requirement=requirement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        behavior: Union[str, core.StringOut] = core.arg()

        condition: Union[List[Condition], core.ArrayOut[Condition]] = core.arg()

        requirement: Union[str, core.StringOut] = core.arg()


@core.schema
class LoggingFilter(core.Schema):

    default_behavior: Union[str, core.StringOut] = core.attr(str)

    filter: Union[List[Filter], core.ArrayOut[Filter]] = core.attr(Filter, kind=core.Kind.array)

    def __init__(
        self,
        *,
        default_behavior: Union[str, core.StringOut],
        filter: Union[List[Filter], core.ArrayOut[Filter]],
    ):
        super().__init__(
            args=LoggingFilter.Args(
                default_behavior=default_behavior,
                filter=filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_behavior: Union[str, core.StringOut] = core.arg()

        filter: Union[List[Filter], core.ArrayOut[Filter]] = core.arg()


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
class RedactedFields(core.Schema):

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
            args=RedactedFields.Args(
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


@core.resource(type="aws_wafv2_web_acl_logging_configuration", namespace="aws_waf")
class V2WebAclLoggingConfiguration(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_destination_configs: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    logging_filter: Optional[LoggingFilter] = core.attr(LoggingFilter, default=None)

    redacted_fields: Optional[
        Union[List[RedactedFields], core.ArrayOut[RedactedFields]]
    ] = core.attr(RedactedFields, default=None, kind=core.Kind.array)

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        log_destination_configs: Union[List[str], core.ArrayOut[core.StringOut]],
        resource_arn: Union[str, core.StringOut],
        logging_filter: Optional[LoggingFilter] = None,
        redacted_fields: Optional[
            Union[List[RedactedFields], core.ArrayOut[RedactedFields]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=V2WebAclLoggingConfiguration.Args(
                log_destination_configs=log_destination_configs,
                resource_arn=resource_arn,
                logging_filter=logging_filter,
                redacted_fields=redacted_fields,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        log_destination_configs: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        logging_filter: Optional[LoggingFilter] = core.arg(default=None)

        redacted_fields: Optional[
            Union[List[RedactedFields], core.ArrayOut[RedactedFields]]
        ] = core.arg(default=None)

        resource_arn: Union[str, core.StringOut] = core.arg()
