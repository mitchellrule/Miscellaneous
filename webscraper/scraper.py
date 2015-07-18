from bs4 import BeautifulSoup
import urllib2


# Downloads and logs all <a> tags into a text file
def logLinks():
	website = urllib2.urlopen(raw_input('Enter website url: '))
	soup = BeautifulSoup(website.read())

	log = open('log.txt', 'ab')

	# Loop to write each tag to file
	for link in soup.find_all('a'):
		log.write(str(link.get('href')))
		log.write('\n')
		print (link.get('href'))
	log.close()

logLinks()