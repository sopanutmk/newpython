hours = int(input("Enter the number of hours worked: "))
rate = float(input("Enter the hourly pay rate: "))

if hours <= 40:
    pay = hours * rate
else:
    pay = (hours - 40) * (rate * 1.5) + (40 * rate)
print("Total pay: $" + str(pay))
    
