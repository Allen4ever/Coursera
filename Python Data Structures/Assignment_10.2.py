name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    line=line.split()
    if len(line)>0 and line[0]=='From':
        date=line[5].split(':')
        counts[date[0]]=counts.get(date[0],0)+1
for k,v in sorted(counts.items()):
    print(k,v)
