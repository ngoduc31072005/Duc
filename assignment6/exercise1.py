s = []
while True:
    a = input("Enter numbers (empty to quit):")
    if a == "" :
        break 
    s += [float(a)]
s.sort(reverse=True)
for i in s[:5]:
    print(i)
