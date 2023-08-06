from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Target(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Target.Args(
                id=id,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_directory_service_shared_directory", namespace="aws_ds")
class DirectoryServiceSharedDirectory(core.Resource):

    directory_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    method: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    notes: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    shared_directory_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    target: Target = core.attr(Target)

    def __init__(
        self,
        resource_name: str,
        *,
        directory_id: Union[str, core.StringOut],
        target: Target,
        method: Optional[Union[str, core.StringOut]] = None,
        notes: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceSharedDirectory.Args(
                directory_id=directory_id,
                target=target,
                method=method,
                notes=notes,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        directory_id: Union[str, core.StringOut] = core.arg()

        method: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        notes: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target: Target = core.arg()
