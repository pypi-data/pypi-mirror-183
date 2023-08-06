from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ses_template", namespace="aws_ses")
class Template(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    html: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    subject: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    text: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        html: Optional[Union[str, core.StringOut]] = None,
        subject: Optional[Union[str, core.StringOut]] = None,
        text: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Template.Args(
                name=name,
                html=html,
                subject=subject,
                text=text,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        html: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        subject: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        text: Optional[Union[str, core.StringOut]] = core.arg(default=None)
