from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
import os
from app.utils.file_utils import save_upload_file, download_html_from_url

router = APIRouter()
UPLOAD_DIR = "uploads"

@router.post("/")
async def upload_or_link_file(
    file: Optional[UploadFile] = File(None),
    url: Optional[str] = Form(None)
):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    if file:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        await save_upload_file(file, file_path)
        return {"status": "uploaded", "filename": file.filename}

    elif url and url.endswith(".html"):
        filename = url.split("/")[-1]
        file_path = os.path.join(UPLOAD_DIR, filename)
        download_html_from_url(url, file_path)
        return {"status": "downloaded", "filename": filename, "source_url": url}

    else:
        return {"error": "Provide either a file or a valid .html URL"}