from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ScalingParameters(core.Schema):

    desired_instance_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    desired_partition_count: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    desired_replication_count: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    def __init__(
        self,
        *,
        desired_instance_type: Optional[Union[str, core.StringOut]] = None,
        desired_partition_count: Optional[Union[int, core.IntOut]] = None,
        desired_replication_count: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ScalingParameters.Args(
                desired_instance_type=desired_instance_type,
                desired_partition_count=desired_partition_count,
                desired_replication_count=desired_replication_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        desired_instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        desired_partition_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        desired_replication_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class IndexField(core.Schema):

    analysis_scheme: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    default_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    facet: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    highlight: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    return_: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, alias="return")

    search: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    sort: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    source_fields: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        analysis_scheme: Optional[Union[str, core.StringOut]] = None,
        default_value: Optional[Union[str, core.StringOut]] = None,
        facet: Optional[Union[bool, core.BoolOut]] = None,
        highlight: Optional[Union[bool, core.BoolOut]] = None,
        return_: Optional[Union[bool, core.BoolOut]] = None,
        search: Optional[Union[bool, core.BoolOut]] = None,
        sort: Optional[Union[bool, core.BoolOut]] = None,
        source_fields: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=IndexField.Args(
                name=name,
                type=type,
                analysis_scheme=analysis_scheme,
                default_value=default_value,
                facet=facet,
                highlight=highlight,
                return_=return_,
                search=search,
                sort=sort,
                source_fields=source_fields,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        analysis_scheme: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        facet: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        highlight: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        return_: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        search: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        sort: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        source_fields: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class EndpointOptions(core.Schema):

    enforce_https: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    tls_security_policy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        enforce_https: Optional[Union[bool, core.BoolOut]] = None,
        tls_security_policy: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EndpointOptions.Args(
                enforce_https=enforce_https,
                tls_security_policy=tls_security_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enforce_https: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tls_security_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_cloudsearch_domain", namespace="aws_cloudsearch")
class Domain(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    document_service_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint_options: Optional[EndpointOptions] = core.attr(
        EndpointOptions, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_field: Optional[Union[List[IndexField], core.ArrayOut[IndexField]]] = core.attr(
        IndexField, default=None, kind=core.Kind.array
    )

    multi_az: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    scaling_parameters: Optional[ScalingParameters] = core.attr(
        ScalingParameters, default=None, computed=True
    )

    search_service_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        endpoint_options: Optional[EndpointOptions] = None,
        index_field: Optional[Union[List[IndexField], core.ArrayOut[IndexField]]] = None,
        multi_az: Optional[Union[bool, core.BoolOut]] = None,
        scaling_parameters: Optional[ScalingParameters] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Domain.Args(
                name=name,
                endpoint_options=endpoint_options,
                index_field=index_field,
                multi_az=multi_az,
                scaling_parameters=scaling_parameters,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        endpoint_options: Optional[EndpointOptions] = core.arg(default=None)

        index_field: Optional[Union[List[IndexField], core.ArrayOut[IndexField]]] = core.arg(
            default=None
        )

        multi_az: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        scaling_parameters: Optional[ScalingParameters] = core.arg(default=None)
