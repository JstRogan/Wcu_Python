principal = float(input("Enter principal: "))
rate = float(input("Enter rate (%): "))
time = float(input("Enter time (years): "))

amount = principal * (1 + rate / 100) ** time
interest = amount - principal

print("Compound interest:", interest)
print("Total amount:", amount)
