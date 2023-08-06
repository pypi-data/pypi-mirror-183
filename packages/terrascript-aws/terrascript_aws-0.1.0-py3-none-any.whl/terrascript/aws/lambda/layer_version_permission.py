from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lambda_layer_version_permission", namespace="aws_lambda")
class LayerVersionPermission(core.Resource):

    action: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    layer_name: Union[str, core.StringOut] = core.attr(str)

    organization_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    policy: Union[str, core.StringOut] = core.attr(str, computed=True)

    principal: Union[str, core.StringOut] = core.attr(str)

    revision_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    statement_id: Union[str, core.StringOut] = core.attr(str)

    version_number: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        action: Union[str, core.StringOut],
        layer_name: Union[str, core.StringOut],
        principal: Union[str, core.StringOut],
        statement_id: Union[str, core.StringOut],
        version_number: Union[int, core.IntOut],
        organization_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LayerVersionPermission.Args(
                action=action,
                layer_name=layer_name,
                principal=principal,
                statement_id=statement_id,
                version_number=version_number,
                organization_id=organization_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: Union[str, core.StringOut] = core.arg()

        layer_name: Union[str, core.StringOut] = core.arg()

        organization_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        principal: Union[str, core.StringOut] = core.arg()

        statement_id: Union[str, core.StringOut] = core.arg()

        version_number: Union[int, core.IntOut] = core.arg()
