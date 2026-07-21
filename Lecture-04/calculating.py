max = 5

print("This profram calculates the sum of")
print(f"{max} numbers you will enter   ")

total = 0.0

for counter in range(max):
    number = int(input("enter a number"))
    total = total+number
    
print(f"the total is {total}")