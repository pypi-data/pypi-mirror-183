from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class EmailCreateContact:
    r"""EmailCreateContact
    Associated Contacts must participate in the email (i.e., have a role).
    """
    
    id: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    role: Optional[Any] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('role') }})
    

@dataclass_json
@dataclass
class EmailCreateLead:
    r"""EmailCreateLead
    Associated Leads must participate in the email (i.e., have a role).
    """
    
    id: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    role: Optional[Any] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('role') }})
    

@dataclass_json
@dataclass
class EmailCreate:
    from_: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('from') }})
    subject: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('subject') }})
    to: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('to') }})
    account_id: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId') }})
    additional: Optional[dict[str, Any]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additional') }})
    bcc: Optional[list[str]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bcc') }})
    body: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('body') }})
    body_html: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bodyHtml') }})
    cc: Optional[list[str]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('cc') }})
    contact: Optional[EmailCreateContact] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contact') }})
    deal_id: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dealId') }})
    is_incoming: Optional[bool] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isIncoming') }})
    lead: Optional[EmailCreateLead] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lead') }})
    message_date: Optional[datetime] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('messageDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    owner_user_id: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ownerUserId') }})
    status: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    
