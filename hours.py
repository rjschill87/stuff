#Get file and create the dictionary
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
tod = dict()
clock = list()

#Go through each line of the file, strip space, look for lines that start with From:
for line in handle :
    line = line.rstrip()
    if not line.startswith('From') :
        continue
#If it exists, split the line into a list, grab the name from the list, and add to dict.
    line = line.split()
    try:
        time = line[5]
        time = time.split(':')
        hour = time[0]
        clock.append(hour)
    except: 
        continue
# add each item to dictionary and keep count
for key in clock :
    tod[key] = tod.get(key,0)+1
# create list, add tupple to list, sort, print
tmp = list()
for k,v in tod.items() :
    tmp.append( (k,v) )
tmp.sort()
for k,v in tmp :
    print k,v 
