from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class GitConfig(core.Schema):

    branch: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    repository_url: Union[str, core.StringOut] = core.attr(str)

    secret_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        repository_url: Union[str, core.StringOut],
        branch: Optional[Union[str, core.StringOut]] = None,
        secret_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=GitConfig.Args(
                repository_url=repository_url,
                branch=branch,
                secret_arn=secret_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        branch: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        repository_url: Union[str, core.StringOut] = core.arg()

        secret_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_sagemaker_code_repository", namespace="aws_sagemaker")
class CodeRepository(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    code_repository_name: Union[str, core.StringOut] = core.attr(str)

    git_config: GitConfig = core.attr(GitConfig)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        code_repository_name: Union[str, core.StringOut],
        git_config: GitConfig,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CodeRepository.Args(
                code_repository_name=code_repository_name,
                git_config=git_config,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        code_repository_name: Union[str, core.StringOut] = core.arg()

        git_config: GitConfig = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
