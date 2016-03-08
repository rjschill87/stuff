import urllib
import json

#Get URL, open, JSOn, check length
url = raw_input("Enter location:")
print "Retrieving: ",url
uh = urllib.urlopen(url)
data = uh.read()
js = json.loads(data)

#print json.dumps(js, indent=4)
print "Retrieved", len(js['comments'])
count = 0
total = 0
#Grab comment count and sum
for item in js['comments'] :
    value = int(item['count'])
    count = count + 1
    total = total + value

print "Count:",count
print "Sum:",total