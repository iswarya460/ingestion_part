from fastapi import FastAPI, HTTPException
from pathlib import Path
import json
import uvicorn
from models import  RegualtionIngestionSchema, OperationalIngestionSchema, DatasetIngestionSchema, DatasourceIngestionSchema, EngineeringIngestionSchema

app = FastAPI(
    title="Kratos Schema Ingestion",
    description="API to ingest nodes schema",
    version="1.0",
    docs_url="/Kratos/ingestion/docs"
)

governance_file = Path(__file__).parent / "governance_schema.json"

operation_file=Path(__file__).parent / "operation_schema.json"

dataset_file=Path(__file__).parent / "dataset_schema.json"

datasource_file=Path(__file__).parent / "datasource_schema.json"

engineering_file=Path(__file__).parent / "engineering_schema.json"

@app.post("/kratos/governance_controls/schema/ingestion")
def ingest_schema(payload: RegualtionIngestionSchema):

    try:
        payload_dict = payload.model_dump()

        with open(governance_file, "w") as f:
            json.dump(payload_dict, f, indent=4)

        return {
            "message": "schema ingested successfully",
            "entity_count": len(payload_dict["entities"]),
            "ingestion_type": payload.ingestion_type
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/kratos/operational_controls/schema/ingestion")
def ingest_schema(payload: OperationalIngestionSchema):

    try:
        payload_dict = payload.model_dump(mode="json")

        with open(operation_file, "w") as f:
            json.dump(payload_dict, f, indent=4)

        return {
            "message": "schema ingested successfully",
            "entity_count": len(payload_dict["entities"]),
            "ingestion_type": payload.ingestion_type
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/kratos/data_controls/schema/ingestion")
def ingest_schema(payload: DatasetIngestionSchema):

    try:
        payload_dict = payload.model_dump(mode="json")

        with open(dataset_file, "w") as f:
            json.dump(payload_dict, f, indent=4)

        return {
            "message": "schema ingested successfully",
            "entity_count": len(payload_dict["entities"]),
            "ingestion_type": payload.ingestion_type
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/kratos/source_controls/schema/ingestion")
def ingest_schema(payload: DatasourceIngestionSchema):

    try:
        payload_dict = payload.model_dump(mode="json")

        with open(datasource_file, "w") as f:
            json.dump(payload_dict, f, indent=4)

        return {
            "message": "schema ingested successfully",
            "entity_count": len(payload_dict["entities"]),
            "ingestion_type": payload.ingestion_type
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/kratos/engineering_controls/schema/ingestion")
def ingest_schema(payload: EngineeringIngestionSchema):

    try:
        payload_dict = payload.model_dump(mode="json")

        with open(engineering_file, "w") as f:
            json.dump(payload_dict, f, indent=4)

        return {
            "message": "schema ingested successfully",
            "entity_count": len(payload_dict["entities"]),
            "ingestion_type": payload.ingestion_type
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)