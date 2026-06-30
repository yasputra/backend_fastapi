from app.core.firebase import db
from fastapi import HTTPException

# menampilkan data seluruh pasien
def get_all_patients():

    patients = []

    docs = db.collection("patients").stream()

    for doc in docs:

        patient = doc.to_dict()

        patient["id"] = doc.id

        patients.append(patient)

    return patients

# menambahkan data pasein
def create_patient(data: dict):

    db.collection("patients").add(data)

    return {
        "message": "Pasien berhasil ditambahkan"
    }


# baca data pasein
def get_patient_by_id(patient_id: str):

    doc = db.collection("patients").document(patient_id).get()

    if not doc.exists:
        return {
            "message": "Pasien tidak ditemukan"
        }

    patient = doc.to_dict()

    patient["id"] = doc.id

    return patient

# edit data pasien
def update_patient(patient_id: str, data: dict):

    doc_ref = db.collection("patients").document(patient_id)

    doc = doc_ref.get()

    if not doc.exists:
        raise HTTPException(
            status_code=404,
            detail="Pasien tidak ditemukan"
        )

    doc_ref.update(data)

    updated_doc = doc_ref.get().to_dict()
    updated_doc["id"] = patient_id

    return updated_doc

# hapus
def delete_patient(patient_id: str):
    doc_ref = db.collection("patients").document(patient_id)
    doc = doc_ref.get()

    if not doc.exists:
        raise HTTPException(
            status_code=404,
            detail="Pasien tidak ditemukan"
        )

    doc_ref.delete()

    return {
        "message": "Data pasien berhasil dihapus"
    }