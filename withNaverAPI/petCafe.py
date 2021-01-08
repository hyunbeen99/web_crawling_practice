import re
import requests
import json
import pandas as pd
from urllib.parse import quote
import urllib


class PetCafe:
	def __init__(self, title):
		self.client_id = "QO2NsVbYBhctOoGzV3nX"
		self.client_secret = "FNKzHJOzAa"
		self.encText = quote(title)
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

		for i in listt:
			dictt = self.removeHTML(dict(i))
			self.finalList.append(dictt)

		return self.finalList
	

	def removeHTML(self, text):
		for key, value in text.items():
			text[key] = re.sub('<[^<]+?>', '', text[key])

		return text

	def fileCreate(self):
		# w+ : read/write , override
		file = open('petcafe.json', 'w+')
		file.write(json.dumps(self.finalList))
		df = pd.read_json('petcafe.json')
		df.to_csv('성북구병원.csv', encoding='utf-8-sig', index=False)

if __name__ == "__main__":
	pet = PetCafe("성북구 동물병원")
	pet.results()
	pet.fileCreate()

