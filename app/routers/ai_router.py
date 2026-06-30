from fastapi import APIRouter

from app.schemas.ai import SOAPRequest
from app.services.ai_service import generate_soap

router = APIRouter(
    prefix="/ai",
    tags=["Artificial Intelligence"]
)


@router.post("/generate-soap")
def generate(request: SOAPRequest):

    return generate_soap(request.transcript)