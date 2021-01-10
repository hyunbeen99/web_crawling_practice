from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen
import pandas as pd
import json
import time
import numpy as np
from selenium import webdriver

class PetItem:
		
	def openPage(self):
		options = webdriver.ChromeOptions()
		#open page or not
		options.add_argument('headless')
		driver = webdriver.Chrome(executable_path='/home/hyunbeen/chromedriver', chrome_options=options)

		#find_lelment_by_css_selector = method to extract tags
		naver_url = 'https://m.map.naver.com/search2/search.nhn?query=%EC%95%A0%EA%B2%AC%EC%9A%A9%ED%92%88&sm=sug&style=v5#/list'
		driver.get(naver_url)
		return driver


	def titleCrawling(self):
		result = []
		name = 1

		print("start")

		while True:
			print(name)

			kind = self.openPage().find_element_by_xpath('//*[@id="ct"]/div[2]/ul/li[%d]/div[1]/a/div/em' %name).text

			if(kind == "애견용품"):
				try:
#html = self.openPage().find_element_by_xpath('//*[@id="ct"]/div[2]/ul/li[%name]/div[1]/a/div/strong' %name)
					html = self.openPage().find_element_by_css_selector('#ct > div.search_listview._content._ctList > ul > li:nth-child(%d) > div.item_info > a > div > strong' %name)
					result.append(html.text)
					name += 1
					print('ok')
					print()
					
				except IndexError:
					print("Index out of range")
					pass	
			else:
				print('not found')
				print()
				name += 1

			if name == 10: break

		print('done')
		return result
#	print(result)

	def fileCreate(self):	
		df = pd.DataFrame(self.titleCrawling(), columns=['NAME'])
		df.to_csv('result.csv', index=False, encoding='utf-8-sig')
		

		
if __name__ == "__main__":
	ph = PetItem()		
	ph.fileCreate()
	
