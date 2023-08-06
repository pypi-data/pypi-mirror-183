from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_msk_scram_secret_association", namespace="aws_managed_streaming_for_kafka")
class MskScramSecretAssociation(core.Resource):

    cluster_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    secret_arn_list: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_arn: Union[str, core.StringOut],
        secret_arn_list: Union[List[str], core.ArrayOut[core.StringOut]],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskScramSecretAssociation.Args(
                cluster_arn=cluster_arn,
                secret_arn_list=secret_arn_list,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_arn: Union[str, core.StringOut] = core.arg()

        secret_arn_list: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()
