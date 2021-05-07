fname = input('Enter a file name:')
hand = open(fname)
total = 0
hits = 0
for line in hand:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    hits = hits + 1
    num = float(line[19:])
    total = total + num
    avg = total / hits
#print(hits)
#print(num)
#print(total)
print('Average spam confidence: ' + str(avg))
