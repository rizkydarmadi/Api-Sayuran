from sqlalchemy import Column,Integer,String
from database import Base


class Provinsi(Base):
    __tablename__ = "Provinsi"

    id = Column('id',Integer,primary_key=True,nullable=False)
    name = Column('nama', String(length=100),nullable=False)
    latitude = Column('latitude', String(length=32))
    longtitude = Column('longtitude', String(length=32))

