from fastapi import APIRouter, Depends
from common.responses_schemas import BadRequest, InternalServerError, Forbidden
from common.responses_services import common_response
from .services import Data_sayuranServices

router = APIRouter(tags=["data_sayuran"])

# create endpoints here :)
