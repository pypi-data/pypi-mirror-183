from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Filter(core.Schema):

    json_path: Union[str, core.StringOut] = core.attr(str)

    match_equals: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        json_path: Union[str, core.StringOut],
        match_equals: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                json_path=json_path,
                match_equals=match_equals,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        json_path: Union[str, core.StringOut] = core.arg()

        match_equals: Union[str, core.StringOut] = core.arg()


@core.schema
class AuthenticationConfiguration(core.Schema):

    allowed_ip_range: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    secret_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        allowed_ip_range: Optional[Union[str, core.StringOut]] = None,
        secret_token: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AuthenticationConfiguration.Args(
                allowed_ip_range=allowed_ip_range,
                secret_token=secret_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allowed_ip_range: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        secret_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_codepipeline_webhook", namespace="aws_codepipeline")
class Webhook(core.Resource):
    """
    The CodePipeline webhook's ARN.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
    """
    authentication: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
    """
    authentication_configuration: Optional[AuthenticationConfiguration] = core.attr(
        AuthenticationConfiguration, default=None
    )

    filter: Union[List[Filter], core.ArrayOut[Filter]] = core.attr(Filter, kind=core.Kind.array)

    """
    The CodePipeline webhook's ARN.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The name of the webhook.
    """
    name: Union[str, core.StringOut] = core.attr(str)

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

    """
    (Required) The name of the action in a pipeline you want to connect to the webhook. The action must
    be from the source (first) stage of the pipeline.
    """
    target_action: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) The name of the pipeline.
    """
    target_pipeline: Union[str, core.StringOut] = core.attr(str)

    """
    The CodePipeline webhook's URL. POST events to this endpoint to trigger the target.
    """
    url: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        authentication: Union[str, core.StringOut],
        filter: Union[List[Filter], core.ArrayOut[Filter]],
        name: Union[str, core.StringOut],
        target_action: Union[str, core.StringOut],
        target_pipeline: Union[str, core.StringOut],
        authentication_configuration: Optional[AuthenticationConfiguration] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Webhook.Args(
                authentication=authentication,
                filter=filter,
                name=name,
                target_action=target_action,
                target_pipeline=target_pipeline,
                authentication_configuration=authentication_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authentication: Union[str, core.StringOut] = core.arg()

        authentication_configuration: Optional[AuthenticationConfiguration] = core.arg(default=None)

        filter: Union[List[Filter], core.ArrayOut[Filter]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_action: Union[str, core.StringOut] = core.arg()

        target_pipeline: Union[str, core.StringOut] = core.arg()
