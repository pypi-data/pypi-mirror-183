from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class PostWebhookRequestBody:
    access_token: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accessToken') }})
    webhook: Optional[shared.WebhookMetadataCreate] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('webhook') }})
    

@dataclass_json
@dataclass
class PostWebhookResponseBody:
    webhook: Optional[shared.WebhookMetadata] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('webhook') }})
    

@dataclass
class PostWebhookRequest:
    request: Optional[PostWebhookRequestBody] = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class PostWebhookResponse:
    content_type: str = field()
    status_code: int = field()
    response_body: Optional[PostWebhookResponseBody] = field(default=None)
    
