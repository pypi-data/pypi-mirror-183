from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_tag", namespace="aws_ec2")
class Tag(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key: Union[str, core.StringOut] = core.attr(str)

    resource_id: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        key: Union[str, core.StringOut],
        resource_id: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Tag.Args(
                key=key,
                resource_id=resource_id,
                value=value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key: Union[str, core.StringOut] = core.arg()

        resource_id: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()
