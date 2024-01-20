def computepay(h,r):
    if(h<=40):
        gp = h*r
    else:
        gp = 40*r + (h-40)*1.5*r
    return gp

hrs = input("Enter hours: ")
rate = input("Enter rate: ")
hourf = float(hrs)
ratef = float(rate)
grosspay = computepay(hourf, ratef)
print("Pay", grosspay)
