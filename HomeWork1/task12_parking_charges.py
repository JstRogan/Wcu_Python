hours = float(input("Enter parking hours: "))

if hours <= 0:
    print("Hours must be positive")
elif hours <= 1:
    charge = 50
else:
    charge = 50 + (hours - 1) * 20

print("Parking charge:", charge)
