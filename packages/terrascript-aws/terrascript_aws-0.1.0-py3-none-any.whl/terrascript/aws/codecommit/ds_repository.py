from typing import Union

import terrascript.core as core


@core.data(type="aws_codecommit_repository", namespace="aws_codecommit")
class DsRepository(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    clone_url_http: Union[str, core.StringOut] = core.attr(str, computed=True)

    clone_url_ssh: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    repository_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    repository_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        repository_name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsRepository.Args(
                repository_name=repository_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        repository_name: Union[str, core.StringOut] = core.arg()
