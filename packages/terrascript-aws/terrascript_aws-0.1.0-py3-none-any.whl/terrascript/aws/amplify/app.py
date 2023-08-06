from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AutoBranchCreationConfig(core.Schema):

    basic_auth_credentials: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    build_spec: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enable_auto_build: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_basic_auth: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_performance_mode: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_pull_request_preview: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    environment_variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    framework: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    pull_request_environment_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    stage: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        basic_auth_credentials: Optional[Union[str, core.StringOut]] = None,
        build_spec: Optional[Union[str, core.StringOut]] = None,
        enable_auto_build: Optional[Union[bool, core.BoolOut]] = None,
        enable_basic_auth: Optional[Union[bool, core.BoolOut]] = None,
        enable_performance_mode: Optional[Union[bool, core.BoolOut]] = None,
        enable_pull_request_preview: Optional[Union[bool, core.BoolOut]] = None,
        environment_variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        framework: Optional[Union[str, core.StringOut]] = None,
        pull_request_environment_name: Optional[Union[str, core.StringOut]] = None,
        stage: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AutoBranchCreationConfig.Args(
                basic_auth_credentials=basic_auth_credentials,
                build_spec=build_spec,
                enable_auto_build=enable_auto_build,
                enable_basic_auth=enable_basic_auth,
                enable_performance_mode=enable_performance_mode,
                enable_pull_request_preview=enable_pull_request_preview,
                environment_variables=environment_variables,
                framework=framework,
                pull_request_environment_name=pull_request_environment_name,
                stage=stage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        basic_auth_credentials: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        build_spec: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable_auto_build: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_basic_auth: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_performance_mode: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_pull_request_preview: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        environment_variables: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        framework: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        pull_request_environment_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        stage: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CustomRule(core.Schema):

    condition: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source: Union[str, core.StringOut] = core.attr(str)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    target: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        source: Union[str, core.StringOut],
        target: Union[str, core.StringOut],
        condition: Optional[Union[str, core.StringOut]] = None,
        status: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CustomRule.Args(
                source=source,
                target=target,
                condition=condition,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        condition: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source: Union[str, core.StringOut] = core.arg()

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target: Union[str, core.StringOut] = core.arg()


@core.schema
class ProductionBranch(core.Schema):

    branch_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_deploy_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    thumbnail_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        branch_name: Union[str, core.StringOut],
        last_deploy_time: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
        thumbnail_url: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ProductionBranch.Args(
                branch_name=branch_name,
                last_deploy_time=last_deploy_time,
                status=status,
                thumbnail_url=thumbnail_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        branch_name: Union[str, core.StringOut] = core.arg()

        last_deploy_time: Union[str, core.StringOut] = core.arg()

        status: Union[str, core.StringOut] = core.arg()

        thumbnail_url: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_amplify_app", namespace="aws_amplify")
class App(core.Resource):

    access_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_branch_creation_config: Optional[AutoBranchCreationConfig] = core.attr(
        AutoBranchCreationConfig, default=None, computed=True
    )

    auto_branch_creation_patterns: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    basic_auth_credentials: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    build_spec: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    custom_rule: Optional[Union[List[CustomRule], core.ArrayOut[CustomRule]]] = core.attr(
        CustomRule, default=None, kind=core.Kind.array
    )

    default_domain: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enable_auto_branch_creation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_basic_auth: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_branch_auto_build: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_branch_auto_deletion: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    environment_variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    iam_service_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    oauth_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    platform: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    production_branch: Union[List[ProductionBranch], core.ArrayOut[ProductionBranch]] = core.attr(
        ProductionBranch, computed=True, kind=core.Kind.array
    )

    repository: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        access_token: Optional[Union[str, core.StringOut]] = None,
        auto_branch_creation_config: Optional[AutoBranchCreationConfig] = None,
        auto_branch_creation_patterns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        basic_auth_credentials: Optional[Union[str, core.StringOut]] = None,
        build_spec: Optional[Union[str, core.StringOut]] = None,
        custom_rule: Optional[Union[List[CustomRule], core.ArrayOut[CustomRule]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        enable_auto_branch_creation: Optional[Union[bool, core.BoolOut]] = None,
        enable_basic_auth: Optional[Union[bool, core.BoolOut]] = None,
        enable_branch_auto_build: Optional[Union[bool, core.BoolOut]] = None,
        enable_branch_auto_deletion: Optional[Union[bool, core.BoolOut]] = None,
        environment_variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        iam_service_role_arn: Optional[Union[str, core.StringOut]] = None,
        oauth_token: Optional[Union[str, core.StringOut]] = None,
        platform: Optional[Union[str, core.StringOut]] = None,
        repository: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=App.Args(
                name=name,
                access_token=access_token,
                auto_branch_creation_config=auto_branch_creation_config,
                auto_branch_creation_patterns=auto_branch_creation_patterns,
                basic_auth_credentials=basic_auth_credentials,
                build_spec=build_spec,
                custom_rule=custom_rule,
                description=description,
                enable_auto_branch_creation=enable_auto_branch_creation,
                enable_basic_auth=enable_basic_auth,
                enable_branch_auto_build=enable_branch_auto_build,
                enable_branch_auto_deletion=enable_branch_auto_deletion,
                environment_variables=environment_variables,
                iam_service_role_arn=iam_service_role_arn,
                oauth_token=oauth_token,
                platform=platform,
                repository=repository,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        auto_branch_creation_config: Optional[AutoBranchCreationConfig] = core.arg(default=None)

        auto_branch_creation_patterns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        basic_auth_credentials: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        build_spec: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        custom_rule: Optional[Union[List[CustomRule], core.ArrayOut[CustomRule]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable_auto_branch_creation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_basic_auth: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_branch_auto_build: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_branch_auto_deletion: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        environment_variables: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        iam_service_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        oauth_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        platform: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        repository: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
