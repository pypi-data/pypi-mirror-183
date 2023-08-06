from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_sagemaker_model_package_group_policy", namespace="aws_sagemaker")
class ModelPackageGroupPolicy(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    model_package_group_name: Union[str, core.StringOut] = core.attr(str)

    resource_policy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        model_package_group_name: Union[str, core.StringOut],
        resource_policy: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ModelPackageGroupPolicy.Args(
                model_package_group_name=model_package_group_name,
                resource_policy=resource_policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        model_package_group_name: Union[str, core.StringOut] = core.arg()

        resource_policy: Union[str, core.StringOut] = core.arg()
