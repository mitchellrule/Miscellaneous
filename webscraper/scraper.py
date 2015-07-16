from bs4 import BeautifulSoup
import urllib2


website = urllib2.urlopen("http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=1;id=2014;type=year")
soup = BeautifulSoup(website.read())

