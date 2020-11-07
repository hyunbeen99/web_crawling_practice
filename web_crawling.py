try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

for meta in bsObject.head.find_all('meta'):
	print(meta.get('content'))

#print(bsObject)
