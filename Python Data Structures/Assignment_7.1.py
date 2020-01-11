# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for letter in fh:
    data=letter.upper()
    print(data.rstrip())
