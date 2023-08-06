from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_servicecatalog_tag_option", namespace="aws_servicecatalog")
class TagOption(core.Resource):

    active: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key: Union[str, core.StringOut] = core.attr(str)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
        active: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TagOption.Args(
                key=key,
                value=value,
                active=active,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        active: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()
