a = input("Enter course codes")
def check_code(a):
    if len(a) != 6:
        return False
    for i in range(3):
        if not a[i].isupper() or not a[i].isalpha():
            return False
    for i in range(3,6):
        if not a[i].isdigit():
            return False
    return True
print(check_code(a))