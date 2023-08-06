from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_codeartifact_repository_endpoint", namespace="aws_codeartifact")
class DsRepositoryEndpoint(core.Data):

    domain: Union[str, core.StringOut] = core.attr(str)

    domain_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    format: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    repository: Union[str, core.StringOut] = core.attr(str)

    repository_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        domain: Union[str, core.StringOut],
        format: Union[str, core.StringOut],
        repository: Union[str, core.StringOut],
        domain_owner: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRepositoryEndpoint.Args(
                domain=domain,
                format=format,
                repository=repository,
                domain_owner=domain_owner,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain: Union[str, core.StringOut] = core.arg()

        domain_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        format: Union[str, core.StringOut] = core.arg()

        repository: Union[str, core.StringOut] = core.arg()
