from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass
class GetOneCrmEventAttendeeQueryParams:
    access_token: str = field(metadata={'query_param': { 'field_name': 'accessToken', 'style': 'form', 'explode': True }})
    id: str = field(metadata={'query_param': { 'field_name': 'id', 'style': 'form', 'explode': True }})
    all_fields: Optional[bool] = field(default=None, metadata={'query_param': { 'field_name': 'allFields', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclass
class GetOneCrmEventAttendeeResponseBody:
    event_attendee: Optional[shared.EventAttendee] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('eventAttendee') }})
    

@dataclass
class GetOneCrmEventAttendeeRequest:
    query_params: GetOneCrmEventAttendeeQueryParams = field()
    

@dataclass
class GetOneCrmEventAttendeeResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[GetOneCrmEventAttendeeResponseBody] = field(default=None)
    
