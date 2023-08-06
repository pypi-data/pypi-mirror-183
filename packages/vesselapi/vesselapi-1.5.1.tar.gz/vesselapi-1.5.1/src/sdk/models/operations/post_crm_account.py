from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class PostCrmAccountRequestBody:
    access_token: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    account: shared.AccountCreate = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('account') }})
    

@dataclass_json
@dataclass
class PostCrmAccountResponseBody:
    id: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass
class PostCrmAccountRequest:
    request: Optional[PostCrmAccountRequestBody] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class PostCrmAccountResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PostCrmAccountResponseBody] = field(default=None)
    
