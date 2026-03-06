# ingestion_part

### Ingestion Folder

The ingestion folder contains the ingestion scripts along with their corresponding schemas. These scripts are responsible for processing and loading the data required by the system.

The processed output data, which is later reflected in the UI, is stored in separate JSON files within this structure. Each JSON file corresponds to its relevant schema and represents the data consumed by the UI.

### schema.py

The schema.py file contains all the schema definitions related to the ontology. These schemas define the structure and validation rules for the data entities used across the system.

### main.py

The main.py file implements the UI connectivity using FastAPI. It exposes the required API endpoints and connects the UI with the backend schemas and data stored in the JSON files.
