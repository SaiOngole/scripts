import urllib2
import json
url = 'http://api.icndb.com/jokes/random/'
# url = 'http://api.icndb.com/jokes/random?limitTo=[nerdy]'


response = json.loads(urllib2.urlopen(url).read())

print response['value']['joke']
