name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
contacts = dict()


for line in handle :
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    line = line.split()
    address = line[1]
    contacts[address] = contacts.get(address,0)+1


sender = None
timesent = None
for person,times in contacts.items() :
    if timesent is None or times > timesent :
        sender = person
        timesent = times

print sender,timesent