from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Monitor(core.Schema):

    alarm_arn: Union[str, core.StringOut] = core.attr(str)

    alarm_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        alarm_arn: Union[str, core.StringOut],
        alarm_role_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Monitor.Args(
                alarm_arn=alarm_arn,
                alarm_role_arn=alarm_role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        alarm_arn: Union[str, core.StringOut] = core.arg()

        alarm_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_appconfig_environment", namespace="aws_appconfig")
class Environment(core.Resource):

    application_id: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    environment_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    monitor: Optional[Union[List[Monitor], core.ArrayOut[Monitor]]] = core.attr(
        Monitor, default=None, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        application_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        monitor: Optional[Union[List[Monitor], core.ArrayOut[Monitor]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Environment.Args(
                application_id=application_id,
                name=name,
                description=description,
                monitor=monitor,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        monitor: Optional[Union[List[Monitor], core.ArrayOut[Monitor]]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
