from dataclasses import dataclass, field
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from sdk import utils

class CrmIntegrationIntegrationIDEnum(str, Enum):
    SALESFORCE = "salesforce"
    HUBSPOT = "hubspot"
    PIPEDRIVE = "pipedrive"


@dataclass_json
@dataclass
class CrmIntegration:
    icon_url: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('iconURL') }})
    integration_id: Optional[CrmIntegrationIntegrationIDEnum] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationId') }})
    name: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    
