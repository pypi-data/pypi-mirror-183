from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CacheAttributes(core.Schema):

    cache_stale_timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        cache_stale_timeout_in_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CacheAttributes.Args(
                cache_stale_timeout_in_seconds=cache_stale_timeout_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cache_stale_timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_storagegateway_file_system_association", namespace="aws_storagegateway")
class FileSystemAssociation(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    audit_destination_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cache_attributes: Optional[CacheAttributes] = core.attr(CacheAttributes, default=None)

    gateway_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    location_arn: Union[str, core.StringOut] = core.attr(str)

    password: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        gateway_arn: Union[str, core.StringOut],
        location_arn: Union[str, core.StringOut],
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
        audit_destination_arn: Optional[Union[str, core.StringOut]] = None,
        cache_attributes: Optional[CacheAttributes] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FileSystemAssociation.Args(
                gateway_arn=gateway_arn,
                location_arn=location_arn,
                password=password,
                username=username,
                audit_destination_arn=audit_destination_arn,
                cache_attributes=cache_attributes,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        audit_destination_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cache_attributes: Optional[CacheAttributes] = core.arg(default=None)

        gateway_arn: Union[str, core.StringOut] = core.arg()

        location_arn: Union[str, core.StringOut] = core.arg()

        password: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        username: Union[str, core.StringOut] = core.arg()
