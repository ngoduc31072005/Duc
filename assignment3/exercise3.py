a = input("Enter numbers (empty to quit):")
if a =="":
    print ("no number entered")
else:
    b = float(a)
    c = float(a)
    while a != "":
        a = input("Enter numbers (empty to quit):")
        if a == "":
            break
        d = float(a)
        if d < b:
            b=d
        if d > c:
            c=d
        
    print("smallest number is", b)
    print("largest number is ", c)
