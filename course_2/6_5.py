text = 'X-DSPAM-confidence:    0.8475'
num = text.find('0')
print(float(text[num:]))
