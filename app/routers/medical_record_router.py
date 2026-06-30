from fastapi import APIRouter

from app.schemas.medical_record import (
    MedicalRecordCreate,
    MedicalRecordUpdate,
)

from app.services.medical_record_service import (
    get_all_medical_records,
    create_medical_record,
    get_medical_record_by_id,
    update_medical_record,
    delete_medical_record,
    get_medical_records_by_patient,
)

router = APIRouter(
    prefix="/medical-records",
    tags=["Medical Records"]
)


# Menampilkan seluruh rekam medis
@router.get("/")
def get_medical_records():
    return get_all_medical_records()


# Menambahkan rekam medis
@router.post("/")
def add_medical_record(record: MedicalRecordCreate):
    return create_medical_record(record.model_dump())

# Riwayat rekam medis berdasarkan pasien
@router.get("/patient/{patient_id}")
def get_patient_medical_records(patient_id: str):
    return get_medical_records_by_patient(patient_id)


# Detail rekam medis
@router.get("/{record_id}")
def get_medical_record(record_id: str):
    return get_medical_record_by_id(record_id)


# Update rekam medis
@router.put("/{record_id}")
def edit_medical_record(
    record_id: str,
    record: MedicalRecordUpdate
):
    return update_medical_record(
        record_id,
        record.model_dump(exclude_none=True)
    )


# Hapus rekam medis
@router.delete("/{record_id}")
def remove_medical_record(record_id: str):
    return delete_medical_record(record_id)