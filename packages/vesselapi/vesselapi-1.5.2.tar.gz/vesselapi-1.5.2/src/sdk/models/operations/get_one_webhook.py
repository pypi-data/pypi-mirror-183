from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass
class GetOneWebhookQueryParams:
    access_token: Optional[str] = field(default=None, metadata={'query_param': { 'field_name': 'accessToken', 'style': 'form', 'explode': True }})
    webhook_id: Optional[str] = field(default=None, metadata={'query_param': { 'field_name': 'webhookId', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclass
class GetOneWebhookResponseBody:
    webhook: Optional[shared.WebhookMetadata] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('webhook') }})
    

@dataclass
class GetOneWebhookRequest:
    query_params: GetOneWebhookQueryParams = field()
    

@dataclass
class GetOneWebhookResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[GetOneWebhookResponseBody] = field(default=None)
    
