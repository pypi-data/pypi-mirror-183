from dataclasses import dataclass, field
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class PostLinkExchangeRequestBody:
    public_token: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('publicToken') }})
    

@dataclass
class PostLinkExchangeSecurity:
    vessel_api_token: shared.SchemeVesselAPIToken = field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    
class PostLinkExchangeResponseBodyIntegrationIDEnum(str, Enum):
    SALESFORCE = "salesforce"
    HUBSPOT = "hubspot"
    PIPEDRIVE = "pipedrive"


@dataclass_json
@dataclass
class PostLinkExchangeResponseBody:
    access_token: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    connection_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('connectionId') }})
    integration_id: PostLinkExchangeResponseBodyIntegrationIDEnum = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationId') }})
    native_org_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('nativeOrgId') }})
    native_org_url: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('nativeOrgURL') }})
    

@dataclass
class PostLinkExchangeRequest:
    security: PostLinkExchangeSecurity = field()
    request: Optional[PostLinkExchangeRequestBody] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class PostLinkExchangeResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PostLinkExchangeResponseBody] = field(default=None)
    
