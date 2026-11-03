a = int(input("Enter an integer:"))
if a < 2:
    print("It is not a prime number")
else:
    for i in range(2,a):
        if a % i == 0:
            print("It is not a prime number")
        else:
            print("It is a prime number")