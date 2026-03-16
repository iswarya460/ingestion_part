from pydantic import BaseModel,Field
from schema import RegulationProperties,ControlObjectiveProperties,RuleProperties,OwnerProperties,IncidentProperties,ViolationProperties,EscalationProperties,RemediationProperties,SystemProperties,JobProperties,PipelineProperties,LogsourceProperties,DatasetProperties,TableProperties,ColumnProperties,DataSourceProperties,TransformationProperties,CodeEventProperties,ScriptProperties,Relationship

class Regulation(BaseModel):
    label_name: str = "Regulation"
    properties: RegulationProperties


class ControlObjective(BaseModel):
    label_name: str = "ControlObjective"
    properties: ControlObjectiveProperties


class Rule(BaseModel):
    label_name: str = "Rule"
    properties: RuleProperties

class Owner(BaseModel):
    label_name: str = "Owner"
    properties: OwnerProperties

class Violation(BaseModel):
    label_name: str = "Violation"
    properties: ViolationProperties

class Incident(BaseModel):
    label_name: str = "Incident"
    properties: IncidentProperties

class Escalation(BaseModel):
    label_name: str = "Escalation"
    properties: EscalationProperties

class Remediation(BaseModel):
    label_name: str = "Remediation"
    properties: RemediationProperties

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
