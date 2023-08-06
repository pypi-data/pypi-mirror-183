from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class TagFilter(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=TagFilter.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class ComplianceDetails(core.Schema):

    compliance_status: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    keys_with_noncompliant_values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    non_compliant_keys: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        compliance_status: Union[bool, core.BoolOut],
        keys_with_noncompliant_values: Union[List[str], core.ArrayOut[core.StringOut]],
        non_compliant_keys: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=ComplianceDetails.Args(
                compliance_status=compliance_status,
                keys_with_noncompliant_values=keys_with_noncompliant_values,
                non_compliant_keys=non_compliant_keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compliance_status: Union[bool, core.BoolOut] = core.arg()

        keys_with_noncompliant_values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        non_compliant_keys: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class ResourceTagMappingList(core.Schema):

    compliance_details: Union[
        List[ComplianceDetails], core.ArrayOut[ComplianceDetails]
    ] = core.attr(ComplianceDetails, computed=True, kind=core.Kind.array)

    resource_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        compliance_details: Union[List[ComplianceDetails], core.ArrayOut[ComplianceDetails]],
        resource_arn: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=ResourceTagMappingList.Args(
                compliance_details=compliance_details,
                resource_arn=resource_arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compliance_details: Union[
            List[ComplianceDetails], core.ArrayOut[ComplianceDetails]
        ] = core.arg()

        resource_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)


@core.data(type="aws_resourcegroupstaggingapi_resources", namespace="aws_resourcegroupstagging")
class DsApiResources(core.Data):

    exclude_compliant_resources: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    include_compliance_details: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    resource_arn_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    resource_tag_mapping_list: Union[
        List[ResourceTagMappingList], core.ArrayOut[ResourceTagMappingList]
    ] = core.attr(ResourceTagMappingList, computed=True, kind=core.Kind.array)

    resource_type_filters: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tag_filter: Optional[Union[List[TagFilter], core.ArrayOut[TagFilter]]] = core.attr(
        TagFilter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        exclude_compliant_resources: Optional[Union[bool, core.BoolOut]] = None,
        include_compliance_details: Optional[Union[bool, core.BoolOut]] = None,
        resource_arn_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        resource_type_filters: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tag_filter: Optional[Union[List[TagFilter], core.ArrayOut[TagFilter]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsApiResources.Args(
                exclude_compliant_resources=exclude_compliant_resources,
                include_compliance_details=include_compliance_details,
                resource_arn_list=resource_arn_list,
                resource_type_filters=resource_type_filters,
                tag_filter=tag_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exclude_compliant_resources: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_compliance_details: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        resource_arn_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        resource_type_filters: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tag_filter: Optional[Union[List[TagFilter], core.ArrayOut[TagFilter]]] = core.arg(
            default=None
        )
