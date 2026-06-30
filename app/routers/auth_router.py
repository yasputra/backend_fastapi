from fastapi import APIRouter, Depends, HTTPException

from app.core.security import verify_token
from app.services.user_service import get_user

router = APIRouter(
    tags=["Authentication"]
)


@router.get("/me")
def me(decoded_token=Depends(verify_token)):

    uid = decoded_token["uid"]

    user = get_user(uid)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User tidak ditemukan"
        )

    return user