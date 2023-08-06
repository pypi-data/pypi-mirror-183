from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class HumanLoopActivationConditionsConfig(core.Schema):

    human_loop_activation_conditions: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        human_loop_activation_conditions: Union[str, core.StringOut],
    ):
        super().__init__(
            args=HumanLoopActivationConditionsConfig.Args(
                human_loop_activation_conditions=human_loop_activation_conditions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        human_loop_activation_conditions: Union[str, core.StringOut] = core.arg()


@core.schema
class HumanLoopActivationConfig(core.Schema):

    human_loop_activation_conditions_config: Optional[
        HumanLoopActivationConditionsConfig
    ] = core.attr(HumanLoopActivationConditionsConfig, default=None)

    def __init__(
        self,
        *,
        human_loop_activation_conditions_config: Optional[
            HumanLoopActivationConditionsConfig
        ] = None,
    ):
        super().__init__(
            args=HumanLoopActivationConfig.Args(
                human_loop_activation_conditions_config=human_loop_activation_conditions_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        human_loop_activation_conditions_config: Optional[
            HumanLoopActivationConditionsConfig
        ] = core.arg(default=None)


@core.schema
class HumanLoopRequestSource(core.Schema):

    aws_managed_human_loop_request_source: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        aws_managed_human_loop_request_source: Union[str, core.StringOut],
    ):
        super().__init__(
            args=HumanLoopRequestSource.Args(
                aws_managed_human_loop_request_source=aws_managed_human_loop_request_source,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_managed_human_loop_request_source: Union[str, core.StringOut] = core.arg()


@core.schema
class OutputConfig(core.Schema):

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_output_path: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        s3_output_path: Union[str, core.StringOut],
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=OutputConfig.Args(
                s3_output_path=s3_output_path,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_output_path: Union[str, core.StringOut] = core.arg()


@core.schema
class AmountInUsd(core.Schema):

    cents: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    dollars: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tenth_fractions_of_a_cent: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        cents: Optional[Union[int, core.IntOut]] = None,
        dollars: Optional[Union[int, core.IntOut]] = None,
        tenth_fractions_of_a_cent: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=AmountInUsd.Args(
                cents=cents,
                dollars=dollars,
                tenth_fractions_of_a_cent=tenth_fractions_of_a_cent,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cents: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        dollars: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tenth_fractions_of_a_cent: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class PublicWorkforceTaskPrice(core.Schema):

    amount_in_usd: Optional[AmountInUsd] = core.attr(AmountInUsd, default=None)

    def __init__(
        self,
        *,
        amount_in_usd: Optional[AmountInUsd] = None,
    ):
        super().__init__(
            args=PublicWorkforceTaskPrice.Args(
                amount_in_usd=amount_in_usd,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amount_in_usd: Optional[AmountInUsd] = core.arg(default=None)


@core.schema
class HumanLoopConfig(core.Schema):

    human_task_ui_arn: Union[str, core.StringOut] = core.attr(str)

    public_workforce_task_price: Optional[PublicWorkforceTaskPrice] = core.attr(
        PublicWorkforceTaskPrice, default=None
    )

    task_availability_lifetime_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    task_count: Union[int, core.IntOut] = core.attr(int)

    task_description: Union[str, core.StringOut] = core.attr(str)

    task_keywords: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    task_time_limit_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    task_title: Union[str, core.StringOut] = core.attr(str)

    workteam_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        human_task_ui_arn: Union[str, core.StringOut],
        task_count: Union[int, core.IntOut],
        task_description: Union[str, core.StringOut],
        task_title: Union[str, core.StringOut],
        workteam_arn: Union[str, core.StringOut],
        public_workforce_task_price: Optional[PublicWorkforceTaskPrice] = None,
        task_availability_lifetime_in_seconds: Optional[Union[int, core.IntOut]] = None,
        task_keywords: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        task_time_limit_in_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=HumanLoopConfig.Args(
                human_task_ui_arn=human_task_ui_arn,
                task_count=task_count,
                task_description=task_description,
                task_title=task_title,
                workteam_arn=workteam_arn,
                public_workforce_task_price=public_workforce_task_price,
                task_availability_lifetime_in_seconds=task_availability_lifetime_in_seconds,
                task_keywords=task_keywords,
                task_time_limit_in_seconds=task_time_limit_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        human_task_ui_arn: Union[str, core.StringOut] = core.arg()

        public_workforce_task_price: Optional[PublicWorkforceTaskPrice] = core.arg(default=None)

        task_availability_lifetime_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        task_count: Union[int, core.IntOut] = core.arg()

        task_description: Union[str, core.StringOut] = core.arg()

        task_keywords: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        task_time_limit_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        task_title: Union[str, core.StringOut] = core.arg()

        workteam_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_sagemaker_flow_definition", namespace="aws_sagemaker")
class FlowDefinition(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    flow_definition_name: Union[str, core.StringOut] = core.attr(str)

    human_loop_activation_config: Optional[HumanLoopActivationConfig] = core.attr(
        HumanLoopActivationConfig, default=None
    )

    human_loop_config: HumanLoopConfig = core.attr(HumanLoopConfig)

    human_loop_request_source: Optional[HumanLoopRequestSource] = core.attr(
        HumanLoopRequestSource, default=None
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    output_config: OutputConfig = core.attr(OutputConfig)

    role_arn: Union[str, core.StringOut] = core.attr(str)

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
        flow_definition_name: Union[str, core.StringOut],
        human_loop_config: HumanLoopConfig,
        output_config: OutputConfig,
        role_arn: Union[str, core.StringOut],
        human_loop_activation_config: Optional[HumanLoopActivationConfig] = None,
        human_loop_request_source: Optional[HumanLoopRequestSource] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FlowDefinition.Args(
                flow_definition_name=flow_definition_name,
                human_loop_config=human_loop_config,
                output_config=output_config,
                role_arn=role_arn,
                human_loop_activation_config=human_loop_activation_config,
                human_loop_request_source=human_loop_request_source,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        flow_definition_name: Union[str, core.StringOut] = core.arg()

        human_loop_activation_config: Optional[HumanLoopActivationConfig] = core.arg(default=None)

        human_loop_config: HumanLoopConfig = core.arg()

        human_loop_request_source: Optional[HumanLoopRequestSource] = core.arg(default=None)

        output_config: OutputConfig = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
