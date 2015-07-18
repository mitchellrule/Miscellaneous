from bs4 import BeautifulSoup
from urllib3 import poolmanager
import csv


# TODO Log to csv

# Downloads and logs all <a> tags into a text file
def logLinks():
	connectBuilder = poolmanager.PoolManager()
	# Take website url and name
	website = connectBuilder.urlopen('GET', (input('Enter website url: ')))
	websiteName = input('What is the name of this website: ')
	soup = BeautifulSoup(website.read(), "html.parser")
	
	# Open log txt file
	log = open(websiteName + '.txt', 'a')

	# Loop to write each tag to file
	for link in soup.find_all('a'):
		log.write(str(link.get('href')))
		log.write('\n')
		print (link.get('href'))
	log.close()

logLinks()