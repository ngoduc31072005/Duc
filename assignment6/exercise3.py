s = []
while True:
    a = input("Enter names (empty to finish)")
    if a == "":
        break 
    if a in s:
        print("Existing name")
    else:
        print("New name")
        s += [a]
for a in s:
    print("List name:", (a))