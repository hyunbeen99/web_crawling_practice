import urllib 
import json 
import pandas as pd 
import requests
import glob
import os

class PetHospital:
	def __init__(self, number, initial):
		self.number = number
		self.initial = initial
		self.area = number+initial

	def callSite(self):
		key = "41547a577374697236345969436661"
		url = "http://openapi.seoul.go.kr:8088/"+key+"/json/"+self.area+"/1/1000"
		result = requests.get(url)
		if (result): print("!!!!!!!!!!!!!!!!!" + self.initial + "!!!!!!!!!!!!!!!!!")
		return result.json()
			

	def results(self):
		list_total_count = self.callSite()[self.area]['list_total_count']
	#	list_total_count = 2
		parse = []
		for num in range(0,list_total_count):
			jsonArray = []
	
			jsonName = self.callSite()[self.area]['row'][num]['BPLCNM']
			jsonArray.append(jsonName)
			jsonAddress = self.callSite()[self.area]['row'][num]['RDNWHLADDR']
			jsonArray.append(jsonAddress)

			parse.append(jsonArray)
			
		return parse


	def fileCreate(self):	
		df = pd.DataFrame(self.results(), columns=['NAME', 'ADDRESS'])
		df.columns = pd.MultiIndex.from_tuples(zip(['*', self.initial], df.columns))
		df.to_csv('S_'+self.initial+'병원.csv', index=False, encoding='utf-8-sig')


	def addAllCSV(self):
		input_file = '/home/hyunbeen/venv/web_crawling_practice/seoulOpenAPI' 
		output_file = '/home/hyunbeen/venv/web_crawling_practice/seoulOpenAPI/seoulHospital.csv' 

		allFile_list = glob.glob(os.path.join(input_file, 'S_*')) 
		allData = [] 

		for file in allFile_list:
		    df = pd.read_csv(file, index_col=None)
		    allData.append(df) 

		#axis 1 : vertical axis 0 : horizontal
		dataCombine = pd.concat(allData, axis=1, ignore_index=False)
		dataCombine.to_csv(output_file, index=False) 
		
if __name__ == "__main__":
	seoul = ['GN', 'GB', 'GD', 'GS', 'GA', 'GJ', 'GR', 'GC', 'NW', 'DB', 'DD', 'DJ', 'MP', 'SM', 'SC', 'SD', 'SB', 'SP', 'YC', 'YD', 'YS', 'EP', 'JN', 'JG', 'JR']
	for initial in seoul:
		ph = PetHospital('LOCALDATA_020301_',initial)
		ph.fileCreate()
		print("###############################FINISH##############################")

#	ph.addAllCSV()

