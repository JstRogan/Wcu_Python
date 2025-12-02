radius = float(input("Enter radius: "))

if radius < 0:
    print("Radius cannot be negative")
else:
    pi = 3.14
    area = pi * radius * radius
    print("Area of circle:", area)
