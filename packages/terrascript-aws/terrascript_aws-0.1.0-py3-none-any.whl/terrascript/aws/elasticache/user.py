from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_elasticache_user", namespace="aws_elasticache")
class User(core.Resource):

    access_string: Union[str, core.StringOut] = core.attr(str)

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    engine: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    no_password_required: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    passwords: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_id: Union[str, core.StringOut] = core.attr(str)

    user_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        access_string: Union[str, core.StringOut],
        engine: Union[str, core.StringOut],
        user_id: Union[str, core.StringOut],
        user_name: Union[str, core.StringOut],
        arn: Optional[Union[str, core.StringOut]] = None,
        no_password_required: Optional[Union[bool, core.BoolOut]] = None,
        passwords: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                access_string=access_string,
                engine=engine,
                user_id=user_id,
                user_name=user_name,
                arn=arn,
                no_password_required=no_password_required,
                passwords=passwords,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_string: Union[str, core.StringOut] = core.arg()

        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine: Union[str, core.StringOut] = core.arg()

        no_password_required: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        passwords: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_id: Union[str, core.StringOut] = core.arg()

        user_name: Union[str, core.StringOut] = core.arg()
