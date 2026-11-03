a = input("Enter a document:")
def hide_phone(a):
    result = ""
    i = 0
    while i < len(a):
        if a[i:i+3] == "+84":
            result += "[REDACTED]"
            i+=3
            while i < len(a) and a[i] in "0123456789":
                i+=1
        elif a[i] in"0123456789":
            number = ""
            for i in range(len(a)):
                if a[i] in "0123456789":
                    number += a[i]
                    i+=1
            if len(number)==10:
                result+="[REDACTED]"
            else:
                result += number
        else:
            result += a[i]
            i+=1
    return result
print(hide_phone(a))
