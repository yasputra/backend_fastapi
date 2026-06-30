from fastapi import FastAPI
from app.schemas.patient import Patient
from app.core.firebase import db
from app.services.patient_service import create_patient

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Backend Rekam Medis"
    }

# crud pasien dulu 
@app.get("/patients")
def get_patients():
    return {
        "patients": [
            {
                "id": 1,
                "nama": "Budi"
            },
            {
                "id": 2,
                "nama": "Siti"
            }
        ]
    }

@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    return {
        "id": patient_id,
        "message": "Data pasien ditemukan"
    }

@app.post("/patients")
def add_patient(patient: Patient):

    return create_patient(patient.model_dump())

#firebase integrasi
@app.get("/test-firebase")
def test_firebase():
    return {
        "message": "Firebase Connected!"
    }