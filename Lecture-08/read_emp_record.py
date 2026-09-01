with open('employees.txt', 'r') as emp_file:
    for line in emp_file:
        emp_id = float(line)
        emp_name = float(line)
        emp_salary = float(line)
        print(f"ID: {emp_id}, Name: {emp_name}, Salary: ${float(emp_salary)}")