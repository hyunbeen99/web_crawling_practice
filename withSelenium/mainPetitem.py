import pandas as pd
import json
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 


class PetCrawler:
    def __init__(self):
        self.url = 'https://map.naver.com/v5'
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='/home/hyunbeen/chromedriver', chrome_options=webdriver.ChromeOptions())

    def getUrl(self):
        #open page or not
        #options.add_argument('headless')
        self.driver.get(self.url)
        return self.driver

    def openPage(self):
        self.driver.implicitly_wait(3)
        #time.sleep(1)
        search_box = self.driver.find_element_by_css_selector('input[id*="input_search"]')
        search_box.send_keys("애견용품")
        search_box.send_keys(Keys.RETURN)

        self.driver.implicitly_wait(10) #

    def crawling(self):
        self.openPage()
#        xpath = "//a[@href='#']"
        #a=driver.find_element_by_xpath(xpath).click()
        name = self.driver.find_element_by_xpath('//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[2]/div[1]/a/span[1]')
        print(name.text)


if __name__== "__main__": 
    p = PetCrawler()
    p.getUrl()
    p.crawling()