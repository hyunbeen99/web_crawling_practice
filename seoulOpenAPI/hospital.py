import urllib 
from urllib.request import HTTPError
import json 
import pandas as pd 
from urllib.parse import quote
import requests
import urllib.request

class PetHospital:
	def __init__(self):
		self.parse = []

	def callSite(self):
		key = "41547a577374697236345969436661"
		url = "http://openapi.seoul.go.kr:8088/"+key+"/json/LOCALDATA_020301_GN/1/1000"
		result = requests.get(url)
		print(result)
		return result.json()
			

	def results(self):
		jsonArray = []
		list_total_count = self.callSite()['LOCALDATA_020301_GN']['list_total_count']
		print(list_total_count)
		for num in range(0,list_total_count):
			jsonArray = self.callSite()["LOCALDATA_020301_GN"]['row'][num]['BPLCNM']

			self.parse.append(jsonArray)
		return self.parse


	def fileCreate(self):	
		print(self.parse)
		df = pd.DataFrame(self.parse, columns=['name'])
		df.to_csv('강남구병원.csv', index=False, encoding='utf-8-sig')

		'''file = open('pethospital.json', 'w+')
		file.write(json.dumps(self.parse))
		df = pd.read_json('pethospital.json')
		df.to_csv('강남구병원.csv', encoding='utf-8-sig', index=False)'''

if __name__ == "__main__":
	ph = PetHospital()
	ph.results()
	ph.fileCreate()

