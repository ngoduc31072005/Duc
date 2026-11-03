a = input("Enter the sex:")
b = float(input("Enter the hemoglobin value (g/l):"))
if a == "females" :
    if b < 117 :
        print("low")
    elif b <= 155 :
        print("normal")
    else :
        print("high")
if a == "males" :
    if b < 134:
        print("low")
    elif b <= 167:
        print("normal")
    else :
        print("high")
else:
    print("not available")