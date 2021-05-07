fname = input('Enter a file name: ')
fh = open(fname)
count = 0

for line in fh:
    if not line.startswith('From '):
        continue
    else:
        count = count + 1
        line = line.rstrip()
        pieces = line.split()
        print(pieces[1])


print("There were", count, "lines in the file with From as the first word")
