from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class UserStorage(core.Schema):

    capacity: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        capacity: Union[str, core.StringOut],
    ):
        super().__init__(
            args=UserStorage.Args(
                capacity=capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity: Union[str, core.StringOut] = core.arg()


@core.schema
class RootStorage(core.Schema):

    capacity: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        capacity: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RootStorage.Args(
                capacity=capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity: Union[str, core.StringOut] = core.arg()


@core.schema
class ComputeType(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ComputeType.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_workspaces_bundle", namespace="aws_workspaces")
class DsBundle(core.Data):

    bundle_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    compute_type: Union[List[ComputeType], core.ArrayOut[ComputeType]] = core.attr(
        ComputeType, computed=True, kind=core.Kind.array
    )

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    root_storage: Union[List[RootStorage], core.ArrayOut[RootStorage]] = core.attr(
        RootStorage, computed=True, kind=core.Kind.array
    )

    user_storage: Union[List[UserStorage], core.ArrayOut[UserStorage]] = core.attr(
        UserStorage, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        bundle_id: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        owner: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsBundle.Args(
                bundle_id=bundle_id,
                name=name,
                owner=owner,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bundle_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)
