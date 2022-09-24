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
	
	def seed_sayuran_2020():
		file = open('data_sayuran/dataset/2020.json')
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
				date=datetime(year=2020,month=1,day=1)
			)
	
	def seed_sayuran_2019():
		file = open('data_sayuran/dataset/2019.json')
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
				date=datetime(year=2019,month=1,day=1)
			)
	
	def seed_sayuran_2018():
		file = open('data_sayuran/dataset/2018.json')
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
				date=datetime(year=2018,month=1,day=1)
			)

	def seed_sayuran_2017():
		file = open('data_sayuran/dataset/2017.json')
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
				date=datetime(year=2017,month=1,day=1)
			)
	
	def seed_sayuran_2016():
		file = open('data_sayuran/dataset/2016.json')
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
				date=datetime(year=2016,month=1,day=1)
			)
	
	def seed_sayuran_2015():
		file = open('data_sayuran/dataset/2015.json')
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
				date=datetime(year=2015,month=1,day=1)
			)
	
	def seed_sayuran_2014():
		file = open('data_sayuran/dataset/2014.json')
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
				date=datetime(year=2014,month=1,day=1)
			)
	
	def seed_sayuran_2013():
		file = open('data_sayuran/dataset/2013.json')
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
				date=datetime(year=2013,month=1,day=1)
			)
	def seed_sayuran_2012():
		file = open('data_sayuran/dataset/2012.json')
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
				date=datetime(year=2012,month=1,day=1)
			)
	def seed_sayuran_2011():
		file = open('data_sayuran/dataset/2011.json')
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
				date=datetime(year=2011,month=1,day=1)
			)

# Seeder.seed_provinsi()
# Seeder.seed_sayuran()
# Seeder.seed_sayuran_2021()
# Seeder.seed_sayuran_2020()
# Seeder.seed_sayuran_2019()
# Seeder.seed_sayuran_2018()
# Seeder.seed_sayuran_2017()
# Seeder.seed_sayuran_2016()
# Seeder.seed_sayuran_2015()
# Seeder.seed_sayuran_2014()
# Seeder.seed_sayuran_2013()
# Seeder.seed_sayuran_2012()
# Seeder.seed_sayuran_2011()
