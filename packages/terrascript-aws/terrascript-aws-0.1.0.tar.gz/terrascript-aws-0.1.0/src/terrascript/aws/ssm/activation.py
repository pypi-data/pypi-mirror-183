from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ssm_activation", namespace="aws_ssm")
class Activation(core.Resource):

    activation_code: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    expiration_date: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    expired: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    iam_role: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    registration_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    registration_limit: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        iam_role: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        expiration_date: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        registration_limit: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Activation.Args(
                iam_role=iam_role,
                description=description,
                expiration_date=expiration_date,
                name=name,
                registration_limit=registration_limit,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        expiration_date: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_role: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        registration_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
