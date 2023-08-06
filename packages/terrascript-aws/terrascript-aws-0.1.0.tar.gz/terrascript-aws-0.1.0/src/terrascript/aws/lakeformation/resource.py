from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lakeformation_resource", namespace="aws_lakeformation")
class Resource(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        arn: Union[str, core.StringOut],
        role_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Resource.Args(
                arn=arn,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arn: Union[str, core.StringOut] = core.arg()

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)
