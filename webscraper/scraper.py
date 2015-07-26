from bs4 import BeautifulSoup
from urllib3 import poolmanager
import csv


# TODO Log to csv

# Downloads and logs all <a> tags into a text file
def logLinks():
	connectBuilder = poolmanager.PoolManager()
	# Take website url and name
	website     = connectBuilder.urlopen('GET', (input('Enter website url: ')))
	websiteName = input('What is the name of this website: ')
	soup        = BeautifulSoup(website.read(), 'html.parser')

	csvfile = open(websiteName + '.csv', 'w')
	writer = csv.writer(csvfile)

	# Open log txt file
	urls = []

	for url in soup.findAll('a', href=re.compile('5'))
		print url['href']

	for url in zip(urls):
		writer.writerow([url])

	csvfile.close()

logLinks()