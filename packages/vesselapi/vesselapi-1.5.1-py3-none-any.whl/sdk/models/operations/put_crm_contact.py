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
class PutCrmContactApplicationJSON:
    access_token: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    contact: shared.ContactUpdate = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('contact') }})
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass
class PutCrmContactRequests:
    application_xml: bytes = field(metadata={'request': { 'media_type': 'application/xml' }})
    object: Optional[PutCrmContactApplicationJSON] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclass
class PutCrmContactResponseBody:
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass
class PutCrmContactRequest:
    request: Optional[PutCrmContactRequests] = field(default=None)
    

@dataclass
class PutCrmContactResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PutCrmContactResponseBody] = field(default=None)
    
