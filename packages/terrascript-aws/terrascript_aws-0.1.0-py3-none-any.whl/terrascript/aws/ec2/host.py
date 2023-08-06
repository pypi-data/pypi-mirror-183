from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_host", namespace="aws_ec2")
class Host(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_placement: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    availability_zone: Union[str, core.StringOut] = core.attr(str)

    host_recovery: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_family: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    outpost_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        availability_zone: Union[str, core.StringOut],
        auto_placement: Optional[Union[str, core.StringOut]] = None,
        host_recovery: Optional[Union[str, core.StringOut]] = None,
        instance_family: Optional[Union[str, core.StringOut]] = None,
        instance_type: Optional[Union[str, core.StringOut]] = None,
        outpost_arn: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Host.Args(
                availability_zone=availability_zone,
                auto_placement=auto_placement,
                host_recovery=host_recovery,
                instance_family=instance_family,
                instance_type=instance_type,
                outpost_arn=outpost_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_placement: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        availability_zone: Union[str, core.StringOut] = core.arg()

        host_recovery: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_family: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        outpost_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
