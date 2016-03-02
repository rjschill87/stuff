#Get file and create the dictionary
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
contacts = dict()

#Go through each line of the file, strip space, look for lines that start with From:
for line in handle :
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
#If it exists, split the line into a list, grab the name from the list, and add to dict.
    line = line.split()
    address = line[1]
    contacts[address] = contacts.get(address,0)+1

#loop through each value, find out which occurs most often
sender = None
timesent = None
for person,times in contacts.items() :
    if timesent is None or times > timesent :
        sender = person
        timesent = times

print sender,timesent
