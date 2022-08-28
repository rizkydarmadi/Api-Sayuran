from fastapi import APIRouter
from .endpoints import router as Sayuran

Sayuran_router = APIRouter(prefix="/Sayuran")
Sayuran_router.include_router(Sayuran)
