from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class EmailAssociations:
    account_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountIds') }})
    contact_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('contactIds') }})
    deal_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dealIds') }})
    lead_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('leadIds') }})
    owner_user_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('ownerUserId') }})
    

@dataclass_json
@dataclass
class Email:
    r"""Email
    An email is a message sent from one person to another through an email service. Emails involve participants - the person who the email was sent to, or the person that sent it. Participants are usually a Contact, Lead, or User but in certain CRMs, can be a person not yet associated with a CRM object.
    """
    
    associations: EmailAssociations = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('associations') }})
    created_time: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    from_: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('from') }})
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    modified_time: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    native_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('nativeId') }})
    subject: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('subject') }})
    to: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('to') }})
    additional: Optional[dict[str, Any]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additional') }})
    bcc: Optional[list[str]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bcc') }})
    body: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('body') }})
    body_html: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bodyHtml') }})
    cc: Optional[list[str]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('cc') }})
    has_attachment: Optional[bool] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hasAttachment') }})
    is_bounced: Optional[bool] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isBounced') }})
    is_incoming: Optional[bool] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isIncoming') }})
    message_date: Optional[datetime] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('messageDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    
