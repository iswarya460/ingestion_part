from fastapi import FastAPI, HTTPException, logger
import uvicorn
import logging
from relationship_models import RegualtionIngestionSchema, OperationalIngestionSchema, DatasetIngestionSchema, DatasourceIngestionSchema, EngineeringIngestionSchema

logger = logging.getLogger("uvicorn")

app = FastAPI(
    title="Kratos Schema Ingestion",
    description="API to ingest nodes schema",
    version="1.0",
    docs_url="/Kratos/ingestion/docs",
    openapi_url="/Kratos/openapi.json"
)


@app.post("/kratos/governance_controls/schema/ingestion")
def ingest_schema(payload: RegualtionIngestionSchema):

    try:
        payload_dict = payload.model_dump()


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

        return {
            "message": "schema ingested successfully",
            "entity_count": len(payload_dict["entities"]),
            "ingestion_type": payload.ingestion_type
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 


@app.on_event("startup")
def show_docs_url():
    logger.info("API is starting up...")
    logger.info("Swagger Docs available at: http://127.0.0.1:8002/Kratos/ingestion/docs")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)
