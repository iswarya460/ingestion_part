from numpy import integer
from pydantic import BaseModel
from datetime import date, datetime 

class RegulationProperties(BaseModel):
    regulation_id: str
    name: str
    jurisdiction: str
    effective_date: str
    status: str


class ControlObjectiveProperties(BaseModel):
    control_id: str
    name: str
    description: str
    severity: str
    recommendation: str
    recommendation_type: str


class RuleProperties(BaseModel):
    rule_id: str
    name: str
    rule_type: str
    threshold: str
    is_blocking: bool
    created_at: str

class SystemProperties(BaseModel):
    system_id: str
    name: str
    type:str
    environment:str
    owner_team:str

class JobProperties(BaseModel):
    job_id: str
    name: str
    status:str
    trigger_type:str
    owner_team:str    
    start_time:datetime


class PipelineProperties(BaseModel):
    pipeline_id: str
    name: str
    type:str
    schedule:str
    owner_team: str
    status:str
    created_at:datetime

class LogsourceProperties(BaseModel):
    log_id: str
    name: str
    platform:str
    path:str
    log_type: str
    retention_days:int
    owner_team:str
    created_at:datetime

class DatasetProperties(BaseModel):
    dataset_id: str
    name: str
    domain:str
    storage_type:str
    description:str
    status:str

class TableProperties(BaseModel):
    table_id: str
    name: str
    schema:str
    storage_type:str
    refresh_type:str
    row_count:int
    status:str
    owner_team:str
    created_at:datetime
  

class ColumnProperties(BaseModel):
    column_id: str
    name: str
    data_type: str
    nullable: bool
    is_primary_key: bool
    ordinal_position: int
    status: str
    created_at: datetime

class DataSourceProperties(BaseModel):
    source_id: str
    name: str
    type:str
    environment:str
    owner_team:str
    status:str
    created_at:datetime

class ScriptProperties(BaseModel):
    script_id: str
    name: str
    language:str
    version:str
    repository:str
    checksum:str
    created_at:datetime

class TransformationProperties(BaseModel):
    transformation_id: str
    type:str
    description:str
    sequence_order:int
    created_at:datetime

class CodeEventProperties(BaseModel):
    event_id: str
    repo_platform: str
    repo_name:str
    branch:str
    author:str
    timestamp:datetime
    message:str
    external_url:str
