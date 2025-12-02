price = float(input("Enter price: "))
discount = float(input("Enter discount (%): "))

if discount < 0:
    print("Discount cannot be negative")
elif discount > 100:
    print("Discount cannot be more than 100%")
else:
    total = price - price * discount / 100
    print("Total price:", total)
