from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class GetAllCrmConnectionsResponseBody:
    connections: Optional[list[shared.Connection]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('connections') }})
    

@dataclass
class GetAllCrmConnectionsResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[GetAllCrmConnectionsResponseBody] = field(default=None)
    
