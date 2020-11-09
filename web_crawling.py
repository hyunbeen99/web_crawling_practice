from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObject = BeautifulSoup(html, "html5lib")


### findAll(tag, attributes, recursive, text, limit, keywords) ###
### if recursive == True -> find son of this tag, default = true
### if recursive == False -> find only top of this tag

nameSpan = bsObject.findAll('span', {'class' : 'green'}) #findAll(tageName, tagAttribute)
#nameList = bsObject.findAll('span')
#nameList = bsObject.findAll('span', {'class' : 'green','red'}) #findAll(tageName, tagAttribute)
nameList = bsObject.findAll(text = "the prince")
print(len(nameList))

for name in nameSpan:
	print(name.get_text())


