from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.schemas.ai import SOAPRequest
from app.services.ai_service import generate_soap, transcribe

router = APIRouter(
    prefix="/ai",
    tags=["Artificial Intelligence"]
)


@router.post("/generate-soap")
def generate(request: SOAPRequest):
    return generate_soap(request.transcript)


@router.post("/transcribe")
def transcribe_audio(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)

    filepath = os.path.join(
        "uploads",
        file.filename
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return transcribe(filepath)