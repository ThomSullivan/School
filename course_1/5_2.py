max = None
min = None
while True:
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    for value in [fval]:
        if min is None :
            min = value
        elif value < min:
            min = value
    for value in [fval]:
        if max is None :
            max = value
        elif value > max:
            max = value
max = int(max)
min = int(min)
print('Maximum is ' + str(max))
print('Minimum is ' + str(min))
