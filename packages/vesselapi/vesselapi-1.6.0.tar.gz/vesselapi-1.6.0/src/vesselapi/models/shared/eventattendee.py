import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from dataclasses_json import dataclass_json
from vesselapi import utils


@dataclass_json
@dataclasses.dataclass
class EventAttendeeAssociations:
    association_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('associationId') }})
    event_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('eventId') }})
    

@dataclass_json
@dataclasses.dataclass
class EventAttendee:
    r"""EventAttendee
    Event Attendees hold information about someone who attendeed or was invited to an event. Attendees are always associated with some Event and another person object such as a Contact, Lead, or Other.
    """
    
    associated_object_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('associatedObjectType') }})
    associations: EventAttendeeAssociations = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('associations') }})
    created_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    modified_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    native_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('nativeId') }})
    additional: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additional') }})
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('email') }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    
