import scholarly
import urllib.request
from pymongo import MongoClient

# Note: the scholarly API is really slow. We'll want to cache the data populated from 
# this, and/or eventually write our own API.

# This "user_agent" thing can go in a configuration file.
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent' : user_agent} 

search_query = scholarly.search_pubs_query('Category theory for the sciences')
book = next(search_query)

request=urllib.request.Request(book.url_scholarbib, None, headers)
response = urllib.request.urlopen(request)
bibtex_reference = response.read()

def populate_local_db(,)
    """ """



