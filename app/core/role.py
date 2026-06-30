from fastapi import Depends, HTTPException

from app.core.security import verify_token
from app.services.user_service import get_user


def require_admin(decoded_token=Depends(verify_token)):

    uid = decoded_token["uid"]

    user = get_user(uid)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User tidak ditemukan"
        )

    if user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Hanya admin yang dapat mengakses"
        )

    return user


def require_doctor(decoded_token=Depends(verify_token)):

    uid = decoded_token["uid"]

    user = get_user(uid)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User tidak ditemukan"
        )

    if user["role"] != "dokter":
        raise HTTPException(
            status_code=403,
            detail="Hanya dokter yang dapat mengakses"
        )

    return user

def require_admin_or_doctor(decoded_token=Depends(verify_token)):

    uid = decoded_token["uid"]

    user = get_user(uid)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User tidak ditemukan"
        )

    if user["role"] not in ["admin", "dokter"]:
        raise HTTPException(
            status_code=403,
            detail="Akses ditolak"
        )

    return user