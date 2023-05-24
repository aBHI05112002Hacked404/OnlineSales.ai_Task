# OnlineSales.ai_Task

# Task-1 SQL

# SQL Output Report Generation

## This script generates an output report by querying a relational database. The database schema includes three tables: Departments, Employees, and Salaries. Each table represents a worksheet in the provided attachment.

# Table Structure

## The script creates the following tables with the respective column definitions:

# Departments:

![image](https://github.com/aBHI05112002Hacked404/OnlineSales.ai_Task/assets/103949784/81d405f5-630c-42f3-b5a5-842a3376506d)

# Employees:

![image](https://github.com/aBHI05112002Hacked404/OnlineSales.ai_Task/assets/103949784/b418979b-b5af-48dd-bd39-124955db4583)

# Salaries:

![image](https://github.com/aBHI05112002Hacked404/OnlineSales.ai_Task/assets/103949784/78a505b5-ff04-44f9-adee-cc172511ca06)

# Steps

## Create a database named onlinesales_task1 using the following SQL command:

![image](https://github.com/aBHI05112002Hacked404/OnlineSales.ai_Task/assets/103949784/ebf4e47b-2ab2-48ee-8d64-9d1a8b11b4d3)

## Select the created database using the following SQL command:

![image](https://github.com/aBHI05112002Hacked404/OnlineSales.ai_Task/assets/103949784/a32963ee-02ce-4c36-82cc-96402695ab0e)

## Insert values into each table using the following SQL commands:

i. Inserting values into the Departments table:

![image](https://github.com/aBHI05112002Hacked404/OnlineSales.ai_Task/assets/103949784/bd6cf483-53a4-4c37-936c-9032b5320eeb)

ii. Inserting values into the Employees table:

![image](https://github.com/aBHI05112002Hacked404/OnlineSales.ai_Task/assets/103949784/143d8061-e929-4a44-887c-0b437bda4f66)

iii. Inserting values into the Salaries table:

![image](https://github.com/aBHI05112002Hacked404/OnlineSales.ai_Task/assets/103949784/d4c92668-c9c9-4545-8545-cf75399f4e3d)

## Execute the SQL command that generates the output report:

![image](https://github.com/aBHI05112002Hacked404/OnlineSales.ai_Task/assets/103949784/39298503-cdd6-4d14-ab81-89fec3d68155)

## The result of the query will be as follows:

![image](https://github.com/aBHI05112002Hacked404/OnlineSales.ai_Task/assets/103949784/8d016c29-f80b-485f-a320-6d5125cc1b70)

## Note: Ensure that you have a suitable SQL database management system installed and configured to execute the provided SQL commands.

## Feel free to modify the code or SQL queries as needed for your specific use case.

# Task-2 Scripting

## Average Monthly Salary Report
## This script calculates the average monthly salary for each department based on data stored in CSV files. The following files are used:

- departments.csv: Contains department information with columns ID and NAME.

- employees.csv: Contains employee information with columns ID, NAME, and DEPT ID.

- salaries.csv: Contains salary information with columns EMP_ID, MONTH (YYYYMM), and AMT (USD).

# Dependencies

- This script requires the csv module, which is included in the Python standard library.

# Usage

- Ensure that the CSV files (departments.csv, employees.csv, and salaries.csv) are in the same directory as the script.
- Run the script using Python 3:

# Code Explanation

- The script defines a function calculate_avg_salary to calculate the average salary.
- The script reads the department data from departments.csv and stores it in a dictionary called departments.
- The employee data is read from employees.csv and stored in a dictionary called employees.
- The salary data is read from salaries.csv and stored in a dictionary called salaries.
- The script calculates the average monthly salary for each department by aggregating the salaries of employees in each department.
- The resulting department salaries are stored in a dictionary called department_salaries.
- The script generates a report by sorting the department salaries in descending order based on the average salary.
- The top 3 departments, along with their names and average monthly salaries, are printed.

## Note: If an incorrect department ID is encountered while processing the employee data, an error message is printed.

## Feel free to modify the code as needed for your specific use case.

# Task-3 Debugging
## Integer Computation
## This script performs a computation based on an input integer n. The script calculates different outputs based on the value of n using the following logic:

- If n is less than 10, the script calculates the square of n and assigns it to the variable out.
- If n is between 10 and 20 (inclusive), the script calculates the factorial of n-9 and assigns it to the variable out.
- If n is greater than 20, the script calculates the sum of numbers from 1 to n-20 and assigns it to the variable out.

# Usage
- Run the script using Python 3.
- Enter an integer when prompted: Enter an integer: <integer>
- The script will perform the computation based on the input integer and print the result.
  
# Code Explanation
- The script defines a function compute that takes an integer n as input.
- Depending on the value of n, the script performs different computations.
- For n less than 10, the script calculates the square of n and assigns it to the variable out.
- For n between 10 and 20 (inclusive), the script calculates the factorial of n-9 and assigns it to the variable out. The factorial is calculated using a loop that multiplies each number from 1 to n-9.
- For n greater than 20, the script calculates the sum of numbers from 1 to n-20 and assigns it to the variable out. The sum is calculated using a loop that iterates from 1 to n-20 and adds each number to the sum.
- The script then prints the value of out.
  
  ## Note: The code has been fixed to correctly calculate the factorial and sum based on the provided logic.

  ## Feel free to modify the code as needed for your specific use case.
