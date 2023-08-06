from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class SelfManagedActiveDirectoryConfiguration(core.Schema):

    dns_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    file_system_administrators_group: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    organizational_unit_distinguished_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    password: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        dns_ips: Union[List[str], core.ArrayOut[core.StringOut]],
        domain_name: Union[str, core.StringOut],
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
        file_system_administrators_group: Optional[Union[str, core.StringOut]] = None,
        organizational_unit_distinguished_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SelfManagedActiveDirectoryConfiguration.Args(
                dns_ips=dns_ips,
                domain_name=domain_name,
                password=password,
                username=username,
                file_system_administrators_group=file_system_administrators_group,
                organizational_unit_distinguished_name=organizational_unit_distinguished_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        domain_name: Union[str, core.StringOut] = core.arg()

        file_system_administrators_group: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        organizational_unit_distinguished_name: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        password: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class ActiveDirectoryConfiguration(core.Schema):

    netbios_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    self_managed_active_directory_configuration: Optional[
        SelfManagedActiveDirectoryConfiguration
    ] = core.attr(SelfManagedActiveDirectoryConfiguration, default=None)

    def __init__(
        self,
        *,
        netbios_name: Optional[Union[str, core.StringOut]] = None,
        self_managed_active_directory_configuration: Optional[
            SelfManagedActiveDirectoryConfiguration
        ] = None,
    ):
        super().__init__(
            args=ActiveDirectoryConfiguration.Args(
                netbios_name=netbios_name,
                self_managed_active_directory_configuration=self_managed_active_directory_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        netbios_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        self_managed_active_directory_configuration: Optional[
            SelfManagedActiveDirectoryConfiguration
        ] = core.arg(default=None)


@core.schema
class Nfs(core.Schema):

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dns_name: Union[str, core.StringOut],
        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Nfs.Args(
                dns_name=dns_name,
                ip_addresses=ip_addresses,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: Union[str, core.StringOut] = core.arg()

        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Smb(core.Schema):

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dns_name: Union[str, core.StringOut],
        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Smb.Args(
                dns_name=dns_name,
                ip_addresses=ip_addresses,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: Union[str, core.StringOut] = core.arg()

        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Iscsi(core.Schema):

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dns_name: Union[str, core.StringOut],
        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Iscsi.Args(
                dns_name=dns_name,
                ip_addresses=ip_addresses,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: Union[str, core.StringOut] = core.arg()

        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Management(core.Schema):

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dns_name: Union[str, core.StringOut],
        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Management.Args(
                dns_name=dns_name,
                ip_addresses=ip_addresses,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: Union[str, core.StringOut] = core.arg()

        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Endpoints(core.Schema):

    iscsi: Union[List[Iscsi], core.ArrayOut[Iscsi]] = core.attr(
        Iscsi, computed=True, kind=core.Kind.array
    )

    management: Union[List[Management], core.ArrayOut[Management]] = core.attr(
        Management, computed=True, kind=core.Kind.array
    )

    nfs: Union[List[Nfs], core.ArrayOut[Nfs]] = core.attr(Nfs, computed=True, kind=core.Kind.array)

    smb: Union[List[Smb], core.ArrayOut[Smb]] = core.attr(Smb, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        iscsi: Union[List[Iscsi], core.ArrayOut[Iscsi]],
        management: Union[List[Management], core.ArrayOut[Management]],
        nfs: Union[List[Nfs], core.ArrayOut[Nfs]],
        smb: Union[List[Smb], core.ArrayOut[Smb]],
    ):
        super().__init__(
            args=Endpoints.Args(
                iscsi=iscsi,
                management=management,
                nfs=nfs,
                smb=smb,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iscsi: Union[List[Iscsi], core.ArrayOut[Iscsi]] = core.arg()

        management: Union[List[Management], core.ArrayOut[Management]] = core.arg()

        nfs: Union[List[Nfs], core.ArrayOut[Nfs]] = core.arg()

        smb: Union[List[Smb], core.ArrayOut[Smb]] = core.arg()


@core.resource(type="aws_fsx_ontap_storage_virtual_machine", namespace="aws_fsx")
class OntapStorageVirtualMachine(core.Resource):

    active_directory_configuration: Optional[ActiveDirectoryConfiguration] = core.attr(
        ActiveDirectoryConfiguration, default=None
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoints: Union[List[Endpoints], core.ArrayOut[Endpoints]] = core.attr(
        Endpoints, computed=True, kind=core.Kind.array
    )

    file_system_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    root_volume_security_style: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    subtype: Union[str, core.StringOut] = core.attr(str, computed=True)

    svm_admin_password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    uuid: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        file_system_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        active_directory_configuration: Optional[ActiveDirectoryConfiguration] = None,
        root_volume_security_style: Optional[Union[str, core.StringOut]] = None,
        svm_admin_password: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=OntapStorageVirtualMachine.Args(
                file_system_id=file_system_id,
                name=name,
                active_directory_configuration=active_directory_configuration,
                root_volume_security_style=root_volume_security_style,
                svm_admin_password=svm_admin_password,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        active_directory_configuration: Optional[ActiveDirectoryConfiguration] = core.arg(
            default=None
        )

        file_system_id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        root_volume_security_style: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        svm_admin_password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
