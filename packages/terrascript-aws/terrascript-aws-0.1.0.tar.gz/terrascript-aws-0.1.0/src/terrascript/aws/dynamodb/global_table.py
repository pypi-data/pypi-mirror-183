from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Replica(core.Schema):

    region_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        region_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Replica.Args(
                region_name=region_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region_name: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_dynamodb_global_table", namespace="aws_dynamodb")
class GlobalTable(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    replica: Union[List[Replica], core.ArrayOut[Replica]] = core.attr(Replica, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        replica: Union[List[Replica], core.ArrayOut[Replica]],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GlobalTable.Args(
                name=name,
                replica=replica,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        replica: Union[List[Replica], core.ArrayOut[Replica]] = core.arg()
