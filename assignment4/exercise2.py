a = input("Enter web color:")
def check_color(a):
    if len(a) != 7 :
        return False
    if a[0] != "#":
        return False
    for i in range(1,7):
        if a[i] not in "0123456789abcdefABCDEF":
            return False
    return True
print(check_color(a))