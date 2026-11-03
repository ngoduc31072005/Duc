a1 = float(input("Enter the diameter of pizza 1:"))
b1 = float(input("Enter the price of pizza 1:"))
a2 = float(input("Enter the diameter of pizza 2:"))
b2 = float(input("Enter the price of pizza 2:"))
unitprice1 = b1 / (3.14*(a1/2)**2)
unitprice2 = b2 / (3.14*(a2/2)**2)
if unitprice1 < unitprice2 :
    print("Pizza 1 provides better value for money.")
elif unitprice1 == unitprice2 :
    print("Same value.")
else:
    print("Pizza 2 provides better value for money.")