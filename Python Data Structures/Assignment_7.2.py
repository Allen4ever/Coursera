# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count_line=0
num=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    num=num+float(line[line.find('0'):])
    count_line=count_line+1
print('Average spam confidence: '+str(num/count_line))
