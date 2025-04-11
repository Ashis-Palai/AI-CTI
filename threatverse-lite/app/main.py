from fastapi import FastAPI
from app.routes.upload import router as upload_router

app = FastAPI(
    title="ThreatVerse Lite - Ingestion API",
    description="Upload or link to sandbox reports (PDF/HTML) for processing",
    version="0.1"
)

app.include_router(upload_router, prefix="/upload")