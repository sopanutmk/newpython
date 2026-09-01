num_emps = int(input('How many employees records do you want to enter? '))

with open('employees.txt' , 'w') as emp_file:
    for count in range(1,num_emps +1):
        print("Enter the information for employee #", count,sep='')
        name = input('Name: ')
        id_num = input('ID Number: ')
        dept = input('Department: ')
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')
        print()
        