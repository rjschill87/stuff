import urllib
import xml.etree.ElementTree as ET

#Get URL, open, check length of document
url = raw_input("Enter location:")
print "Retrieving: ",url
openUrl = urllib.urlopen(url)
info = openUrl.read()
print 'Retrieved', len(info),'characters'

# Parse XML and look for <count>
tree = ET.fromstring(info)
count = tree.findall('.//count')

# Sum and keep count of number of comments
each = 0
total = 0
for item in count :
    value = int(item.text)
    total = total + value
    each = each + 1

print "Count:",each
print "Sum: ",total

