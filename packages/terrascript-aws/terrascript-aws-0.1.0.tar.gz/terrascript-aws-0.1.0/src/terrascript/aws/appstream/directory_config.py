from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ServiceAccountCredentials(core.Schema):

    account_name: Union[str, core.StringOut] = core.attr(str)

    account_password: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        account_name: Union[str, core.StringOut],
        account_password: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ServiceAccountCredentials.Args(
                account_name=account_name,
                account_password=account_password,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_name: Union[str, core.StringOut] = core.arg()

        account_password: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_appstream_directory_config", namespace="aws_appstream")
class DirectoryConfig(core.Resource):

    created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    directory_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    organizational_unit_distinguished_names: Union[
        List[str], core.ArrayOut[core.StringOut]
    ] = core.attr(str, kind=core.Kind.array)

    service_account_credentials: ServiceAccountCredentials = core.attr(ServiceAccountCredentials)

    def __init__(
        self,
        resource_name: str,
        *,
        directory_name: Union[str, core.StringOut],
        organizational_unit_distinguished_names: Union[List[str], core.ArrayOut[core.StringOut]],
        service_account_credentials: ServiceAccountCredentials,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryConfig.Args(
                directory_name=directory_name,
                organizational_unit_distinguished_names=organizational_unit_distinguished_names,
                service_account_credentials=service_account_credentials,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        directory_name: Union[str, core.StringOut] = core.arg()

        organizational_unit_distinguished_names: Union[
            List[str], core.ArrayOut[core.StringOut]
        ] = core.arg()

        service_account_credentials: ServiceAccountCredentials = core.arg()
