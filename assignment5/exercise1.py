numbers = []
while True:
    a = input("Enter numbers (Empty to quit):")
    if a == "":
        break 
    number = int(a)
    numbers.append(number)  
numbers.sort(reverse=True)
print("The five greatest numbers:", numbers[:])