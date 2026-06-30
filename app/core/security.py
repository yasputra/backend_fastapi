from fastapi import Header, HTTPException
from firebase_admin import auth

# DEVELOPMENT MODE
DEV_MODE = True


def verify_token(authorization: str = Header(None)):

    # DEVELOPMENT MODE   
    if DEV_MODE:
        return {
            "uid": "dev-admin"
        }

    # PRODUCTION MODE
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