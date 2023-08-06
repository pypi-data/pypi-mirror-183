from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class DeleteConnectionRequestBody:
    access_token: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    

@dataclass
class DeleteConnectionSecurity:
    vessel_api_token: shared.SchemeVesselAPIToken = field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclass
class DeleteConnectionRequest:
    security: DeleteConnectionSecurity = field()
    request: Optional[DeleteConnectionRequestBody] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class DeleteConnectionResponse:
    content_type: str = field()
    status_code: int = field()
    
