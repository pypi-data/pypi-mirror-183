from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_db_instance_role_association", namespace="aws_rds")
class DbInstanceRoleAssociation(core.Resource):

    db_instance_identifier: Union[str, core.StringOut] = core.attr(str)

    feature_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        db_instance_identifier: Union[str, core.StringOut],
        feature_name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbInstanceRoleAssociation.Args(
                db_instance_identifier=db_instance_identifier,
                feature_name=feature_name,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        db_instance_identifier: Union[str, core.StringOut] = core.arg()

        feature_name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()
