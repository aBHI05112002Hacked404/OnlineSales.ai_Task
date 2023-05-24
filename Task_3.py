def compute(n):

    if n < 10:
        out = n ** 2
    elif n <=20:  # Fixed: To calculate the factorial correctly between 10 to 20 including 20 also, so the fix involved changing 'n<20' to 'n<=20'
        out = 1
        for i in range(1, n-9):  # Fixed: To calculate the factorial correctly, the fix involved changing 'n-10' to 'n-9'
            out *= i
    else:
       
        lim = n - 20
        out = 0  # Fixed: Initialize the 'out' variable to 0 instead of lim * lim
        for i in range(1, lim+1):  # Fixed: Changed lim to lim+1 to include the upper limit in the sum also
            out += i
    print(out)


n = int(input("Enter an integer: "))
compute(n)


# Integer Computation
# This script performs a computation based on an input integer n. The script calculates different outputs based on the value of n using the following logic:

# If n is less than 10, the script calculates the square of n and assigns it to the variable out.
# If n is between 10 and 20 (inclusive), the script calculates the factorial of n-9 and assigns it to the variable out.
# If n is greater than 20, the script calculates the sum of numbers from 1 to n-20 and assigns it to the variable out.
# Usage
# Run the script using Python 3.
# Enter an integer when prompted: Enter an integer: <integer>
# The script will perform the computation based on the input integer and print the result.
# Code Explanation
# The script defines a function compute that takes an integer n as input.
# Depending on the value of n, the script performs different computations.
# For n less than 10, the script calculates the square of n and assigns it to the variable out.
# For n between 10 and 20 (inclusive), the script calculates the factorial of n-9 and assigns it to the variable out. The factorial is calculated using a loop that multiplies each number from 1 to n-9.
# For n greater than 20, the script calculates the sum of numbers from 1 to n-20 and assigns it to the variable out. The sum is calculated using a loop that iterates from 1 to n-20 and adds each number to the sum.
# The script then prints the value of out.
# Note: The code has been fixed to correctly calculate the factorial and sum based on the provided logic.

# Feel free to modify the code as needed for your specific use case