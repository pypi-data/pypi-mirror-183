from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_glue_schema", namespace="aws_glue")
class Schema(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    compatibility: Union[str, core.StringOut] = core.attr(str)

    data_format: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    latest_schema_version: Union[int, core.IntOut] = core.attr(int, computed=True)

    next_schema_version: Union[int, core.IntOut] = core.attr(int, computed=True)

    registry_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    registry_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    schema_checkpoint: Union[int, core.IntOut] = core.attr(int, computed=True)

    schema_definition: Union[str, core.StringOut] = core.attr(str)

    schema_name: Union[str, core.StringOut] = core.attr(str)

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
        compatibility: Union[str, core.StringOut],
        data_format: Union[str, core.StringOut],
        schema_definition: Union[str, core.StringOut],
        schema_name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        registry_arn: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Schema.Args(
                compatibility=compatibility,
                data_format=data_format,
                schema_definition=schema_definition,
                schema_name=schema_name,
                description=description,
                registry_arn=registry_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        compatibility: Union[str, core.StringOut] = core.arg()

        data_format: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        registry_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schema_definition: Union[str, core.StringOut] = core.arg()

        schema_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
