fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words=line.split()
    for num in range(len(words)):
        if words[num] not in lst:
            lst.append(words[num])
lst.sort()            
print(lst)
