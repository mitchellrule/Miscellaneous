from bs4 import BeautifulSoup
from urllib3 import poolmanager


# TODO Log to csv

# Downloads and logs all <a> tags into a text file
def logLinks():
	connectBuilder = poolmanager.PoolManager()
	# Take website url and name
	website     = connectBuilder.urlopen('GET', (input('Enter website url: ')))
	websiteName = input('What is the name of this website: ')
	soup        = BeautifulSoup(website.read(), 'html.parser')

	csvfile = open(websiteName + '.csv', 'w')

	for link in soup.findAll('a'):
		csvfile.write(str(link.get('href')))
		csvfile.write('\n')

	csvfile.close()

logLinks()