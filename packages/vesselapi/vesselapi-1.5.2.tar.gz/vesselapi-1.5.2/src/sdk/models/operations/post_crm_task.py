from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class PostCrmTaskRequestBody:
    access_token: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    task: Optional[shared.TaskCreate] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('task') }})
    

@dataclass_json
@dataclass
class PostCrmTaskResponseBody:
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass
class PostCrmTaskRequest:
    request: Optional[PostCrmTaskRequestBody] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class PostCrmTaskResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PostCrmTaskResponseBody] = field(default=None)
    
