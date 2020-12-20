from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import sys
import urllib.request
import json
import pandas as pd

class PetCafe:
	def __init__(self):
		self.client_id = "QO2NsVbYBhctOoGzV3nX"
		self.client_secret = "FNKzHJOzAa`"
		self.encText = urllib.parse.quote("반려동물 출입 가능 카페")


	def callSite(self):
		url = "https://openapi.naver.com/v1/search/blog?query=" + self.encText # json 결과
		request = urllib.request.Request(url)
		request.add_header("X-Naver-Client-Id",self.client_id)
		request.add_header("X-Naver-Client-Secret",self.client_secret)
		response = urllib.request.urlopen(request)
		
		#check server success or not
		rescode = response.getcode()

		if(rescode==200):
		    response_body = response.read()
		    print(response_body.decode('utf-8'))
		else:
		    print("Error Code:" + rescode) 


		return result.json()



	def results(self):
		list = []
		for num in range(0,10):
			list = list + self.callSite()['items']

		return list


if __name__ == "__main__":
	pet = PetCafe()
	file = open('cafe.json', 'w+')
	file.write(json.dumps(pet.results()))
	

	df = pd.read_json('cafe.json')
	df.to_csv('crawling_naver_pet_cafe.csv', encoding='utf-8-sig',index=False)


	
