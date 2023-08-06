from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_network_insights_path", namespace="aws_vpc")
class Ec2NetworkInsightsPath(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    destination: Union[str, core.StringOut] = core.attr(str)

    destination_ip: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    destination_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    protocol: Union[str, core.StringOut] = core.attr(str)

    source: Union[str, core.StringOut] = core.attr(str)

    source_ip: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        destination: Union[str, core.StringOut],
        protocol: Union[str, core.StringOut],
        source: Union[str, core.StringOut],
        destination_ip: Optional[Union[str, core.StringOut]] = None,
        destination_port: Optional[Union[int, core.IntOut]] = None,
        source_ip: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2NetworkInsightsPath.Args(
                destination=destination,
                protocol=protocol,
                source=source,
                destination_ip=destination_ip,
                destination_port=destination_port,
                source_ip=source_ip,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination: Union[str, core.StringOut] = core.arg()

        destination_ip: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        destination_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        protocol: Union[str, core.StringOut] = core.arg()

        source: Union[str, core.StringOut] = core.arg()

        source_ip: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
