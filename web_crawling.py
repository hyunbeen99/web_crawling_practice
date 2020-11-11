from urllib.request import urlopen
from bs4 import BeautifulSoup

### if recursive == True -> find son of this tag, default = true
### if recursive == False -> find only top of this tag

def findTags(url):

	bs = urlopen(url)
	bsObject = BeautifulSoup(bs, "html5lib")

	### findAll(tag, attributes, recursive, text, limit, keywords) ###
	green = []
	nameSpan = bsObject.findAll('span', {'class' : 'green'}) #findAll(tageName, tagAttribute)
	for name in nameSpan:
		green.append(name.get_text())

	return green


def findLenOfTags(url):
	bs = urlopen(url)
	bsObject = BeautifulSoup(bs, "html5lib")

	nameList = bsObject.findAll(text = "the prince")

	return len(nameList)


def main():
	tag_ = findTags("http://www.pythonscraping.com/pages/warandpeace.html")
	lentag_ = findLenOfTags("http://www.pythonscraping.com/pages/warandpeace.html")

	print(tag_)
	print(lentag_)
a = main()



#bs.tag.subTag.anotherSubTag
#son of table = th, td, img, span, tr // just use .children 


