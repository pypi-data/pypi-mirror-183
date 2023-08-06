from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloud9_environment_ec2", namespace="aws_cloud9")
class EnvironmentEc2(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    automatic_stop_time_minutes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    connection_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_type: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    owner_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        automatic_stop_time_minutes: Optional[Union[int, core.IntOut]] = None,
        connection_type: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        image_id: Optional[Union[str, core.StringOut]] = None,
        owner_arn: Optional[Union[str, core.StringOut]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EnvironmentEc2.Args(
                instance_type=instance_type,
                name=name,
                automatic_stop_time_minutes=automatic_stop_time_minutes,
                connection_type=connection_type,
                description=description,
                image_id=image_id,
                owner_arn=owner_arn,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        automatic_stop_time_minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        connection_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_type: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        owner_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
