from dataclasses import dataclass, field
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from enum import Enum
from dataclasses_json import dataclass_json
from sdk import utils


@dataclass_json
@dataclass
class FieldOptions:
    key: Optional[Any] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('key') }})
    name: Optional[str] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    
class FieldTypeEnum(str, Enum):
    STRING = "string"
    NUMBER = "number"
    DATETIME = "datetime"
    DATE = "date"
    BOOLEAN = "boolean"
    REFERENCE = "reference"
    PHONE = "phone"
    URL = "url"
    ID = "id"
    EMAIL = "email"
    PERCENT = "percent"
    SINGLESELECT = "singleselect"
    MULTISELECT = "multiselect"
    ADDRESS = "address"
    DECIMAL = "decimal"
    TIME = "time"
    DATERANGE = "daterange"
    OBJECT = "object"


@dataclass_json
@dataclass
class Field:
    r"""Field
    (Alias: property) A field is a key-value pair on a CRM Object that provides information about that object.
    """
    
    creatable: bool = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('creatable') }})
    custom: bool = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('custom') }})
    key: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('key') }})
    name: str = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    required: bool = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    type: FieldTypeEnum = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    universal: bool = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('universal') }})
    updatable: bool = field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('updatable') }})
    is_array: Optional[bool] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isArray') }})
    options: Optional[list[FieldOptions]] = field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options') }})
    
