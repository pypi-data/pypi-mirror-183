from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class PostCrmEventAttendeeResponseBody:
    access_token: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    event_attendee: Optional[shared.EventAttendeeCreate] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('eventAttendee') }})
    

@dataclass
class PostCrmEventAttendeeResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PostCrmEventAttendeeResponseBody] = field(default=None)
    
