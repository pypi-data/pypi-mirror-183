from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass
class GetDetailsCrmEventQueryParams:
    access_token: str = field(metadata={'query_param': { 'field_name': 'accessToken', 'style': 'form', 'explode': True }})
    all_fields: Optional[bool] = field(default=None, metadata={'query_param': { 'field_name': 'allFields', 'style': 'form', 'explode': True }})
    cursor: Optional[str] = field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclass
class GetDetailsCrmEventResponseBody:
    fields: Optional[list[shared.Field]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fields') }})
    next_page_cursor: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nextPageCursor') }})
    

@dataclass
class GetDetailsCrmEventRequest:
    query_params: GetDetailsCrmEventQueryParams = field()
    

@dataclass
class GetDetailsCrmEventResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[GetDetailsCrmEventResponseBody] = field(default=None)
    
