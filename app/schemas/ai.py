from pydantic import BaseModel


class SOAPRequest(BaseModel):
    transcript: str


class SOAPResponse(BaseModel):
    subjective: str
    objective: str
    assessment: str
    plan: str

class TranscriptResponse(BaseModel):
    transcript: str