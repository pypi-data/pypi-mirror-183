from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class PutCrmTaskRequestBody:
    access_token: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    task: Optional[shared.TaskUpdate] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('task') }})
    

@dataclass_json
@dataclass
class PutCrmTaskResponseBody:
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass
class PutCrmTaskRequest:
    request: Optional[PutCrmTaskRequestBody] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class PutCrmTaskResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PutCrmTaskResponseBody] = field(default=None)
    
