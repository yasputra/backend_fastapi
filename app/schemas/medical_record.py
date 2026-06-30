from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MedicalRecordCreate(BaseModel):
    patient_id: str
    doctor_name: str
    visit_date: datetime

    subjective: str
    objective: str
    assessment: str
    plan: str


class MedicalRecordUpdate(BaseModel):
    doctor_name: Optional[str] = None
    visit_date: Optional[datetime] = None

    subjective: Optional[str] = None
    objective: Optional[str] = None
    assessment: Optional[str] = None
    plan: Optional[str] = None


class MedicalRecordResponse(BaseModel):
    id: str
    patient_id: str
    doctor_name: str
    visit_date: datetime

    subjective: str
    objective: str
    assessment: str
    plan: str

    created_at: datetime
    updated_at: datetime