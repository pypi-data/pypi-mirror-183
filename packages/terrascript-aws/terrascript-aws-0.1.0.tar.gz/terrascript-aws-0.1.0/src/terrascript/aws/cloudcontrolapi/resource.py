from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudcontrolapi_resource", namespace="aws_cloudcontrolapi")
class Resource(core.Resource):

    desired_state: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    properties: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    schema: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    type_name: Union[str, core.StringOut] = core.attr(str)

    type_version_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        desired_state: Union[str, core.StringOut],
        type_name: Union[str, core.StringOut],
        role_arn: Optional[Union[str, core.StringOut]] = None,
        schema: Optional[Union[str, core.StringOut]] = None,
        type_version_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Resource.Args(
                desired_state=desired_state,
                type_name=type_name,
                role_arn=role_arn,
                schema=schema,
                type_version_id=type_version_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        desired_state: Union[str, core.StringOut] = core.arg()

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schema: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type_name: Union[str, core.StringOut] = core.arg()

        type_version_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
