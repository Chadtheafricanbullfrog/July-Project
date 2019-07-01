def main():
    print("hello world")

name = input("What is your name?")
print("Hello %s" %name)

if __name__ == "__main__":
    main()

f = int(input("Choose a number "))

if f > 5:
    print("f is greater than 5")

elif f < 5:
    print("f is less than 5")

elif f == 5:
    print("f is 5")
else:
    print("f is not a number")
