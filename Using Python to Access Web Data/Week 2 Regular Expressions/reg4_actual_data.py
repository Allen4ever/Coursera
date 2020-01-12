import re
hand=open('Actual data.txt')
numlist=list()
for line in hand:
    line=line.rstrip()
    numtarget=re.findall('[0-9][$0-9]*',line)
    if len(numtarget)>0:
        for num in numtarget:
            numlist.append(int(num))
numsum=sum(numlist)
