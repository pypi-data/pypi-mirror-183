from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class PostCrmLeadRequestBody:
    access_token: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    lead: shared.LeadCreate = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('lead') }})
    

@dataclass_json
@dataclass
class PostCrmLeadResponseBody:
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass
class PostCrmLeadRequest:
    request: Optional[PostCrmLeadRequestBody] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class PostCrmLeadResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PostCrmLeadResponseBody] = field(default=None)
    
