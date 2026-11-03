a = input("Enter exam scores ( type done when finish)")
if a =="":
    print("No number Enter")
else:
    b=float(a)
    while a !="":
        if a=="done":
            break
        if b<0 and b>100:
            print("Score must be 0-100")
                  