from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass
class GetOneCrmContactQueryParams:
    access_token: str = field(metadata={'query_param': { 'field_name': 'accessToken', 'style': 'form', 'explode': True }})
    all_fields: Optional[bool] = field(default=None, metadata={'query_param': { 'field_name': 'allFields', 'style': 'form', 'explode': True }})
    email: Optional[str] = field(default=None, metadata={'query_param': { 'field_name': 'email', 'style': 'form', 'explode': True }})
    id: Optional[str] = field(default=None, metadata={'query_param': { 'field_name': 'id', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclass
class GetOneCrmContactResponseBody:
    contact: Optional[shared.Contact] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contact') }})
    

@dataclass
class GetOneCrmContactRequest:
    query_params: GetOneCrmContactQueryParams = field()
    

@dataclass
class GetOneCrmContactResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[GetOneCrmContactResponseBody] = field(default=None)
    
