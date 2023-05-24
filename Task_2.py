import csv

# Function: calculate_avg_salary - This function calculates the average salary.
def calculate_avg_salary(salaries):

    total_salary = sum(salaries)
    average_salary = total_salary / len(salaries)
    return round(average_salary, 2)

# Read departments from the departments.csv file.
departments = {}

with open('departments.csv', 'r') as file:

    reader = csv.reader(file)
    next(reader) 
    for row in reader:
        department_id = int(row[0])
        department_name = row[1]
        departments[department_id] = department_name

# Read employees from employees.csv file.
employees = {}

with open('employees.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        employee_id = int(row[0])
        employee_name = row[1]
        department_id = int(row[2])
        employees[employee_id] = (employee_name, department_id)

# Read salaries from salaries.csv file.
salaries = {}

with open('salaries.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        employee_id = int(row[0])
        month = row[1]
        salary = int(row[2])
        if employee_id in salaries:
            salaries[employee_id].append(salary)
        else:
            salaries[employee_id] = [salary]

# Calculate the average monthly salary for each department.
department_salaries = {}

for employee_id, (employee_name, department_id) in employees.items():
    if department_id in departments:  
        if department_id in department_salaries:
            department_salaries[department_id].extend(salaries[employee_id])
        else:
            department_salaries[department_id] = salaries[employee_id]
    else:
        print(f"Incorrect department ID  {employee_id}")

# Generate the report
print("DEPT_NAME ", " AVG_MONTHLY_SALARY (USD)")
print()

# Sort the departments in descending order based on the average salary.
sorted_departments = sorted(department_salaries.items(), key=lambda x: calculate_avg_salary(x[1]), reverse=True)

# Fetch top 3 departments along with their name and average monthly salary.
for i in range(3):
    department_id, salaries = sorted_departments[i]
    department_name = departments.get(department_id, "Unknown")
    average_salary = calculate_avg_salary(salaries)
    print(department_name," ", average_salary)
    print()



# Average Monthly Salary Report
# This script calculates the average monthly salary for each department based on data stored in CSV files. The following files are used:

# departments.csv: Contains department information with columns ID and NAME.
# employees.csv: Contains employee information with columns ID, NAME, and DEPT ID.
# salaries.csv: Contains salary information with columns EMP_ID, MONTH (YYYYMM), and AMT (USD).
# Dependencies
# This script requires the csv module, which is included in the Python standard library.

# Usage
# Ensure that the CSV files (departments.csv, employees.csv, and salaries.csv) are in the same directory as the script.
# Run the script using Python 3:
# python average_salary_report.py
# Code Explanation
# The script defines a function calculate_avg_salary to calculate the average salary.
# The script reads the department data from departments.csv and stores it in a dictionary called departments.
# The employee data is read from employees.csv and stored in a dictionary called employees.
# The salary data is read from salaries.csv and stored in a dictionary called salaries.
# The script calculates the average monthly salary for each department by aggregating the salaries of employees in each department.
# The resulting department salaries are stored in a dictionary called department_salaries.
# The script generates a report by sorting the department salaries in descending order based on the average salary.
# The top 3 departments, along with their names and average monthly salaries, are printed.
# Note: If an incorrect department ID is encountered while processing the employee data, an error message is printed.

# Feel free to modify the code as needed for your specific use case.