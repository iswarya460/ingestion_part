from pydantic import BaseModel
from typing import List, Union
from relationships import Properties_info
from models import Regulation, ControlObjective, Rule, Owner, Violation, Incident, Escalation, Remediation,System, Job, Pipeline, Logsource, Dataset, Table, Column, DataSource, Transformation, CodeEvent, Script

class Contains(BaseModel):
    label_name: str = "CONTAINS"
    properties: Properties_info

class HasColumn(BaseModel):
    label_name: str = "HAS_COLUMN"
    properties: Properties_info

class DerivedFrom(BaseModel):
    label_name: str = "DERIVED_FROM"
    properties: Properties_info        

class Mandates(BaseModel):
    label_name: str = "MANDATES"
    properties: Properties_info

class ImplementedBy(BaseModel):
    label_name: str = "IMPLEMENTED_BY"
    properties: Properties_info       

class EnforcedBy(BaseModel):  
    label_name: str = "ENFORCED_BY"
    properties: Properties_info

class Generates(BaseModel):
    label_name: str = "GENERATES"
    properties: Properties_info

class OwnsPipeline(BaseModel):
    label_name: str = "OWNS_PIPELINE"
    properties: Properties_info

class OwnsJob(BaseModel):
    label_name: str = "OWNS_JOB"
    properties: Properties_info

class OwnsSystem(BaseModel):    
    label_name: str = "OWNS_SYSTEM"
    properties: Properties_info

class OwnsControl(BaseModel):
    label_name: str = "OWNS_CONTROL"
    properties: Properties_info

class Creates(BaseModel):  
    label_name: str = "CREATES"
    properties: Properties_info

class Triggers(BaseModel):
    label_name: str = "RESOLVED_BY"
    properties: Properties_info

class AssignedTo(BaseModel):
    label_name: str = "ASSIGNED_TO"
    properties: Properties_info

class  ResolvedBy(BaseModel):
    label_name: str = "RESOLVED_BY"
    properties: Properties_info 

class RunsJob(BaseModel):
    label_name: str = "RUNS_JOB"
    properties: Properties_info

class LoggedIn(BaseModel):
    label_name: str = "LOGGED_IN"
    properties: Properties_info

class DependsOn(BaseModel):
    label_name: str = "DEPENDS_ON"
    properties: Properties_info

class Executes(BaseModel):
    label_name: str = "EXECUTES"
    properties: Properties_info

class UsesScript(BaseModel):  
    label_name: str = "USES_SCRIPT"
    properties: Properties_info

class HasTransformation(BaseModel):
    label_name: str = "HAS_TRANSFORMATION"
    properties: Properties_info

class OwnsPipeline(BaseModel):
    label_name: str = "OWNS_PIPELINE"
    properties: Properties_info        

class Reads(BaseModel):
    label_name: str = "READS"
    properties: Properties_info

class Writes(BaseModel):
    label_name: str = "WRITES"
    properties: Properties_info

class SourcedFrom(BaseModel):
    label_name: str = "SOURCED_FROM"
    properties: Properties_info    

class TypicallyImplements(BaseModel):   
    label_name: str = "TYPICALLY_IMPLEMENTS"
    properties: Properties_info

class ChangedBy(BaseModel):
    label_name: str = "CHANGED_BY"
    properties: Properties_info    

regulation_EntityType = Union[Regulation, ControlObjective, Rule, Owner, Violation, Incident, Escalation, Remediation,Transformation,Violation,Pipeline,Job,System,Logsource]
operational_EntityType = Union[System, Job, Pipeline, Logsource,Owner,Script,Transformation]
DataSet_EntityType = Union[Dataset, Table, Column,Script,Dataset]
Datasource_EntityType = Union[DataSource,Table]
engineering_EntityType = Union[Script,Transformation,CodeEvent,Table,Rule]

#relationship types for dataset ingestion
Regulation_RelationshipType = Union[Mandates, ImplementedBy, EnforcedBy,Generates,OwnsPipeline, OwnsJob, OwnsSystem, OwnsControl,AssignedTo,Creates,ResolvedBy,Triggers]
operational_RelationshipType = Union[RunsJob,LoggedIn,OwnsSystem,RunsJob,DependsOn,Executes,OwnsJob,UsesScript,HasTransformation,OwnsPipeline,]
Dataset_RelationshipType = Union[Contains, HasColumn, DerivedFrom,Reads,Writes,SourcedFrom]
DataSource_RelationshipType = Union[SourcedFrom ]
Engineering_RelationshipType=Union[UsesScript,TypicallyImplements,Reads,Writes,ChangedBy,HasTransformation,EnforcedBy]


class RegualtionIngestionSchema(BaseModel):
    ingestion_type: str="governance"
    entities: List[regulation_EntityType]
    relationships:List[Regulation_RelationshipType]

class OperationalIngestionSchema(BaseModel):
    ingestion_type: str="operational"
    entities: List[operational_EntityType]
    relationships:List[operational_RelationshipType]

class  DatasetIngestionSchema(BaseModel):
    ingestion_type: str="dataset"
    entities: List[DataSet_EntityType]
    relationships:List[Dataset_RelationshipType]

class DatasourceIngestionSchema(BaseModel):
    ingestion_type: str="datasource"
    entities: List[Datasource_EntityType]
    relationships:List[DataSource_RelationshipType]

class EngineeringIngestionSchema(BaseModel):
    ingestion_type: str="engineering"
    entities: List[engineering_EntityType]
    relationships:List[Engineering_RelationshipType]
