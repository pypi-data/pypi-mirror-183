from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class PostCrmContactRequestBody:
    access_token: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    contact: shared.ContactCreate = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('contact') }})
    

@dataclass_json
@dataclass
class PostCrmContactResponseBody:
    id: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass
class PostCrmContactRequest:
    request: Optional[PostCrmContactRequestBody] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class PostCrmContactResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PostCrmContactResponseBody] = field(default=None)
    
