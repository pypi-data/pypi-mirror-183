from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class UserAssociations:
    deal_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dealIds') }})
    event_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('eventIds') }})
    note_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('noteIds') }})
    task_ids: list[str] = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('taskIds') }})
    

@dataclass_json
@dataclass
class User:
    r"""User
    Users of the connected CRM platform. These are *not* the contacts or leads, but rather the user accounts from the connected CRM.
    """
    
    associations: UserAssociations = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('associations') }})
    created_time: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    modified_time: datetime = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    native_id: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('nativeId') }})
    additional: Optional[dict[str, Any]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additional') }})
    email: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('email') }})
    first_name: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('firstName') }})
    last_name: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lastName') }})
    
