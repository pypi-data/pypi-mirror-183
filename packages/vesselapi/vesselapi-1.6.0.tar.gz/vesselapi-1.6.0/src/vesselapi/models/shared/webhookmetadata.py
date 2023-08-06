import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from dataclasses_json import dataclass_json
from vesselapi import utils


@dataclass_json
@dataclasses.dataclass
class WebhookMetadata:
    connection_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('connectionId') }})
    created_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    webhook_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('webhookId') }})
    webhook_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('webhookUrl') }})
    
