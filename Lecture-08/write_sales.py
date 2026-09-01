num_days = int(input("For how many days do you have sales? "))

with open("sales.txt", "w") as sales_file:
    
    for count in range(num_days):
        sales = float(input(f"Enter the sales for day {count + 1}: "))
        sales_file.write(f"{sales}\n")