from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass
class GetBatchCrmEmailQueryParams:
    access_token: str = field(metadata={'query_param': { 'field_name': 'accessToken', 'style': 'form', 'explode': True }})
    all_fields: Optional[bool] = field(default=None, metadata={'query_param': { 'field_name': 'allFields', 'style': 'form', 'explode': True }})
    ids: Optional[str] = field(default=None, metadata={'query_param': { 'field_name': 'ids', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclass
class GetBatchCrmEmailResponseBody:
    emails: Optional[list[shared.Email]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('emails') }})
    invalid_ids: Optional[list[str]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invalidIds') }})
    

@dataclass
class GetBatchCrmEmailRequest:
    query_params: GetBatchCrmEmailQueryParams = field()
    

@dataclass
class GetBatchCrmEmailResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[GetBatchCrmEmailResponseBody] = field(default=None)
    
