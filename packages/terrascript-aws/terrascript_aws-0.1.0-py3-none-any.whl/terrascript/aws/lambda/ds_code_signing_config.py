from typing import List, Union

import terrascript.core as core


@core.schema
class AllowedPublishers(core.Schema):

    signing_profile_version_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
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

    untrusted_artifact_on_deployment: Union[str, core.StringOut] = core.attr(str, computed=True)

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


@core.data(type="aws_lambda_code_signing_config", namespace="aws_lambda")
class DsCodeSigningConfig(core.Data):

    allowed_publishers: Union[
        List[AllowedPublishers], core.ArrayOut[AllowedPublishers]
    ] = core.attr(AllowedPublishers, computed=True, kind=core.Kind.array)

    arn: Union[str, core.StringOut] = core.attr(str)

    config_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified: Union[str, core.StringOut] = core.attr(str, computed=True)

    policies: Union[List[Policies], core.ArrayOut[Policies]] = core.attr(
        Policies, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsCodeSigningConfig.Args(
                arn=arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()
