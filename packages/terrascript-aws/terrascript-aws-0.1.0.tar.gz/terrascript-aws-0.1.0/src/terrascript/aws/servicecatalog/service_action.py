from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Definition(core.Schema):

    assume_role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    parameters: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    version: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        version: Union[str, core.StringOut],
        assume_role: Optional[Union[str, core.StringOut]] = None,
        parameters: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Definition.Args(
                name=name,
                version=version,
                assume_role=assume_role,
                parameters=parameters,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        assume_role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        parameters: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_servicecatalog_service_action", namespace="aws_servicecatalog")
class ServiceAction(core.Resource):

    accept_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    definition: Definition = core.attr(Definition)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        definition: Definition,
        name: Union[str, core.StringOut],
        accept_language: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceAction.Args(
                definition=definition,
                name=name,
                accept_language=accept_language,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        definition: Definition = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()
