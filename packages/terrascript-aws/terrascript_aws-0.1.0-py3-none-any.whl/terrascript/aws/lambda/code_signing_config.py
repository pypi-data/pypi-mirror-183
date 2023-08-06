from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class AllowedPublishers(core.Schema):

    signing_profile_version_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        signing_profile_version_arns: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=AllowedPublishers.Args(
                signing_profile_version_arns=signing_profile_version_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        signing_profile_version_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Policies(core.Schema):

    untrusted_artifact_on_deployment: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        untrusted_artifact_on_deployment: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Policies.Args(
                untrusted_artifact_on_deployment=untrusted_artifact_on_deployment,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        untrusted_artifact_on_deployment: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_lambda_code_signing_config", namespace="aws_lambda")
class CodeSigningConfig(core.Resource):

    allowed_publishers: AllowedPublishers = core.attr(AllowedPublishers)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    config_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified: Union[str, core.StringOut] = core.attr(str, computed=True)

    policies: Optional[Policies] = core.attr(Policies, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        allowed_publishers: AllowedPublishers,
        description: Optional[Union[str, core.StringOut]] = None,
        policies: Optional[Policies] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CodeSigningConfig.Args(
                allowed_publishers=allowed_publishers,
                description=description,
                policies=policies,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allowed_publishers: AllowedPublishers = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policies: Optional[Policies] = core.arg(default=None)
