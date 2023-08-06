from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_amplify_branch", namespace="aws_amplify")
class Branch(core.Resource):

    app_id: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    associated_resources: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    backend_environment_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    basic_auth_credentials: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    branch_name: Union[str, core.StringOut] = core.attr(str)

    custom_domains: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    destination_branch: Union[str, core.StringOut] = core.attr(str, computed=True)

    display_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    enable_auto_build: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_basic_auth: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_notification: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_performance_mode: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_pull_request_preview: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    environment_variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    framework: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    pull_request_environment_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    source_branch: Union[str, core.StringOut] = core.attr(str, computed=True)

    stage: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    ttl: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        app_id: Union[str, core.StringOut],
        branch_name: Union[str, core.StringOut],
        backend_environment_arn: Optional[Union[str, core.StringOut]] = None,
        basic_auth_credentials: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        display_name: Optional[Union[str, core.StringOut]] = None,
        enable_auto_build: Optional[Union[bool, core.BoolOut]] = None,
        enable_basic_auth: Optional[Union[bool, core.BoolOut]] = None,
        enable_notification: Optional[Union[bool, core.BoolOut]] = None,
        enable_performance_mode: Optional[Union[bool, core.BoolOut]] = None,
        enable_pull_request_preview: Optional[Union[bool, core.BoolOut]] = None,
        environment_variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        framework: Optional[Union[str, core.StringOut]] = None,
        pull_request_environment_name: Optional[Union[str, core.StringOut]] = None,
        stage: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        ttl: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Branch.Args(
                app_id=app_id,
                branch_name=branch_name,
                backend_environment_arn=backend_environment_arn,
                basic_auth_credentials=basic_auth_credentials,
                description=description,
                display_name=display_name,
                enable_auto_build=enable_auto_build,
                enable_basic_auth=enable_basic_auth,
                enable_notification=enable_notification,
                enable_performance_mode=enable_performance_mode,
                enable_pull_request_preview=enable_pull_request_preview,
                environment_variables=environment_variables,
                framework=framework,
                pull_request_environment_name=pull_request_environment_name,
                stage=stage,
                tags=tags,
                tags_all=tags_all,
                ttl=ttl,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_id: Union[str, core.StringOut] = core.arg()

        backend_environment_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        basic_auth_credentials: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        branch_name: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        display_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable_auto_build: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_basic_auth: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_notification: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_performance_mode: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_pull_request_preview: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        environment_variables: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        framework: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        pull_request_environment_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        stage: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        ttl: Optional[Union[str, core.StringOut]] = core.arg(default=None)
