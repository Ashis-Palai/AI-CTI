from fastapi import FastAPI
from app.routes.upload import router as upload_router
# Update main.py to include:
from app.routes.extract import router as extract_router



app = FastAPI(
    title="ThreatVerse Lite - Ingestion API",
    description="Upload or link to sandbox reports (PDF/HTML) for processing",
    version="0.1"
)

app.include_router(upload_router, prefix="/upload")
app.include_router(extract_router, prefix="/extract")