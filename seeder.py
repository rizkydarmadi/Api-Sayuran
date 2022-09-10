from datetime import datetime
import json
from Provinsi.repository import ProvinsiRepository
from Sayuran.repository import SayuranRepository
from data_sayuran.repository import Data_sayuranRepository


class Seeder:
    def seed_provinsi():
        file = open('Provinsi/dataset/provinsi.json')
        provinsi = json.load(file)

        for data in provinsi['data']:
            ProvinsiRepository.create_new_provinsi(
                name=data['nama']
            )

    def seed_sayuran():
        file = open('Sayuran/dataset/sayuran.json')
        sayuran = json.load(file)

        for data in sayuran['data']:
            SayuranRepository.create_new_sayuran(
                name=data['nama']
            )
    
    def seed_sayuran_2021():
        file = open('data_sayuran/dataset/2021.json')
        data = json.load(file)
        data_json = []
        provinsi_id = 0
        for index,i in enumerate(data):
            provinsi_id += 1
            z = 0
            for j in data[index]:
                data_json.append({
                    "provinsi_id":provinsi_id,
                    'sayuran_id':int(j),
                    'value':i[f'{j}']
                })
        for i in data_json:
            if i['value'] == "-":
                i['value'] = 0
            Data_sayuranRepository.create_new_data_sayuran(
                sayuran_id=i['sayuran_id'],
                provinsi_id=i['provinsi_id'],
                value=i['value'],
                date=datetime(year=2021,month=1,day=1)
            )
        
Seeder.seed_sayuran_2021()
# Seeder.seed_provinsi()
# Seeder.seed_sayuran()

