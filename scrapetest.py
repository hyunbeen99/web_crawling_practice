from urllib.request import urlopen
from urllib.request import HTTPError # when we can't find the page
from urllib.request import URLError  # when server could not be found
from bs4 import BeautifulSoup  #HTML -> XML object

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		print(e)
		return None
	except URLError as e:
		print("This server could not be found!")
		return None

	try:
		#bs = BeautifulSoup(html, 'html.parser')
		#bs = BeautifulSoup(html.read(), 'html.parser')
		bs = BeautifulSoup(html, 'html5lib') # html5lib, lxml = instead of html.parser when the html codes are mixed
		title = bs.h1
		#print(bs.h1)  # if we need to check if the tags are exist or not
		#print(bs.html.body.h1)
		#print(bs.html.h1)
		#print(bs.body.h1)

	except AttributeError as e:
		return None

	
	return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")

if (title == None):
	print("There is no title in the URL")
else:
	print(title)



