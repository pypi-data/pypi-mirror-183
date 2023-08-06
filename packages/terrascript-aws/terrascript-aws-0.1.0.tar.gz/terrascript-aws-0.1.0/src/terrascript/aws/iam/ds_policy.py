from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_iam_policy", namespace="aws_iam")
class DsPolicy(core.Data):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    path: Union[str, core.StringOut] = core.attr(str, computed=True)

    path_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    policy: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        path_prefix: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPolicy.Args(
                arn=arn,
                name=name,
                path_prefix=path_prefix,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        path_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
