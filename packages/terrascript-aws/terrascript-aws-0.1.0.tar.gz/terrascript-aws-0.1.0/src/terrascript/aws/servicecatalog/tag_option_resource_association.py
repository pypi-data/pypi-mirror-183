from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_servicecatalog_tag_option_resource_association", namespace="aws_servicecatalog"
)
class TagOptionResourceAssociation(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_description: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_id: Union[str, core.StringOut] = core.attr(str)

    resource_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    tag_option_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        resource_id: Union[str, core.StringOut],
        tag_option_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TagOptionResourceAssociation.Args(
                resource_id=resource_id,
                tag_option_id=tag_option_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        resource_id: Union[str, core.StringOut] = core.arg()

        tag_option_id: Union[str, core.StringOut] = core.arg()
