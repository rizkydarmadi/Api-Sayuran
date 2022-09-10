from datetime import datetime
from sqlalchemy import select
from database import Session
from .model import Data_sayuran


class Data_sayuranRepository:
    
    @staticmethod
    def create_new_data_sayuran(sayuran_id:int,provinsi_id:int,value:int,date:datetime):
        with Session() as session:
            new_data = Data_sayuran(
                sayuran_id=sayuran_id,
                provinsi_id=provinsi_id,
                value=value,
                date=date
            )
            session.add(new_data)
            session.commit()
            session.refresh(new_data)
        return new_data


