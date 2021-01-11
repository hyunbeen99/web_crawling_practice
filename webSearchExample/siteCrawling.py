import requests
from bs4 import BeautifulSoup

class Content:
	def __init__(self, topic, url, title, body):
		self.topic = topic
		self.title = title
		self.body = body
		self.url = url


	def print(self):
		print('New article found for topic: {}'.format(self.topic))
		print('URL: {}'.format(self.url))
		print('TITLE: {}'.format(self.title))
		print('BODY:|n {}'.format(self.body))


class Website:
	
	def __init__(self, name,url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
		self.name = name
		self.url = url
		self.searcUrl = searchUrl
		self.resultListing = resultListing
		self.resultUrl = resultUrl
		self.absoluteUrl = absoluteUrl
		self.titleTag = titleTag
		self.bodyTag = bodyTag 


class Crawler:
	def getPage(self, url):
		try:
			req = requests.get(url)
		except requests.exceptions.RequestException:

	
	
