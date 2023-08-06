from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class UiTemplate(core.Schema):

    content: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    content_sha256: Union[str, core.StringOut] = core.attr(str, computed=True)

    url: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        content_sha256: Union[str, core.StringOut],
        url: Union[str, core.StringOut],
        content: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=UiTemplate.Args(
                content_sha256=content_sha256,
                url=url,
                content=content,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_sha256: Union[str, core.StringOut] = core.arg()

        url: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_sagemaker_human_task_ui", namespace="aws_sagemaker")
class HumanTaskUi(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    human_task_ui_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    ui_template: UiTemplate = core.attr(UiTemplate)

    def __init__(
        self,
        resource_name: str,
        *,
        human_task_ui_name: Union[str, core.StringOut],
        ui_template: UiTemplate,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=HumanTaskUi.Args(
                human_task_ui_name=human_task_ui_name,
                ui_template=ui_template,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        human_task_ui_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        ui_template: UiTemplate = core.arg()
