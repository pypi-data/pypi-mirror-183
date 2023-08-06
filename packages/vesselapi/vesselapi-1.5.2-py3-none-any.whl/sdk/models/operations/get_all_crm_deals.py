from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass
class GetAllCrmDealsQueryParams:
    access_token: str = field(metadata={'query_param': { 'field_name': 'accessToken', 'style': 'form', 'explode': True }})
    all_fields: Optional[bool] = field(default=None, metadata={'query_param': { 'field_name': 'allFields', 'style': 'form', 'explode': True }})
    cursor: Optional[str] = field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    limit: Optional[float] = field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclass
class GetAllCrmDealsResponseBody:
    deals: Optional[list[shared.Deal]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deals') }})
    next_page_cursor: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nextPageCursor') }})
    

@dataclass
class GetAllCrmDealsRequest:
    query_params: GetAllCrmDealsQueryParams = field()
    

@dataclass
class GetAllCrmDealsResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[GetAllCrmDealsResponseBody] = field(default=None)
    
