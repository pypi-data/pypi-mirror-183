from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_opsworks_rds_db_instance", namespace="aws_opsworks")
class RdsDbInstance(core.Resource):

    db_password: Union[str, core.StringOut] = core.attr(str)

    db_user: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    rds_db_instance_arn: Union[str, core.StringOut] = core.attr(str)

    stack_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        db_password: Union[str, core.StringOut],
        db_user: Union[str, core.StringOut],
        rds_db_instance_arn: Union[str, core.StringOut],
        stack_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RdsDbInstance.Args(
                db_password=db_password,
                db_user=db_user,
                rds_db_instance_arn=rds_db_instance_arn,
                stack_id=stack_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        db_password: Union[str, core.StringOut] = core.arg()

        db_user: Union[str, core.StringOut] = core.arg()

        rds_db_instance_arn: Union[str, core.StringOut] = core.arg()

        stack_id: Union[str, core.StringOut] = core.arg()
