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

    def openPage(self):
        options = webdriver.ChromeOptions()
        #open page or not
        #options.add_argument('headless')
        driver = webdriver.Chrome(executable_path='/home/hyunbeen/chromedriver', chrome_options=options)
        driver.get(self.url)
        driver.implicitly_wait(3)
        #time.sleep(1)
        search_box = driver.find_element_by_css_selector('input[id*="input_search"]')
        search_box.send_keys("애견용품")
        search_box.send_keys(Keys.RETURN)

        time.sleep(1)
        urlButton = driver.find_element_by_xpath('//span[@class="_16f7Q"]')
        #urlButton = driver.find_element_by_xpath('//a[@class]')
        #urlButton = driver.find_element_by_css_selector('a[role*="button"]')
        urlButton.click()



        return driver


if __name__== "__main__": 
    p = PetCrawler()
#    p.crawler()
    p.openPage()
