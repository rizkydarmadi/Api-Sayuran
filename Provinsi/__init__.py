from fastapi import APIRouter
from .endpoints import router as Provinsi

Provinsi_router = APIRouter(prefix="/Provinsi")
Provinsi_router.include_router(Provinsi)
