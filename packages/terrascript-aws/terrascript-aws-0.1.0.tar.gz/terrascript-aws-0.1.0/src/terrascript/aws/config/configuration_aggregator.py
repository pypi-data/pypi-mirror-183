from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AccountAggregationSource(core.Schema):

    account_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    all_regions: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        account_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        all_regions: Optional[Union[bool, core.BoolOut]] = None,
        regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AccountAggregationSource.Args(
                account_ids=account_ids,
                all_regions=all_regions,
                regions=regions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        all_regions: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class OrganizationAggregationSource(core.Schema):

    all_regions: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: Union[str, core.StringOut],
        all_regions: Optional[Union[bool, core.BoolOut]] = None,
        regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=OrganizationAggregationSource.Args(
                role_arn=role_arn,
                all_regions=all_regions,
                regions=regions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        all_regions: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_config_configuration_aggregator", namespace="aws_config")
class ConfigurationAggregator(core.Resource):

    account_aggregation_source: Optional[AccountAggregationSource] = core.attr(
        AccountAggregationSource, default=None
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    organization_aggregation_source: Optional[OrganizationAggregationSource] = core.attr(
        OrganizationAggregationSource, default=None
    )

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
        name: Union[str, core.StringOut],
        account_aggregation_source: Optional[AccountAggregationSource] = None,
        organization_aggregation_source: Optional[OrganizationAggregationSource] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigurationAggregator.Args(
                name=name,
                account_aggregation_source=account_aggregation_source,
                organization_aggregation_source=organization_aggregation_source,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_aggregation_source: Optional[AccountAggregationSource] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        organization_aggregation_source: Optional[OrganizationAggregationSource] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
