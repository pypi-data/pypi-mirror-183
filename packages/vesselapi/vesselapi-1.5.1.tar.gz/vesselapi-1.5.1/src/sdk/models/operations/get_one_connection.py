from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass
class GetOneConnectionQueryParams:
    access_token: str = field(metadata={'query_param': { 'field_name': 'accessToken', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclass
class GetOneConnectionResponseBody:
    connection: Optional[shared.Connection] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('connection') }})
    

@dataclass
class GetOneConnectionRequest:
    query_params: GetOneConnectionQueryParams = field()
    

@dataclass
class GetOneConnectionResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[GetOneConnectionResponseBody] = field(default=None)
    
