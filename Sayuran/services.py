from .repository import SayuranRepository
from .model import Sayuran
from common.responses_services import BadRequest, Created, InternalServerError, Ok
#from common.security import generate_jwt_token_from_user


class SayuranServices:
    @staticmethod
    async def get_all(limit:int=None,search:str=None,sayuran:int=None,provinsi:int=None,startdate:str=None,enddate:str=None):
        result = SayuranRepository.get_all(
            limit=limit,
            search=search,
            sayuran=sayuran,
            provinsi=provinsi,
            startdate=startdate,
            enddate=enddate
        )
        return Ok(data=[{
            'provinsi':i[1],
            'jenis_tani':i[2],
            'hasil_tani':i[3],
            'tanggal':i[4].strftime('%Y-%m-%d')
        }for i in result])
