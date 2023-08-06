from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_elasticache_user_group", namespace="aws_elasticache")
class UserGroup(core.Resource):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    engine: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_group_id: Union[str, core.StringOut] = core.attr(str)

    user_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        engine: Union[str, core.StringOut],
        user_group_id: Union[str, core.StringOut],
        arn: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        user_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserGroup.Args(
                engine=engine,
                user_group_id=user_group_id,
                arn=arn,
                tags=tags,
                tags_all=tags_all,
                user_ids=user_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_group_id: Union[str, core.StringOut] = core.arg()

        user_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)
