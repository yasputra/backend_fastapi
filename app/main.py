from fastapi import FastAPI

from app.routers.patient_router import router as patient_router
from app.routers.auth_router import router as auth_router

app = FastAPI(
    title="Backend Rekam Medis",
    version="1.0.0"
)

# Register Router
app.include_router(auth_router)
app.include_router(patient_router)


@app.get("/")
def root():
    return {
        "message": "Backend Rekam Medis"
    }


@app.get("/test-firebase")
def test_firebase():
    return {
        "message": "Firebase Connected!"
    }