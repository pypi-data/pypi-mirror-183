from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class PostCrmEventRequestBody:
    access_token: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    event: Optional[shared.EventCreate] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('event') }})
    

@dataclass_json
@dataclass
class PostCrmEventResponseBody:
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass
class PostCrmEventRequest:
    request: Optional[PostCrmEventRequestBody] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class PostCrmEventResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PostCrmEventResponseBody] = field(default=None)
    
