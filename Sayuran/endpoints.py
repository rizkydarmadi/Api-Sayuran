from fastapi import APIRouter, Depends
from common.responses_schemas import BadRequest, InternalServerError, Forbidden
from common.responses_services import common_response
from .services import SayuranServices
from common.security import oauth2_scheme,get_user_from_jwt_token


router = APIRouter(tags=["Sayuran"])

# create endpoints here :)
router = APIRouter(
    tags=['hasil-pertanian']
)

@router.get('/')
async def get_all(limit:int=50,search:str=None,sayuran:int=None,provinsi:int=None,startdate:str=None,enddate:str=None,token: str = Depends(oauth2_scheme)):
    result = await SayuranServices.get_all(
        limit=limit,
        search=search,
        sayuran=sayuran,
        provinsi=provinsi,
        startdate=startdate,
        enddate=enddate
    )
    return common_response(result)
