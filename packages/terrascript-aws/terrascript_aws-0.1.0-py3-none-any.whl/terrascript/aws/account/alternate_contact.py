from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_account_alternate_contact", namespace="aws_account")
class AlternateContact(core.Resource):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    alternate_contact_type: Union[str, core.StringOut] = core.attr(str)

    email_address: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    phone_number: Union[str, core.StringOut] = core.attr(str)

    title: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        alternate_contact_type: Union[str, core.StringOut],
        email_address: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        phone_number: Union[str, core.StringOut],
        title: Union[str, core.StringOut],
        account_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AlternateContact.Args(
                alternate_contact_type=alternate_contact_type,
                email_address=email_address,
                name=name,
                phone_number=phone_number,
                title=title,
                account_id=account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        alternate_contact_type: Union[str, core.StringOut] = core.arg()

        email_address: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        phone_number: Union[str, core.StringOut] = core.arg()

        title: Union[str, core.StringOut] = core.arg()
