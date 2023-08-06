from typing import List, Optional, Union

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


@core.resource(
    type="aws_elastic_beanstalk_configuration_template", namespace="aws_elastic_beanstalk"
)
class ConfigurationTemplate(core.Resource):

    application: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    environment_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    setting: Optional[Union[List[Setting], core.ArrayOut[Setting]]] = core.attr(
        Setting, default=None, computed=True, kind=core.Kind.array
    )

    solution_stack_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        application: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        environment_id: Optional[Union[str, core.StringOut]] = None,
        setting: Optional[Union[List[Setting], core.ArrayOut[Setting]]] = None,
        solution_stack_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigurationTemplate.Args(
                application=application,
                name=name,
                description=description,
                environment_id=environment_id,
                setting=setting,
                solution_stack_name=solution_stack_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        environment_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        setting: Optional[Union[List[Setting], core.ArrayOut[Setting]]] = core.arg(default=None)

        solution_stack_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
