from urllib.request import urlopen
from bs4 import BeautifulSoup

def findTags(url):

	bs = urlopen(url)
	bsObject = BeautifulSoup(bs, "html5lib")

	### findAll(tag, attributes, recursive, text, limit, keywords) ###
	### if recursive == True -> find son of this tag, default = true
	### if recursive == False -> find only top of this tag

	nameSpan = bsObject.findAll('span', {'class' : 'green'}) #findAll(tageName, tagAttribute)
	#nameList = bsObject.findAll('span')
	#nameList = bsObject.findAll('span', {'class' : 'green','red'}) #findAll(tageName, tagAttribute)
	nameList = bsObject.findAll(text = "the prince")
	print(len(nameList))

	for name in nameSpan:
		a = name.get_text()

	return a

answer = findTags("http://www.pythonscraping.com/pages/warandpeace.html")


def codeForTree(url):
#bs.tag.subTag.anotherSubTag
	
