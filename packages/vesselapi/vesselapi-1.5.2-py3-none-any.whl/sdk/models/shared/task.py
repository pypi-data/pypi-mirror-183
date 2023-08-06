from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class TaskAssociations:
    account_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountIds') }})
    contact_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('contactIds') }})
    deal_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dealIds') }})
    lead_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('leadIds') }})
    owner_user_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('ownerUserId') }})
    

@dataclass_json
@dataclass
class Task:
    r"""Task
    A task attached to some CRM object
    """
    
    associations: TaskAssociations = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('associations') }})
    created_time: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    modified_time: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    native_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('nativeId') }})
    additional: Optional[dict[str, Any]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additional') }})
    body: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('body') }})
    due_date: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dueDate') }})
    is_done: Optional[bool] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDone') }})
    priority: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('priority') }})
    status: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    subject: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subject') }})
    
