from fastapi import APIRouter, Depends
from common.responses_schemas import BadRequest, InternalServerError, Forbidden
from common.responses_services import common_response
from .services import SayuranServices

router = APIRouter(tags=["Sayuran"])

# create endpoints here :)
