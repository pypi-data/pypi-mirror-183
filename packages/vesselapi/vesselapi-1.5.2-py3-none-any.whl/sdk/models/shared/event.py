from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class EventAssociations:
    account_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountIds') }})
    contact_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('contactIds') }})
    deal_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dealIds') }})
    event_attendee_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('eventAttendeeIds') }})
    lead_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('leadIds') }})
    owner_user_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('ownerUserId') }})
    

@dataclass_json
@dataclass
class Event:
    r"""Event
    Events are a type of activity that has attendees and takes place at a certain point in time (i.e., has a start and end date).
    For the currently supported CRMs, these are the objects Events most closely maps to:
    - Salesforce = Events
    - HubSpot = Meetings
    - Pipedrive = Activities
    """
    
    associations: EventAssociations = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('associations') }})
    created_time: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    modified_time: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    native_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('nativeId') }})
    additional: Optional[dict[str, Any]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additional') }})
    description: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    end_date_time: Optional[datetime] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('endDateTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    is_all_day_event: Optional[bool] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isAllDayEvent') }})
    location: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('location') }})
    start_date_time: Optional[datetime] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('startDateTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    subject: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subject') }})
    type: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    
