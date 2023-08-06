from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_appsync_api_cache", namespace="aws_appsync")
class ApiCache(core.Resource):

    api_caching_behavior: Union[str, core.StringOut] = core.attr(str)

    api_id: Union[str, core.StringOut] = core.attr(str)

    at_rest_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    transit_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ttl: Union[int, core.IntOut] = core.attr(int)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_caching_behavior: Union[str, core.StringOut],
        api_id: Union[str, core.StringOut],
        ttl: Union[int, core.IntOut],
        type: Union[str, core.StringOut],
        at_rest_encryption_enabled: Optional[Union[bool, core.BoolOut]] = None,
        transit_encryption_enabled: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ApiCache.Args(
                api_caching_behavior=api_caching_behavior,
                api_id=api_id,
                ttl=ttl,
                type=type,
                at_rest_encryption_enabled=at_rest_encryption_enabled,
                transit_encryption_enabled=transit_encryption_enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_caching_behavior: Union[str, core.StringOut] = core.arg()

        api_id: Union[str, core.StringOut] = core.arg()

        at_rest_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        transit_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ttl: Union[int, core.IntOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()
