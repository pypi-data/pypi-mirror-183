import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from dataclasses_json import dataclass_json
from vesselapi import utils


@dataclass_json
@dataclasses.dataclass
class DealAssociations:
    account_ids: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountIds') }})
    contact_ids: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('contactIds') }})
    note_ids: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('noteIds') }})
    owner_user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('ownerUserId') }})
    task_ids: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('taskIds') }})
    event_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('eventIds') }})
    

@dataclass_json
@dataclasses.dataclass
class Deal:
    r"""Deal
    (Alias: Opportunity) An object representing either the opportunity to sell a product to an Account, or in the case of an `isWon` deal, a product sold to an Account.
    *CRM Caveats*:
    - Pipedrive: Users must have \"Deal probability\" turned on for the given pipeline for probability to be configurable and returned.
    """
    
    associations: DealAssociations = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('associations') }})
    close_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('closeDate'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    created_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    modified_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    native_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('nativeId') }})
    additional: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additional') }})
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount') }})
    expected_revenue: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('expectedRevenue') }})
    is_closed: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isClosed') }})
    is_won: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isWon') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    probability: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('probability') }})
    stage: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('stage') }})
    
