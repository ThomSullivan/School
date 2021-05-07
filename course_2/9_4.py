fname = input('Enter a file name: ')
fh = open(fname)
senders = dict()
for line in fh:
    if not line.startswith('From '):
        continue
    pieces = line.split()
    pieces = pieces[1]
    senders[pieces] = senders.get(pieces, 0) + 1
bigval = 0
for a,b in senders.items() :
    if b > bigval:
        bigval = b
        bigmail = a
print(bigmail,bigval)
