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
class PutCrmLeadRequestBody:
    access_token: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    lead: Optional[shared.LeadUpdate] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lead') }})
    

@dataclass_json
@dataclass
class PutCrmLeadResponseBody:
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass
class PutCrmLeadRequest:
    request: Optional[PutCrmLeadRequestBody] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class PutCrmLeadResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PutCrmLeadResponseBody] = field(default=None)
    
