from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass
class GetOneCrmNoteQueryParams:
    access_token: str = field(metadata={'query_param': { 'field_name': 'accessToken', 'style': 'form', 'explode': True }})
    id: str = field(metadata={'query_param': { 'field_name': 'id', 'style': 'form', 'explode': True }})
    all_fields: Optional[bool] = field(default=None, metadata={'query_param': { 'field_name': 'allFields', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclass
class GetOneCrmNoteResponseBody:
    note: Optional[shared.Note] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('note') }})
    

@dataclass
class GetOneCrmNoteRequest:
    query_params: GetOneCrmNoteQueryParams = field()
    

@dataclass
class GetOneCrmNoteResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[GetOneCrmNoteResponseBody] = field(default=None)
    
