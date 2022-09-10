from fastapi import APIRouter
from .endpoints import router as data_sayuran

data_sayuran_router = APIRouter(prefix="/data_sayuran")
data_sayuran_router.include_router(data_sayuran)
