from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ssm_parameter", namespace="aws_ssm")
class Parameter(core.Resource):

    allowed_pattern: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    data_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    insecure_value: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    overwrite: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    type: Union[str, core.StringOut] = core.attr(str)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    version: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        allowed_pattern: Optional[Union[str, core.StringOut]] = None,
        arn: Optional[Union[str, core.StringOut]] = None,
        data_type: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        insecure_value: Optional[Union[str, core.StringOut]] = None,
        key_id: Optional[Union[str, core.StringOut]] = None,
        overwrite: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tier: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Parameter.Args(
                name=name,
                type=type,
                allowed_pattern=allowed_pattern,
                arn=arn,
                data_type=data_type,
                description=description,
                insecure_value=insecure_value,
                key_id=key_id,
                overwrite=overwrite,
                tags=tags,
                tags_all=tags_all,
                tier=tier,
                value=value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allowed_pattern: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        data_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        insecure_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        overwrite: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        tier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)
