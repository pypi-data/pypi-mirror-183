from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Tag(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    propagate_at_launch: Union[bool, core.BoolOut] = core.attr(bool)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        propagate_at_launch: Union[bool, core.BoolOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Tag.Args(
                key=key,
                propagate_at_launch=propagate_at_launch,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        propagate_at_launch: Union[bool, core.BoolOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_autoscaling_group_tag", namespace="aws_autoscaling")
class GroupTag(core.Resource):

    autoscaling_group_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tag: Tag = core.attr(Tag)

    def __init__(
        self,
        resource_name: str,
        *,
        autoscaling_group_name: Union[str, core.StringOut],
        tag: Tag,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GroupTag.Args(
                autoscaling_group_name=autoscaling_group_name,
                tag=tag,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        autoscaling_group_name: Union[str, core.StringOut] = core.arg()

        tag: Tag = core.arg()
