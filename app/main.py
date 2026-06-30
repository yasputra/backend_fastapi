from fastapi import FastAPI
from app.schemas.patient import Patient
from app.core.firebase import db
from app.services.patient_service import create_patient
from app.services.patient_service import get_all_patients
from app.services.patient_service import get_patient_by_id
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Backend Rekam Medis"
    }

# crud pasien dulu 
@app.get("/patients")
def get_patients():

    return get_all_patients()

@app.get("/patients/{patient_id}")

def get_patient_by_id(patient_id: str):

    doc = db.collection("patients").document(patient_id).get()

    if not doc.exists:
        raise HTTPException(
            status_code=404,
            detail="Pasien tidak ditemukan"
        )

    patient = doc.to_dict()
    patient["id"] = doc.id

    return patient

@app.post("/patients")
def add_patient(patient: Patient):

    return create_patient(patient.model_dump())

@app.get("/patients/{patient_id}")
def get_patient(patient_id: str):

    return get_patient_by_id(patient_id)

#firebase integrasi
@app.get("/test-firebase")
def test_firebase():
    return {
        "message": "Firebase Connected!"
    }