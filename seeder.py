import json
from Provinsi.repository import ProvinsiRepository
from Sayuran.repository import SayuranRepository

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

seed_sayuran()