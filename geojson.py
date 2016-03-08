import urllib
import json

# url and api
serviceurl = 'http://python-data.dr-chuck.net/geojson?'
address = raw_input("Enter location:")
url = serviceurl + urllib.urlencode({'sensor':'false','address': address})
print 'Retrieving',url
uh = urllib.urlopen(url)
data = uh.read()
js = json.loads(str(data))

print "Retrieved",len(data)
#print json.dumps(js, indent=4)
#grab place id from json results
location = js['results'][0]['place_id']
print location