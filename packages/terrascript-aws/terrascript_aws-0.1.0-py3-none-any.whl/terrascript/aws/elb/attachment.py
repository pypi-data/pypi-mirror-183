from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_elb_attachment", namespace="aws_elb")
class Attachment(core.Resource):

    elb: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        elb: Union[str, core.StringOut],
        instance: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Attachment.Args(
                elb=elb,
                instance=instance,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        elb: Union[str, core.StringOut] = core.arg()

        instance: Union[str, core.StringOut] = core.arg()
