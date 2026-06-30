from fastapi import APIRouter, Depends

from app.schemas.patient import Patient

from app.services.patient_service import (
    create_patient,
    get_all_patients,
    get_patient_by_id,
    update_patient,
    delete_patient
)

from app.core.role import (
    require_admin,
    require_admin_or_doctor
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)



# GET ALL PATIENTS
@router.get("")
def get_patients(
    user=Depends(require_admin_or_doctor)
):
    return get_all_patients()


# GET PATIENT BY ID
@router.get("/{patient_id}")
def get_patient(
    patient_id: str,
    user=Depends(require_admin_or_doctor)
):
    return get_patient_by_id(patient_id)



# CREATE PATIENT
@router.post("")
def add_patient(
    patient: Patient,
    admin=Depends(require_admin)
):
    return create_patient(patient.model_dump())



# UPDATE PATIENT
@router.put("/{patient_id}")
def edit_patient(
    patient_id: str,
    patient: Patient,
    admin=Depends(require_admin)
):
    return update_patient(
        patient_id,
        patient.model_dump()
    )

# DELETE PATIENT
@router.delete("/{patient_id}")
def remove_patient(
    patient_id: str,
    admin=Depends(require_admin)
):
    return delete_patient(patient_id)