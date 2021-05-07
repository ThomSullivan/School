fname = input('Enter a file name: ')
fh = open(fname)
words = list()
for line in fh:
    line = line.rstrip()
    text = line.split()
    for word in text:
        if word in words:
            continue
        else:
            words.append(word)
words.sort()
print(words)
