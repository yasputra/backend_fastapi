from pydantic import BaseModel

class Patient(BaseModel):
    nama: str
    umur: int
    alamat: str
