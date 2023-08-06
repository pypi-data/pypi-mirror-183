from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Details(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    policy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        policy: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Details.Args(
                name=name,
                policy=policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        policy: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_s3control_multi_region_access_point_policy", namespace="aws_s3control")
class MultiRegionAccessPointPolicy(core.Resource):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    details: Details = core.attr(Details)

    established: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    proposed: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        details: Details,
        account_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MultiRegionAccessPointPolicy.Args(
                details=details,
                account_id=account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        details: Details = core.arg()
