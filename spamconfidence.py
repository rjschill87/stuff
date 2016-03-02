#Request file and try to open
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print "File cannot be opened: ",fh
    exit()
#Grab the lines containing spam confidence from each line
count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count = count + 1
    pos = line.find(":")
    #Grab the exact value
    value = float(line[pos+1:])
    #Average total of all lines so far
    total = total + value
    
print "Average spam confidence:",total / count

