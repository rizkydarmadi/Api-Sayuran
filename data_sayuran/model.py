from sqlalchemy import Column,Integer,ForeignKey,DateTime
from database import Base


class Data_sayuran(Base):
    __tablename__ = "hasil_pertanian"

    id = Column('id',Integer,primary_key=True,nullable=False)
    sayuran_id = Column('sayuran_id',ForeignKey('Sayuran.id'))
    provinsi_id = Column('provinsi_id',ForeignKey('Provinsi.id'))
    value = Column('value',Integer)
    date = Column('date', DateTime(timezone=True))



    
