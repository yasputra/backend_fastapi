from app.core.firebase import db

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