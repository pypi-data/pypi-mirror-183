from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass
class GetBatchCrmEventAttendeeQueryParams:
    access_token: str = field(metadata={'query_param': { 'field_name': 'accessToken', 'style': 'form', 'explode': True }})
    all_fields: Optional[bool] = field(default=None, metadata={'query_param': { 'field_name': 'allFields', 'style': 'form', 'explode': True }})
    ids: Optional[str] = field(default=None, metadata={'query_param': { 'field_name': 'ids', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclass
class GetBatchCrmEventAttendeeResponseBody:
    event_attendees: Optional[list[shared.EventAttendee]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('eventAttendees') }})
    invalid_ids: Optional[list[str]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invalidIds') }})
    

@dataclass
class GetBatchCrmEventAttendeeRequest:
    query_params: GetBatchCrmEventAttendeeQueryParams = field()
    

@dataclass
class GetBatchCrmEventAttendeeResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[GetBatchCrmEventAttendeeResponseBody] = field(default=None)
    
