name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    line=line.split()
    if len(line)>0 and line[0]=='From':
        counts[line[1]]=counts.get(line[1],0)+1
num_max=0
for email,num in counts.items():
    if num>num_max:
        num_max=num
        committer=email
print(committer,num_max)
