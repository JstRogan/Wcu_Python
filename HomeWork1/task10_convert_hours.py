hours = float(input("Enter hours: "))

if hours < 0:
    print("Hours cannot be negative")
else:
    minutes = hours * 60
    seconds = hours * 3600
    print("Minutes:", minutes)
    print("Seconds:", seconds)
