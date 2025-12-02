price1 = float(input("Enter price of item 1: "))
qty1 = int(input("Enter quantity of item 1: "))

price2 = float(input("Enter price of item 2: "))
qty2 = int(input("Enter quantity of item 2: "))

price3 = float(input("Enter price of item 3: "))
qty3 = int(input("Enter quantity of item 3: "))

total1 = price1 * qty1
total2 = price2 * qty2
total3 = price3 * qty3
total = total1 + total2 + total3

print("Item 1 total:", total1)
print("Item 2 total:", total2)
print("Item 3 total:", total3)
print("Final bill:", total)
