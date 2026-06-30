from pydantic import BaseModel


class User(BaseModel):
    nama: str
    email: str
    role: str