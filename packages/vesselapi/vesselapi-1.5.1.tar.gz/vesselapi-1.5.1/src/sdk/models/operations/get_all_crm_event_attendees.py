from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass
class GetAllCrmEventAttendeesQueryParams:
    access_token: Optional[str] = field(default=None, metadata={'query_param': { 'field_name': 'accessToken', 'style': 'form', 'explode': True }})
    all_fields: Optional[bool] = field(default=None, metadata={'query_param': { 'field_name': 'allFields', 'style': 'form', 'explode': True }})
    cursor: Optional[str] = field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    limit: Optional[float] = field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclass
class GetAllCrmEventAttendeesResponseBody:
    event_attendees: Optional[list[shared.EventAttendee]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('eventAttendees') }})
    next_page_cursor: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nextPageCursor') }})
    

@dataclass
class GetAllCrmEventAttendeesRequest:
    query_params: GetAllCrmEventAttendeesQueryParams = field()
    

@dataclass
class GetAllCrmEventAttendeesResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[GetAllCrmEventAttendeesResponseBody] = field(default=None)
    
