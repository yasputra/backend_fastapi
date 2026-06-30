from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class MedicalRecord(BaseModel):
    id: Optional[str] = None
    patient_id: str
    doctor_name: str
    visit_date: datetime

    subjective: str
    objective: str
    assessment: str
    plan: str

    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()