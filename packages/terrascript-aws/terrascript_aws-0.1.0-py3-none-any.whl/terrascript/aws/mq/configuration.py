from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_mq_configuration", namespace="aws_mq")
class Configuration(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authentication_strategy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    data: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    engine_type: Union[str, core.StringOut] = core.attr(str)

    engine_version: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    latest_revision: Union[int, core.IntOut] = core.attr(int, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

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
        data: Union[str, core.StringOut],
        engine_type: Union[str, core.StringOut],
        engine_version: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        authentication_strategy: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Configuration.Args(
                data=data,
                engine_type=engine_type,
                engine_version=engine_version,
                name=name,
                authentication_strategy=authentication_strategy,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authentication_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        data: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine_type: Union[str, core.StringOut] = core.arg()

        engine_version: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
