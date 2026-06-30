from fastapi import Header, HTTPException
from firebase_admin import auth


def verify_token(authorization: str = Header(None)):
    """
    Memverifikasi Firebase ID Token dari Authorization Header
    Format:
    Authorization: Bearer <firebase_id_token>
    """

    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Authorization header tidak ditemukan"
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Format token salah"
        )

    id_token = authorization.split("Bearer ")[1]

    try:
        decoded_token = auth.verify_id_token(id_token)

        return decoded_token

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Token tidak valid"
        )