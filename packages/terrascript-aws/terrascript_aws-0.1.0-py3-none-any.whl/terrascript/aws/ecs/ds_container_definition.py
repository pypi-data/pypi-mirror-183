from typing import Dict, Union

import terrascript.core as core


@core.data(type="aws_ecs_container_definition", namespace="aws_ecs")
class DsContainerDefinition(core.Data):

    container_name: Union[str, core.StringOut] = core.attr(str)

    cpu: Union[int, core.IntOut] = core.attr(int, computed=True)

    disable_networking: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    docker_labels: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    environment: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_digest: Union[str, core.StringOut] = core.attr(str, computed=True)

    memory: Union[int, core.IntOut] = core.attr(int, computed=True)

    memory_reservation: Union[int, core.IntOut] = core.attr(int, computed=True)

    task_definition: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        container_name: Union[str, core.StringOut],
        task_definition: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsContainerDefinition.Args(
                container_name=container_name,
                task_definition=task_definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_name: Union[str, core.StringOut] = core.arg()

        task_definition: Union[str, core.StringOut] = core.arg()
