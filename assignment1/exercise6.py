talent = float(input("Enter talents" ))
pound = float(input("Enter pounds"))
lot = float(input("Enter lots"))
lots = talent * 20 * 30 + pound * 32 + lot
grams = lots * 13.3
kilograms = int(grams // 1000)
grams = grams % 1000
print("The weight in modern units:")
print(kilograms, "kilograms and", grams,"grams.")