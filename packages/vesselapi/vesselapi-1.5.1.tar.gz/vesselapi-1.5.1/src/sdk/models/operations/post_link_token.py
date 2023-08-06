from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass
class PostLinkTokenSecurity:
    vessel_api_token: shared.SchemeVesselAPIToken = field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclass_json
@dataclass
class PostLinkTokenResponseBody:
    link_token: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('linkToken') }})
    

@dataclass
class PostLinkTokenRequest:
    security: PostLinkTokenSecurity = field()
    

@dataclass
class PostLinkTokenResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PostLinkTokenResponseBody] = field(default=None)
    
