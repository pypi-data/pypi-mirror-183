from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class PostCrmDealRequestBody:
    access_token: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    deal: shared.DealCreate = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('deal') }})
    

@dataclass_json
@dataclass
class PostCrmDealResponseBody:
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass
class PostCrmDealRequest:
    request: Optional[PostCrmDealRequestBody] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class PostCrmDealResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PostCrmDealResponseBody] = field(default=None)
    
