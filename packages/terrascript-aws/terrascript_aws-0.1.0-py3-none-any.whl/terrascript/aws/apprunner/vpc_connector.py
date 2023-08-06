from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_apprunner_vpc_connector", namespace="aws_apprunner")
class VpcConnector(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_connector_name: Union[str, core.StringOut] = core.attr(str)

    vpc_connector_revision: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        security_groups: Union[List[str], core.ArrayOut[core.StringOut]],
        subnets: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_connector_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VpcConnector.Args(
                security_groups=security_groups,
                subnets=subnets,
                vpc_connector_name=vpc_connector_name,
                tags=tags,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        vpc_connector_name: Union[str, core.StringOut] = core.arg()
