import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import string


def make_soup(url):
    thePage = urllib.request.urlopen(url)
    soupData = BeautifulSoup(thePage, "html.parser")
    return soupData

# opens and fills a file called items.txt, create before running
file = open(os.path.expanduser("items.txt"), "wb")


# set soup to the url wanting to scrap
soup = make_soup("Your URL goes here")

itemData = itemDataSaved = ""
for record in soup.findAll('ul'):
    itemData = ""
    for data in record.findAll('li'):
        itemData = itemData  + data.text
        itemDataSaved = itemDataSaved + "\n" + "\'" + itemData[0:] + "\'" + ","

file.write(bytes(itemDataSaved, encoding="ascii", errors='ignore'))

# prints the data scraped
print(itemDataSaved)
