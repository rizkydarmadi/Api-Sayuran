from .model import Sayuran
from sqlalchemy import select
from database import Session


class SayuranRepository:
    
    @staticmethod
    def create_new_sayuran(name:str,catatan:str=None)->Sayuran:

        with Session() as session:
            new_sayuran = Sayuran(
                name=name,
                catatan=catatan,
            )
            session.add(new_sayuran)
            session.commit()
            session.refresh(new_sayuran)
        return new_sayuran
