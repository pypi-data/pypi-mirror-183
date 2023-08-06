from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class HealthCheck(core.Schema):

    healthy_threshold: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    interval_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    success_codes: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    timeout_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    unhealthy_threshold: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        healthy_threshold: Optional[Union[int, core.IntOut]] = None,
        interval_seconds: Optional[Union[int, core.IntOut]] = None,
        path: Optional[Union[str, core.StringOut]] = None,
        success_codes: Optional[Union[str, core.StringOut]] = None,
        timeout_seconds: Optional[Union[int, core.IntOut]] = None,
        unhealthy_threshold: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=HealthCheck.Args(
                healthy_threshold=healthy_threshold,
                interval_seconds=interval_seconds,
                path=path,
                success_codes=success_codes,
                timeout_seconds=timeout_seconds,
                unhealthy_threshold=unhealthy_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        healthy_threshold: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        interval_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        success_codes: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        timeout_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        unhealthy_threshold: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class PublicEndpoint(core.Schema):

    container_name: Union[str, core.StringOut] = core.attr(str)

    container_port: Union[int, core.IntOut] = core.attr(int)

    health_check: HealthCheck = core.attr(HealthCheck)

    def __init__(
        self,
        *,
        container_name: Union[str, core.StringOut],
        container_port: Union[int, core.IntOut],
        health_check: HealthCheck,
    ):
        super().__init__(
            args=PublicEndpoint.Args(
                container_name=container_name,
                container_port=container_port,
                health_check=health_check,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_name: Union[str, core.StringOut] = core.arg()

        container_port: Union[int, core.IntOut] = core.arg()

        health_check: HealthCheck = core.arg()


@core.schema
class Container(core.Schema):

    command: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    container_name: Union[str, core.StringOut] = core.attr(str)

    environment: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    image: Union[str, core.StringOut] = core.attr(str)

    ports: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        container_name: Union[str, core.StringOut],
        image: Union[str, core.StringOut],
        command: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        environment: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        ports: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Container.Args(
                container_name=container_name,
                image=image,
                command=command,
                environment=environment,
                ports=ports,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        command: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        container_name: Union[str, core.StringOut] = core.arg()

        environment: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        image: Union[str, core.StringOut] = core.arg()

        ports: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)


@core.resource(type="aws_lightsail_container_service_deployment_version", namespace="aws_lightsail")
class ContainerServiceDeploymentVersion(core.Resource):

    container: Union[List[Container], core.ArrayOut[Container]] = core.attr(
        Container, kind=core.Kind.array
    )

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_endpoint: Optional[PublicEndpoint] = core.attr(PublicEndpoint, default=None)

    service_name: Union[str, core.StringOut] = core.attr(str)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    version: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        container: Union[List[Container], core.ArrayOut[Container]],
        service_name: Union[str, core.StringOut],
        public_endpoint: Optional[PublicEndpoint] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ContainerServiceDeploymentVersion.Args(
                container=container,
                service_name=service_name,
                public_endpoint=public_endpoint,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        container: Union[List[Container], core.ArrayOut[Container]] = core.arg()

        public_endpoint: Optional[PublicEndpoint] = core.arg(default=None)

        service_name: Union[str, core.StringOut] = core.arg()
