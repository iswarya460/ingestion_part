from pydantic import BaseModel
from typing import List, Union
from schema import RegulationProperties,ControlObjectiveProperties,RuleProperties,SystemProperties,JobProperties,PipelineProperties,LogsourceProperties,DatasetProperties,TableProperties,ColumnProperties,DataSourceProperties,TransformationProperties,CodeEventProperties,ScriptProperties
  

class Regulation(BaseModel):
    label_name: str = "Regulation"
    properties: RegulationProperties


class ControlObjective(BaseModel):
    label_name: str = "ControlObjective"
    properties: ControlObjectiveProperties


class Rule(BaseModel):
    label_name: str = "Rule"
    properties: RuleProperties

class System(BaseModel):
    label_name: str = "System"
    properties: SystemProperties

class Job(BaseModel):
    label_name: str = "Job"
    properties: JobProperties

class Pipeline(BaseModel):
    label_name: str = "Pipeline"
    properties: PipelineProperties

class Logsource(BaseModel):
    label_name: str = "Logsource"
    properties: LogsourceProperties    

class  Dataset(BaseModel):
    label_name: str = "Dataset"
    properties: DatasetProperties

class Table(BaseModel):
    label_name: str = "Table"
    properties: TableProperties 

class Column(BaseModel):
    label_name: str = "Column"
    properties: ColumnProperties        


class DataSource(BaseModel):
    label_name: str = "DataSource"
    properties: DataSourceProperties

class Transformation(BaseModel):
    label_name: str = "Transformation"
    properties: TransformationProperties

class CodeEvent(BaseModel):
    label_name: str = "CodeEvent"
    properties: CodeEventProperties    

class Script(BaseModel):    
    label_name: str = "Script"
    properties: ScriptProperties


regulation_EntityType = Union[Regulation, ControlObjective, Rule]
operational_EntityType = Union[System, Job, Pipeline, Logsource]
DataSet_EntityType = Union[Dataset, Table, Column]
Datasource_EntityType = Union[DataSource]
engineering_EntityType = Union[Script,Transformation,CodeEvent]


class RegualtionIngestionSchema(BaseModel):
    ingestion_type: str="governance"
    entities: List[regulation_EntityType]

class OperationalIngestionSchema(BaseModel):
    ingestion_type: str="operational"
    entities: List[operational_EntityType]

class  DatasetIngestionSchema(BaseModel):
    ingestion_type: str="dataset"
    entities: List[DataSet_EntityType]

class DatasourceIngestionSchema(BaseModel):
    ingestion_type: str="datasource"
    entities: List[Datasource_EntityType]

class EngineeringIngestionSchema(BaseModel):
    ingestion_type: str="engineering"
    entities: List[engineering_EntityType]