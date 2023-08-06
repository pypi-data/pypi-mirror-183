from typing import List, Optional, Union

import terrascript.core as core


@core.data(
    type="aws_serverlessapplicationrepository_application",
    namespace="aws_serverlessapplicationrepository",
)
class DsApplication(core.Data):

    application_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    required_capabilities: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    semantic_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    source_code_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    template_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        application_id: Union[str, core.StringOut],
        semantic_version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsApplication.Args(
                application_id=application_id,
                semantic_version=semantic_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        application_id: Union[str, core.StringOut] = core.arg()

        semantic_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)
