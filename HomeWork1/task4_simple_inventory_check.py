in_stock = int(input("Enter items in stock: "))
requested = int(input("Enter items requested: "))

if in_stock < 0 or requested < 0:
    print("Quantity cannot be negative")
elif requested <= in_stock:
    print("Order can be placed")
else:
    print("Not enough items in stock")
