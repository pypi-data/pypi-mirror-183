from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class GetAllCrmIntegrationsResponseBody:
    integrations: Optional[list[shared.CrmIntegration]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrations') }})
    

@dataclass
class GetAllCrmIntegrationsResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[GetAllCrmIntegrationsResponseBody] = field(default=None)
    
