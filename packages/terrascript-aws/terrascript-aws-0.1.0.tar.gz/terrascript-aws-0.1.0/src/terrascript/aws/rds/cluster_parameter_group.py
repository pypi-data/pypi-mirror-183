from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Parameter(core.Schema):

    apply_method: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
        apply_method: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Parameter.Args(
                name=name,
                value=value,
                apply_method=apply_method,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        apply_method: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_rds_cluster_parameter_group", namespace="aws_rds")
class ClusterParameterGroup(core.Resource):
    """
    The ARN of the db cluster parameter group.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) The description of the DB cluster parameter group. Defaults to "Managed by Terraform".
    """
    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Required) The family of the DB cluster parameter group.
    """
    family: Union[str, core.StringOut] = core.attr(str)

    """
    The db cluster parameter group name.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The name of the DB cluster parameter group. If omitted, Terraform wi
    ll assign a random, unique name.
    """
    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts
    with `name`.
    """
    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    """
    (Optional) A list of DB parameters to apply. Note that parameters may differ from a family to an oth
    er. Full list of all parameters can be discovered via [`aws rds describe-db-cluster-parameters`](htt
    ps://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameters.html) after initial
    creation of the group.
    """
    parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        family: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterParameterGroup.Args(
                family=family,
                description=description,
                name=name,
                name_prefix=name_prefix,
                parameter=parameter,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        family: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
