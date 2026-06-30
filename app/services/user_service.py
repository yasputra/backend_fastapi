from app.core.firebase import db


def get_user(uid: str):

    doc = db.collection("users").document(uid).get()

    if not doc.exists:
        return None

    user = doc.to_dict()
    user["uid"] = uid

    return user