a = float(input("Enter the electricity used(kWh):"))
while a !="":
    vat = bill*8/100
    total= vat +a
    if a < 50 :
        bill= a*8/100
    elif a > 100 :
        bill= a*2500
    else :
        bill= a*2000
    return total