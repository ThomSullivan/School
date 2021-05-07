fname = input('Enter a file name: ')
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
hours = dict()
for line in fh:
    if not line.startswith('From '):
        continue
    pieces = line.split()
    pieces = pieces[5]
    hour = pieces[:2]
    hours[hour] = hours.get(hour, 0) + 1
lst=list()
for k,v in hours.items():
    newtup = (k, v)
    lst.append(newtup)
lst.sort()
for val, key in lst :
    print(val, key)
