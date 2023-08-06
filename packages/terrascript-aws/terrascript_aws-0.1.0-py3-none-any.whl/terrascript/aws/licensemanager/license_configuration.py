from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_licensemanager_license_configuration", namespace="aws_licensemanager")
class LicenseConfiguration(core.Resource):
    """
    The license configuration ARN.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) Description of the license configuration.
    """
    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    The license configuration ARN.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) Number of licenses managed by the license configuration.
    """
    license_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    """
    (Optional) Sets the number of available licenses as a hard limit.
    """
    license_count_hard_limit: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    """
    (Required) Dimension to use to track license inventory. Specify either `vCPU`, `Instance`, `Core` or
    Socket`.
    """
    license_counting_type: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) Array of configured License Manager rules.
    """
    license_rules: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) Name of the license configuration.
    """
    name: Union[str, core.StringOut] = core.attr(str)

    """
    Account ID of the owner of the license configuration.
    """
    owner_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        license_counting_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        license_count: Optional[Union[int, core.IntOut]] = None,
        license_count_hard_limit: Optional[Union[bool, core.BoolOut]] = None,
        license_rules: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LicenseConfiguration.Args(
                license_counting_type=license_counting_type,
                name=name,
                description=description,
                license_count=license_count,
                license_count_hard_limit=license_count_hard_limit,
                license_rules=license_rules,
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

        license_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        license_count_hard_limit: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        license_counting_type: Union[str, core.StringOut] = core.arg()

        license_rules: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
