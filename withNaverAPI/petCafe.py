import re
import requests
import json
import pandas as pd
from urllib.parse import quote
import urllib


class PetCafe:
	def __init__(self):
		self.client_id = "QO2NsVbYBhctOoGzV3nX"
		self.client_secret = "FNKzHJOzAa"
		self.encText = quote("반려동물 출입 가능 카페")
#		self.jsonlist =[]
		self.finalList = []


	def callSite(self, start):
		url = "https://openapi.naver.com/v1/search/blog?query="+self.encText+"&sort=sim&display=100&start="+str(start) # json 결과
		result = requests.get(url=url, headers={"X-Naver-Client-ID": self.client_id, "X-Naver-Client-Secret": self.client_secret})
		print(result)
		return result.json()



	def results(self):
		listt =[]
		#items include title, origin, allink, description, pubDate
		for num in range(0,10):
			listt = listt + self.callSite(num + 1)['items']
			listt = self.removeHTML(listt)
		self.finalList = self.finalList + listt

		return self.finalList
	

	def removeHTML(self, text):
		answer = []
		for i in text:
			answer.append(re.sub('<[^<]+?>', '', str(i)))

		return answer

	def fileCreate(self):
		# w+ : read/write , override
		file = open('petcafe.json', 'w+')
		file.write(json.dumps(self.finalList))
		df = pd.read_json('petcafe.json')
		df.to_csv('crawling_naver_pet_cafe.csv', encoding='utf-8-sig', index=False)

if __name__ == "__main__":
	pet = PetCafe()
	pet.results()
	pet.fileCreate()

