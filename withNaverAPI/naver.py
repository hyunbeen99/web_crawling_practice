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
		self.encText = urllib.parse.quote("반려동물%출입%가능%카페")


	def callSite(self, start):
		url = "https://openapi.naver.com/v1/search/blog?query=" + self.encText + "&sort=sim&display=100&start=" + str(start) # json 결과
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
		#items include title, origin, allink, description, pubDate
		for num in range(0,10):
			list = list + self.callSite(num * 100)['items']

		return list

	def fileCreate(self):
		finalList = []
		finalList = finalList + self.results()
		# w+ : read/write , override
		file = open('petcafe.json', 'w+')
		file.write(json.dumps(finalList))
		df = pd.read_json('petcafe.json')
		df.to_csv('crawling_naver_pet_cafe.csv', encoding='utf-8-sig', index=False)

if __name__ == "__main__":
	pet = PetCafe()
	pet.fileCreate


	
