cost = 3
secondnd_price = 45000
total = cost * secondnd_price
print("Total: " , total)
discount = int(input('Discount (%): '))
final = total - total * discount / 100
print('Final price:', final)
