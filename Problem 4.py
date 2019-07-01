y = 0
num = int(input("Please give me a number"))
list = [10, 20, 30, 40, 2, 6, 1, 66, 12, 22]
for x in list:
    if num > x:
        y = y+1
    print("There are ", y, 'numbers less than your number')