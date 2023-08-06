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
class PutCrmDealRequestBody:
    access_token: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    deal: shared.DealUpdate = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('deal') }})
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclass
class PutCrmDealResponseBody:
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass
class PutCrmDealRequest:
    request: Optional[PutCrmDealRequestBody] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class PutCrmDealResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PutCrmDealResponseBody] = field(default=None)
    
