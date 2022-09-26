from .model import Sayuran
from sqlalchemy import select
from database import Session,engine
from sqlalchemy.sql import text
from datetime import datetime


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
    
    @staticmethod
    def get_all(limit:int=None,search:str=None,sayuran:int=None,provinsi:int=None,startdate:str=None,enddate:str=None):
        with engine.begin() as conn:

            query = '''
                SELECT hp.id,p.nama as provinsi ,s.nama as sayuran,hp.value,hp.date
                FROM public."hasil_pertanian" hp
                LEFT JOIN public."Sayuran" s on hp.sayuran_id = s.id
                LEFT JOIN public."Provinsi" p on hp.provinsi_id = p.id
            '''
            date = """'2021-01-01'""" #datetime.now().strftime("""'%Y-%m-%d'""")
            if (startdate and enddate) != None:
                query += 'WHERE date >= :startdate AND date <= :enddate'
            else:
                query += f'WHERE hp.date = {date}'

            if sayuran != None:
                query += ' AND s.id = :sayuran_id'
            
            if provinsi != None:
                query += ' AND p.id = :provinsi_id'
            
            if search != None:
                query += f""" AND s.nama LIKE '%{search}%' """

            if limit != None:
                query += ' LIMIT :limit ;'

            params = {
                'startdate':startdate,
                'enddate':enddate,
                'sayuran_id':sayuran,
                'provinsi_id':provinsi,
                'limit':limit
            }
            result = conn.execute(text(query),params)

            return result

