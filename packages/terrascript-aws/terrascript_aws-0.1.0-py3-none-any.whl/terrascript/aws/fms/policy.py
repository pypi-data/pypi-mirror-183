from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class IncludeMap(core.Schema):

    account: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    orgunit: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        account: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        orgunit: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=IncludeMap.Args(
                account=account,
                orgunit=orgunit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        orgunit: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class SecurityServicePolicyData(core.Schema):

    managed_service_data: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        managed_service_data: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SecurityServicePolicyData.Args(
                type=type,
                managed_service_data=managed_service_data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        managed_service_data: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class ExcludeMap(core.Schema):

    account: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    orgunit: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        account: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        orgunit: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=ExcludeMap.Args(
                account=account,
                orgunit=orgunit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        orgunit: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.resource(type="aws_fms_policy", namespace="aws_fms")
class Policy(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    delete_all_policy_resources: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    delete_unused_fm_managed_resources: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    exclude_map: Optional[ExcludeMap] = core.attr(ExcludeMap, default=None)

    exclude_resource_tags: Union[bool, core.BoolOut] = core.attr(bool)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    include_map: Optional[IncludeMap] = core.attr(IncludeMap, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    policy_update_token: Union[str, core.StringOut] = core.attr(str, computed=True)

    remediation_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    resource_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    resource_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    resource_type_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    security_service_policy_data: SecurityServicePolicyData = core.attr(SecurityServicePolicyData)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        exclude_resource_tags: Union[bool, core.BoolOut],
        name: Union[str, core.StringOut],
        security_service_policy_data: SecurityServicePolicyData,
        delete_all_policy_resources: Optional[Union[bool, core.BoolOut]] = None,
        delete_unused_fm_managed_resources: Optional[Union[bool, core.BoolOut]] = None,
        exclude_map: Optional[ExcludeMap] = None,
        include_map: Optional[IncludeMap] = None,
        remediation_enabled: Optional[Union[bool, core.BoolOut]] = None,
        resource_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        resource_type: Optional[Union[str, core.StringOut]] = None,
        resource_type_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Policy.Args(
                exclude_resource_tags=exclude_resource_tags,
                name=name,
                security_service_policy_data=security_service_policy_data,
                delete_all_policy_resources=delete_all_policy_resources,
                delete_unused_fm_managed_resources=delete_unused_fm_managed_resources,
                exclude_map=exclude_map,
                include_map=include_map,
                remediation_enabled=remediation_enabled,
                resource_tags=resource_tags,
                resource_type=resource_type,
                resource_type_list=resource_type_list,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delete_all_policy_resources: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        delete_unused_fm_managed_resources: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        exclude_map: Optional[ExcludeMap] = core.arg(default=None)

        exclude_resource_tags: Union[bool, core.BoolOut] = core.arg()

        include_map: Optional[IncludeMap] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        remediation_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        resource_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        resource_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resource_type_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        security_service_policy_data: SecurityServicePolicyData = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
