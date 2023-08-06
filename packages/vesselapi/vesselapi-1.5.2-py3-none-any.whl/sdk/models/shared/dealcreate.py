from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class DealCreate:
    close_date: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('closeDate') }})
    name: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    account_id: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountId') }})
    additional: Optional[dict[str, Any]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additional') }})
    amount: Optional[float] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount') }})
    probability: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('probability') }})
    stage: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('stage') }})
    
