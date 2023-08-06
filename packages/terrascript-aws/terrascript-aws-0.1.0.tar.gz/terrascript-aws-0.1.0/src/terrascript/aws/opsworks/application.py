from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Environment(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    secure: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
        secure: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Environment.Args(
                key=key,
                value=value,
                secure=secure,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        secure: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class SslConfiguration(core.Schema):

    certificate: Union[str, core.StringOut] = core.attr(str)

    chain: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    private_key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        certificate: Union[str, core.StringOut],
        private_key: Union[str, core.StringOut],
        chain: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SslConfiguration.Args(
                certificate=certificate,
                private_key=private_key,
                chain=chain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate: Union[str, core.StringOut] = core.arg()

        chain: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        private_key: Union[str, core.StringOut] = core.arg()


@core.schema
class AppSource(core.Schema):

    password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    revision: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssh_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    username: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        password: Optional[Union[str, core.StringOut]] = None,
        revision: Optional[Union[str, core.StringOut]] = None,
        ssh_key: Optional[Union[str, core.StringOut]] = None,
        url: Optional[Union[str, core.StringOut]] = None,
        username: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AppSource.Args(
                type=type,
                password=password,
                revision=revision,
                ssh_key=ssh_key,
                url=url,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        revision: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssh_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()

        url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        username: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_opsworks_application", namespace="aws_opsworks")
class Application(core.Resource):

    app_source: Optional[Union[List[AppSource], core.ArrayOut[AppSource]]] = core.attr(
        AppSource, default=None, computed=True, kind=core.Kind.array
    )

    auto_bundle_on_deploy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    aws_flow_ruby_settings: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    data_source_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    data_source_database_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    data_source_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    document_root: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    domains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    enable_ssl: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    environment: Optional[Union[List[Environment], core.ArrayOut[Environment]]] = core.attr(
        Environment, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    rails_env: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    short_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    ssl_configuration: Optional[
        Union[List[SslConfiguration], core.ArrayOut[SslConfiguration]]
    ] = core.attr(SslConfiguration, default=None, kind=core.Kind.array)

    stack_id: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        stack_id: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        app_source: Optional[Union[List[AppSource], core.ArrayOut[AppSource]]] = None,
        auto_bundle_on_deploy: Optional[Union[str, core.StringOut]] = None,
        aws_flow_ruby_settings: Optional[Union[str, core.StringOut]] = None,
        data_source_arn: Optional[Union[str, core.StringOut]] = None,
        data_source_database_name: Optional[Union[str, core.StringOut]] = None,
        data_source_type: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        document_root: Optional[Union[str, core.StringOut]] = None,
        domains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        enable_ssl: Optional[Union[bool, core.BoolOut]] = None,
        environment: Optional[Union[List[Environment], core.ArrayOut[Environment]]] = None,
        rails_env: Optional[Union[str, core.StringOut]] = None,
        short_name: Optional[Union[str, core.StringOut]] = None,
        ssl_configuration: Optional[
            Union[List[SslConfiguration], core.ArrayOut[SslConfiguration]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Application.Args(
                name=name,
                stack_id=stack_id,
                type=type,
                app_source=app_source,
                auto_bundle_on_deploy=auto_bundle_on_deploy,
                aws_flow_ruby_settings=aws_flow_ruby_settings,
                data_source_arn=data_source_arn,
                data_source_database_name=data_source_database_name,
                data_source_type=data_source_type,
                description=description,
                document_root=document_root,
                domains=domains,
                enable_ssl=enable_ssl,
                environment=environment,
                rails_env=rails_env,
                short_name=short_name,
                ssl_configuration=ssl_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_source: Optional[Union[List[AppSource], core.ArrayOut[AppSource]]] = core.arg(
            default=None
        )

        auto_bundle_on_deploy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        aws_flow_ruby_settings: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        data_source_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        data_source_database_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        data_source_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        document_root: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        domains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        enable_ssl: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        environment: Optional[Union[List[Environment], core.ArrayOut[Environment]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        rails_env: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        short_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssl_configuration: Optional[
            Union[List[SslConfiguration], core.ArrayOut[SslConfiguration]]
        ] = core.arg(default=None)

        stack_id: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()
