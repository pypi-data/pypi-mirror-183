from dataclasses import dataclass, field
from typing import Any,Optional
from dataclasses_json import dataclass_json
from sdk import utils
from .. import shared


@dataclass_json
@dataclass
class AccountCreate:
    name: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    additional: Optional[dict[str, Any]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additional') }})
    address: Optional[shared.Address] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('address') }})
    annual_revenue: Optional[float] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('annualRevenue') }})
    description: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    industry: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('industry') }})
    number_of_employees: Optional[float] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('numberOfEmployees') }})
    phone: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('phone') }})
    website: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('website') }})
    
