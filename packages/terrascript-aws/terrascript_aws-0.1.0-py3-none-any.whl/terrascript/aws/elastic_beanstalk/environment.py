from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Setting(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    namespace: Union[str, core.StringOut] = core.attr(str)

    resource: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        namespace: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
        resource: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Setting.Args(
                name=name,
                namespace=namespace,
                value=value,
                resource=resource,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        namespace: Union[str, core.StringOut] = core.arg()

        resource: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class AllSettings(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    namespace: Union[str, core.StringOut] = core.attr(str)

    resource: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        namespace: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
        resource: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AllSettings.Args(
                name=name,
                namespace=namespace,
                value=value,
                resource=resource,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        namespace: Union[str, core.StringOut] = core.arg()

        resource: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_elastic_beanstalk_environment", namespace="aws_elastic_beanstalk")
class Environment(core.Resource):

    all_settings: Union[List[AllSettings], core.ArrayOut[AllSettings]] = core.attr(
        AllSettings, computed=True, kind=core.Kind.array
    )

    application: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    autoscaling_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    cname: Union[str, core.StringOut] = core.attr(str, computed=True)

    cname_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    endpoint_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instances: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    launch_configurations: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    load_balancers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    platform_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    poll_interval: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    queues: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    setting: Optional[Union[List[Setting], core.ArrayOut[Setting]]] = core.attr(
        Setting, default=None, kind=core.Kind.array
    )

    solution_stack_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    template_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    triggers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    version_label: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    wait_for_ready_timeout: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        application: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        cname_prefix: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        platform_arn: Optional[Union[str, core.StringOut]] = None,
        poll_interval: Optional[Union[str, core.StringOut]] = None,
        setting: Optional[Union[List[Setting], core.ArrayOut[Setting]]] = None,
        solution_stack_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        template_name: Optional[Union[str, core.StringOut]] = None,
        tier: Optional[Union[str, core.StringOut]] = None,
        version_label: Optional[Union[str, core.StringOut]] = None,
        wait_for_ready_timeout: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Environment.Args(
                application=application,
                name=name,
                cname_prefix=cname_prefix,
                description=description,
                platform_arn=platform_arn,
                poll_interval=poll_interval,
                setting=setting,
                solution_stack_name=solution_stack_name,
                tags=tags,
                tags_all=tags_all,
                template_name=template_name,
                tier=tier,
                version_label=version_label,
                wait_for_ready_timeout=wait_for_ready_timeout,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application: Union[str, core.StringOut] = core.arg()

        cname_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        platform_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        poll_interval: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        setting: Optional[Union[List[Setting], core.ArrayOut[Setting]]] = core.arg(default=None)

        solution_stack_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        template_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version_label: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        wait_for_ready_timeout: Optional[Union[str, core.StringOut]] = core.arg(default=None)
