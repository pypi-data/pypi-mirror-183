from typing import Union

import terrascript.core as core


@core.data(type="aws_eks_cluster_auth", namespace="aws_eks")
class DsClusterAuth(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    token: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsClusterAuth.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()
