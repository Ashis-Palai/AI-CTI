from fastapi import APIRouter
from app.utils.model_runner import extract_cti_entities
import os
import json
from bs4 import BeautifulSoup

router = APIRouter()

@router.get("/")
def run_extraction(filename: str):
    file_path = os.path.join("uploads", filename)
    if not os.path.exists(file_path):
        return {"error": f"File {filename} not found in uploads/"}

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    clean_text = soup.get_text(separator="\n")  # readable text

    # For prototype, pass full HTML. Later we’ll chunk intelligently.
    result,model_name = extract_cti_entities(clean_text)

    # Save output to file
    output_path = os.path.join("outputs", model_name,filename.replace(".html", ".json"))
    os.makedirs("outputs", exist_ok=True)
    with open(output_path, "w") as out:
        json.dump(result, out, indent=2)

    return {"status": "extracted", "output": result}
