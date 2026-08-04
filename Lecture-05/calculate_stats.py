def calculate_stats(number):
    total_sum = sum(number)
    average = total_sum / len(number)
    maximum=max(number)
    minimum=min(number)
    return total_sum,average,maximum,minimum

number=[5,10,15,20,25]
total,avg,max_num,min_num = calculate_stats(number)

print(f"Total sum : {total}")
print(f"Average: {avg}")
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")
