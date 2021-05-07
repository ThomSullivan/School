hrs = input('Enter hours: ')
rate = input('enter rate: ')
try:
    h = float(hrs)
    r = float(rate)
except:
    print('error, please enter numerical input')
    quit()
def computepay(h, r):
    if h > 40:
        ot = h - 40
        otp = (40 * r) + (ot * (r * 1.5))
        return(otp)
    else:
        return( h * r)
    return
p = computepay(h, r)
print('Pay',p)
