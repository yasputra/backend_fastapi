from app.core.firebase import db
from fastapi import HTTPException
from datetime import datetime


# Menampilkan seluruh rekam medis
def get_all_medical_records():

    medical_records = []

    docs = db.collection("medical_records").stream()

    for doc in docs:

        medical_record = doc.to_dict()

        medical_record["id"] = doc.id

        medical_records.append(medical_record)

    return medical_records


# Menambahkan rekam medis
def create_medical_record(data: dict):

    # Validasi pasien
    patient = db.collection("patients").document(data["patient_id"]).get()

    if not patient.exists:
        raise HTTPException(
            status_code=404,
            detail="Pasien tidak ditemukan"
        )

    now = datetime.utcnow().isoformat()

    data["created_at"] = now
    data["updated_at"] = now

    doc_ref = db.collection("medical_records").document()

    doc_ref.set(data)

    return {
        "id": doc_ref.id,
        "message": "Rekam medis berhasil ditambahkan"
    }


# Detail rekam medis berdasarkan ID
def get_medical_record_by_id(record_id: str):

    doc = db.collection("medical_records").document(record_id).get()

    if not doc.exists:
        return {
            "message": "Rekam medis tidak ditemukan"
        }

    medical_record = doc.to_dict()

    medical_record["id"] = doc.id

    return medical_record


# Update rekam medis
def update_medical_record(record_id: str, data: dict):

    doc_ref = db.collection("medical_records").document(record_id)

    doc = doc_ref.get()

    if not doc.exists:
        raise HTTPException(
            status_code=404,
            detail="Rekam medis tidak ditemukan"
        )

    data["updated_at"] = datetime.utcnow().isoformat()
    doc_ref.update(data)

    updated_doc = doc_ref.get().to_dict()
    updated_doc["id"] = record_id

    return updated_doc


# Hapus rekam medis
def delete_medical_record(record_id: str):

    doc_ref = db.collection("medical_records").document(record_id)

    doc = doc_ref.get()

    if not doc.exists:
        raise HTTPException(
            status_code=404,
            detail="Rekam medis tidak ditemukan"
        )

    doc_ref.delete()

    return {
        "message": "Rekam medis berhasil dihapus"
    }


# Menampilkan riwayat rekam medis berdasarkan pasien
def get_medical_records_by_patient(patient_id: str):

    medical_records = []

    from firebase_admin import firestore

    docs = (
        db.collection("medical_records")
        .where("patient_id", "==", patient_id)
        .order_by(
            "created_at",
            direction=firestore.Query.DESCENDING
        )
        .stream()
    )

    for doc in docs:

        medical_record = doc.to_dict()

        medical_record["id"] = doc.id

        medical_records.append(medical_record)

    return medical_records