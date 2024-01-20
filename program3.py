hrs = input("Enter hours: ")
rate = input("Enter rate: ")
h = float(hrs)
r = float(rate)
if h <=40:
    grosspay = h*r
else:
    grosspay = 40*r + ((h-40)*1.5*r)
print(grosspay)