from bs4 import BeautifulSoup
import urllib2


#website = urllib2.urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
#soup = BeautifulSoup(website.read())

#TODO Convert to reusable functions and objects
def getLinks():
	website = urllib2.urlopen(raw_input('Enter website url: '))
	soup = BeautifulSoup(website.read())

	log = open('log.txt', 'ab')

	for link in soup.find_all('a'):
		log.write(str(link.get('href')))
		log.write('\n')
		print (link.get('href'))
	log.close()

getLinks()