n = int(input("Enter number of employees: "))
data = {}

for _ in range(n):
    dept = input("Enter department number: ")
    emp = input("Enter employee roll no: ")
    salary = float(input("Enter salary: "))
    
    if dept not in data:
        data[dept] = []
    data[dept].append(salary)

for dept, salaries in data.items():
    print(f"Department {dept}: Min Salary = {min(salaries)}, Max Salary = {max(salaries)}")
