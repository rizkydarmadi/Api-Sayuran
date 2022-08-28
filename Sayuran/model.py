from sqlalchemy import Column,Integer,String
from database import Base


class Sayuran(Base):
    __tablename__ = "Sayuran"

    id = Column('id',Integer,primary_key=True,nullable=False)
    name = Column('nama', String(length=100),nullable=False)
    catatan = Column('catatan', String(length=32))