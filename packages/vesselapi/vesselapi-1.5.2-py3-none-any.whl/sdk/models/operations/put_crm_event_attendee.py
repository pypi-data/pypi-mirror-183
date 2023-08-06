from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class PutCrmEventAttendeeResponseBody:
    access_token: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    event_attendee: Optional[shared.EventAttendeeUpdate] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('eventAttendee') }})
    

@dataclass
class PutCrmEventAttendeeResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PutCrmEventAttendeeResponseBody] = field(default=None)
    
