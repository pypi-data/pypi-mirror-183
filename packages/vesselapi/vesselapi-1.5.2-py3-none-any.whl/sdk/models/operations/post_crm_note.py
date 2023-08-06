from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class PostCrmNoteRequestBody:
    access_token: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    note: shared.NoteCreate = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('note') }})
    

@dataclass_json
@dataclass
class PostCrmNoteResponseBody:
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass
class PostCrmNoteRequest:
    request: Optional[PostCrmNoteRequestBody] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class PostCrmNoteResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PostCrmNoteResponseBody] = field(default=None)
    
