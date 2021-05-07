import re
fname = input('Enter a file name: ')
if len(fname) < 1:
    fname = 'sample_11.txt'
fh = open(fname)
digi = re.findall('[0-9]+', fh.read())
sum = 0
for num in digi:
    num = int(num)
    sum = num + sum
print(sum)
