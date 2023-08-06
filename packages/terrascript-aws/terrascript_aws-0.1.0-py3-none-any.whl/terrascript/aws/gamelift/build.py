from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class StorageLocation(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str)

    key: Union[str, core.StringOut] = core.attr(str)

    object_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        object_version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=StorageLocation.Args(
                bucket=bucket,
                key=key,
                role_arn=role_arn,
                object_version=object_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()

        object_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_gamelift_build", namespace="aws_gamelift")
class Build(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    operating_system: Union[str, core.StringOut] = core.attr(str)

    storage_location: StorageLocation = core.attr(StorageLocation)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        operating_system: Union[str, core.StringOut],
        storage_location: StorageLocation,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        version: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Build.Args(
                name=name,
                operating_system=operating_system,
                storage_location=storage_location,
                tags=tags,
                tags_all=tags_all,
                version=version,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        operating_system: Union[str, core.StringOut] = core.arg()

        storage_location: StorageLocation = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)
