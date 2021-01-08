import urllib 
import json 
import pandas as pd 
from urllib.parse import quote
import requests
import urllib.request


def callSite(start, end):
	key = "41547a577374697236345969436661"
	url = "http://openapi.seoul.go.kr:8088/"+key+"/json/LOCALDATA_020301_GN/"+str(start)+"/"+str(end)	
	result = requests.get(url)
	print(result)
	return result.json()
		

def result():
	listt = []
	'''parse = []
	jsonArray = []
	js = callSite(1,10)
#	jsonObject = str(js)
	jsonArray = js.get('row')
	for idx in jsonArray:
		print(idx)
		parse.append(idx.get("BPLCNM"))'''
	for num in range(1,10):
		listt = callSite(1,10).get('row')
	
	return listt


def fileCreate():	
	file = open('pr_hospital.json', 'w+')
	file.write(json.dumps(result()))
	df = pd.read_json('pr_hospital.json')
	df.to_csv('강남구병원.csv', encoding='utf-8-sig', index=False)


if __name__ == "__main__":
	result()
	fileCreate()

