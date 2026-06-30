from fastapi import FastAPI
from app.schemas.patient import Patient
from app.core.firebase import db
from app.services.patient_service import create_patient
from app.services.patient_service import get_all_patients
from app.services.patient_service import get_patient_by_id
from fastapi import HTTPException
from app.services.patient_service import update_patient
from app.services.patient_service import delete_patient
from app.schemas.patient import Patient

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Backend Rekam Medis"
    }

# crud pasien dulu 
# baca
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

# tambah
@app.post("/patients")
def add_patient(patient: Patient):

    return create_patient(patient.model_dump())

@app.get("/patients/{patient_id}")
def get_patient(patient_id: str):

    return get_patient_by_id(patient_id)

# edit
@app.put("/patients/{patient_id}")
def edit_patient(patient_id: str, patient: Patient):

    return update_patient(patient_id, patient.model_dump())

# hapus
@app.delete("/patients/{patient_id}")
def remove_patient(patient_id: str):
    return delete_patient(patient_id)

#firebase integrasi
@app.get("/test-firebase")
def test_firebase():
    return {
        "message": "Firebase Connected!"
    }