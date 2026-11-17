s = ("winter","spring","summer","autumn")
a = int(input("Enter the number of a month:"))
if a == 12 or a ==1 or a ==2:
    print(s[0])
elif a >= 3 and a <=5 :
    print(s[1])
elif a >=6 and a<=8:
    print(s[2])
elif a>=9 and a<=11:
    print(s[3])
else:
    print("Enter another number")