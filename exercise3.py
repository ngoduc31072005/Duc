a = input("Enter paragraph:")
def sum_numbers(a):
    total = 0 
    number = ""
    for i in a:
        if i in "0123456789":
            number += i 
        else:
            if number !="":
                total += int(number)
    if number !="":
        total+= int(number)
    return total
print(sum_numbers(a))
        
