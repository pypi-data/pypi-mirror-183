from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Scope(core.Schema):

    compliance_resource_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    compliance_resource_types: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    tag_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tag_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        compliance_resource_id: Optional[Union[str, core.StringOut]] = None,
        compliance_resource_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tag_key: Optional[Union[str, core.StringOut]] = None,
        tag_value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Scope.Args(
                compliance_resource_id=compliance_resource_id,
                compliance_resource_types=compliance_resource_types,
                tag_key=tag_key,
                tag_value=tag_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compliance_resource_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        compliance_resource_types: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        tag_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tag_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SourceDetail(core.Schema):

    event_source: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    maximum_execution_frequency: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    message_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        event_source: Optional[Union[str, core.StringOut]] = None,
        maximum_execution_frequency: Optional[Union[str, core.StringOut]] = None,
        message_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SourceDetail.Args(
                event_source=event_source,
                maximum_execution_frequency=maximum_execution_frequency,
                message_type=message_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_source: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        maximum_execution_frequency: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        message_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CustomPolicyDetails(core.Schema):

    enable_debug_log_delivery: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    policy_runtime: Union[str, core.StringOut] = core.attr(str)

    policy_text: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        policy_runtime: Union[str, core.StringOut],
        policy_text: Union[str, core.StringOut],
        enable_debug_log_delivery: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=CustomPolicyDetails.Args(
                policy_runtime=policy_runtime,
                policy_text=policy_text,
                enable_debug_log_delivery=enable_debug_log_delivery,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable_debug_log_delivery: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        policy_runtime: Union[str, core.StringOut] = core.arg()

        policy_text: Union[str, core.StringOut] = core.arg()


@core.schema
class Source(core.Schema):

    custom_policy_details: Optional[CustomPolicyDetails] = core.attr(
        CustomPolicyDetails, default=None
    )

    owner: Union[str, core.StringOut] = core.attr(str)

    source_detail: Optional[Union[List[SourceDetail], core.ArrayOut[SourceDetail]]] = core.attr(
        SourceDetail, default=None, kind=core.Kind.array
    )

    source_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        owner: Union[str, core.StringOut],
        custom_policy_details: Optional[CustomPolicyDetails] = None,
        source_detail: Optional[Union[List[SourceDetail], core.ArrayOut[SourceDetail]]] = None,
        source_identifier: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Source.Args(
                owner=owner,
                custom_policy_details=custom_policy_details,
                source_detail=source_detail,
                source_identifier=source_identifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_policy_details: Optional[CustomPolicyDetails] = core.arg(default=None)

        owner: Union[str, core.StringOut] = core.arg()

        source_detail: Optional[Union[List[SourceDetail], core.ArrayOut[SourceDetail]]] = core.arg(
            default=None
        )

        source_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_config_config_rule", namespace="aws_config")
class ConfigRule(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    input_parameters: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    maximum_execution_frequency: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    rule_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    scope: Optional[Scope] = core.attr(Scope, default=None)

    source: Source = core.attr(Source)

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
        source: Source,
        description: Optional[Union[str, core.StringOut]] = None,
        input_parameters: Optional[Union[str, core.StringOut]] = None,
        maximum_execution_frequency: Optional[Union[str, core.StringOut]] = None,
        scope: Optional[Scope] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigRule.Args(
                name=name,
                source=source,
                description=description,
                input_parameters=input_parameters,
                maximum_execution_frequency=maximum_execution_frequency,
                scope=scope,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        input_parameters: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        maximum_execution_frequency: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        scope: Optional[Scope] = core.arg(default=None)

        source: Source = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
