'''
Extracting Data With Regular Expressions
'''
import re
hand=open('Sample data.txt')
numlist=list()
for line in hand:
    line=line.rstrip()
    numtarget=re.findall('[0-9][$0-9]*',line)
    if len(numtarget)>0:
        for num in numtarget:
            numlist.append(int(num))
print(sum(numlist))

# Optional: Just for Fun
import re
print(sum([int(num) for num in re.findall('[0-9][$0-9]*',open('Sample data.txt').read())]))
