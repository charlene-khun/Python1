largest = None
smallest = None
num1 = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num1 = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = num1;
    elif num1 > largest:
        largest = num1
    if smallest is None:
        smallest = num1;
    elif num1 < smallest:
        smallest = num1
    
print('Maximum is ', largest)
print('Minimum is ', smallest)