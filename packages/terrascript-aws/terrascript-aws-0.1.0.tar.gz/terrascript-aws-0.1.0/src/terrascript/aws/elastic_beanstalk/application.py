from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AppversionLifecycle(core.Schema):

    delete_source_from_s3: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    max_age_in_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    max_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    service_role: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        service_role: Union[str, core.StringOut],
        delete_source_from_s3: Optional[Union[bool, core.BoolOut]] = None,
        max_age_in_days: Optional[Union[int, core.IntOut]] = None,
        max_count: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=AppversionLifecycle.Args(
                service_role=service_role,
                delete_source_from_s3=delete_source_from_s3,
                max_age_in_days=max_age_in_days,
                max_count=max_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_source_from_s3: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        max_age_in_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        max_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        service_role: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_elastic_beanstalk_application", namespace="aws_elastic_beanstalk")
class Application(core.Resource):

    appversion_lifecycle: Optional[AppversionLifecycle] = core.attr(
        AppversionLifecycle, default=None
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        appversion_lifecycle: Optional[AppversionLifecycle] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Application.Args(
                name=name,
                appversion_lifecycle=appversion_lifecycle,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        appversion_lifecycle: Optional[AppversionLifecycle] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
