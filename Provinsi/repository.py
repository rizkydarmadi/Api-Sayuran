from database import Session
from .model import Provinsi



class ProvinsiRepository:
    
    @staticmethod
    def create_new_provinsi(name:str,latitude:str=None,longtitude:str=None)->Provinsi:

        with Session() as session:
            new_provinsi = Provinsi(
                name=name,
                latitude=latitude,
                longtitude=longtitude,
            )
            session.add(new_provinsi)
            session.commit()
            session.refresh(new_provinsi)
        return new_provinsi
