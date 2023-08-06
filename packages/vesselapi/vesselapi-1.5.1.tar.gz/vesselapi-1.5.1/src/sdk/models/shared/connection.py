from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from sdk import utils

class ConnectionIntegrationIDEnum(str, Enum):
    SALESFORCE = "salesforce"
    HUBSPOT = "hubspot"
    PIPEDRIVE = "pipedrive"

class ConnectionStatusEnum(str, Enum):
    NEW_CONNECTION = "NEW_CONNECTION"
    INITIAL_SYNC = "INITIAL_SYNC"
    READY = "READY"


@dataclass_json
@dataclass
class Connection:
    connection_id: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('connectionId') }})
    created_time: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdTime') }})
    integration_id: Optional[ConnectionIntegrationIDEnum] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationId') }})
    last_activity_date: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lastActivityDate') }})
    native_org_url: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nativeOrgURL') }})
    status: Optional[ConnectionStatusEnum] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    
