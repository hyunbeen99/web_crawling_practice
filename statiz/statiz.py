from bs4 import BeautifulSoup 
from selenium import webdriver
import pandas as pd
import json
import numpy as np
import glob
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

chromeDriver = webdriver.Chrome(executable_path='/home/hyunbeen/chromedriver', chrome_options=chrome_options)

for page in range(8,9):
	url = "http://www.kbreport.com/leader/pitcher/main?rows=100&order=WAR&orderType=DESC&teamId=&pitcher_type=&year_from=2020&year_to=2020&gameType=&split01=&split02_1=&split02_2=&r_inning_count=&inning_count=0#/"+str(page)

	chromeDriver.get(url) #사용할 URL 
	html = chromeDriver.page_source 
	bsObject = BeautifulSoup(html, 'html.parser')


	temp = bsObject.find_all("table")[1]
	temp

	column = ["선수명","팀명","승","패","세","홀드","블론","경기","선발","이닝","삼진/9","볼넷/9","홈런/9","BABIP","LOB%",	"ERA","RA9-WAR","FIP","kFIP","WAR"]

	df = pd.DataFrame(columns=column)
	templen = len(temp.find_all("tr"))

	for i in range(2, templen):
		tempTr = temp.find_all("tr")[i]
		if(tempTr.find("th") is not None):
			continue
		row = {}
		column_idx = 0
		for j in range(1,21):
			tempTd = tempTr.find_all("td")[j].text
			row[column[column_idx]] = tempTd
			column_idx += 1
		df = df.append(row,ignore_index=True)
	df.to_csv("f"+str(page)+"stats.csv") 

'''input_file = '/home/hyunbeen/venv/web_crawling_practice'
output_file = '/home/hyunbeen/venv/web_crawling_practice/pitcher_stats_2020.csv' 

allFile_list = glob.glob(os.path.join(input_file, 'f*')) 
allData = [] 

for f in allFile_list:
	df = pd.read_csv(f, index_col=None, engine='python-fwf')
	allData.append(df) 

#axis 1 : vertical axis 0 : horizontal
dataCombine = pd.concat(allData, axis=0, ignore_index=False)
dataCombine.to_csv(output_file, index=False)

'''
