from fastapi import FastAPI
from app.schemas.patient import Patient

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
def tambah_pasien(patient: Patient):

    return patient