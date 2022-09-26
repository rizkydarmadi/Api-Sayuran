from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import user
import Sayuran

app = FastAPI(title='Pertanian')

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=CORS_ALLOWED_ORIGINS,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(user.auth_router)
app.include_router(Sayuran.Sayuran_router)
@app.get("/")
async def hello():
    return {'Hello': "You Make Me Happy"}