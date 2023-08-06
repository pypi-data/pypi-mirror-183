from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_redshift_cluster_iam_roles", namespace="aws_redshift")
class ClusterIamRoles(core.Resource):

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    default_iam_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    iam_role_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_identifier: Union[str, core.StringOut],
        default_iam_role_arn: Optional[Union[str, core.StringOut]] = None,
        iam_role_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterIamRoles.Args(
                cluster_identifier=cluster_identifier,
                default_iam_role_arn=default_iam_role_arn,
                iam_role_arns=iam_role_arns,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_identifier: Union[str, core.StringOut] = core.arg()

        default_iam_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_role_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )
