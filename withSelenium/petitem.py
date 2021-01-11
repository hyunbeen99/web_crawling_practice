from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen
import pandas as pd
import json
import time
import numpy as np
from selenium import webdriver

class PetItem:
	def __init__(self):
		self.url = 'https://m.map.naver.com/search2/search.nhn?query=%EC%95%A0%EA%B2%AC%EC%9A%A9%ED%92%88&sm=sug&style=v5#/list'

	def openPage(self):
		options = webdriver.ChromeOptions()
		#open page or not
		options.add_argument('headless')
		driver = webdriver.Chrome(executable_path='/home/hyunbeen/chromedriver', chrome_options=options)
		driver.get(self.url)

		return self.driver


	def titleCrawling(self):
		result = []

		for name in range(1,75):
			array = []
			kind = self.openPage().find_element_by_xpath('//*[@id="ct"]/div[2]/ul/li[%d]/div[1]/a/div/em' %name).text
			if(kind == "애견용품"):
				try:
					html = self.openPage().find_element_by_css_selector('#ct > div.search_listview._content._ctList > ul > li:nth-child(%d) > div.item_info > a > div > strong' %idx)
					array.append(html.text)
					html2 = self.openPage().find_element_by_css_selector('#ct > div.search_listview._content._ctList > ul > li:nth-child(%d) > div.item_info > div.item_info_inn > div > a' %idx)
					array.append(html2.text)
					print('ok')
					print()
					result.append(array)
				
					
				except IndexError:
					print("Index out of range")
					pass	
			else:
				print('not found')

		return result

	def fileCreate(self):	
		df = pd.DataFrame(self.titleCrawling(), columns=['NAME', 'ADDRESS'])
		df.to_csv('petitem.csv', index=False, encoding='utf-8-sig')
		
if __name__ == "__main__":
	ph = PetItem()		
	ph.fileCreate()
	
