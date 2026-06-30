from app.core.firebase import db

def create_patient(data: dict):

    db.collection("patients").add(data)

    return {
        "message": "Pasien berhasil ditambahkan"
    }