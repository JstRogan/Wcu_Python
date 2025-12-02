amount = float(input("Enter grocery amount: "))
tax_percent = float(input("Enter tax (%): "))

if amount < 0:
    print("Amount cannot be negative")
elif tax_percent < 0:
    print("Tax cannot be negative")
else:
    tax = amount * tax_percent / 100
    total = amount + tax
    print("Tax:", tax)
    print("Total with tax:", total)
