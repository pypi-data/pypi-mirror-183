from dataclasses import dataclass, field



@dataclass
class SchemeVesselAPIToken:
    api_key: str = field(metadata={'security': { 'field_name': 'vessel-api-token' }})
    

@dataclass
class Security:
    vessel_api_token: SchemeVesselAPIToken = field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    
