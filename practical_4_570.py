"""
Practical 4
Roll no. : 570
Name : Sarthak Turkar
Batch : E3
Problem statement : Solve the factorial and Fibonacci sequence using recursive function in Python.
Date : 15/6/21
"""
# Input:

# Factorial

n = int(input("Enter value of N to calculate factorial : "))            # Taking the input from user for factorial


def factorial(n):                          # defining the function
    if n == 1 or n == 0:                   # checking if n is 0 or 1
        return 1
    i = 1

    while i <= n:
        fact = n * factorial(n - 1)                   # calculating the factorial
        return fact


result = factorial(n)                          # calling the function
print("Factorial is ", result)                 # printing the factorial

# Fibonacci

a = int(input("Enter number of terms of fibonacci series :"))              # taking the input from user for the number of terms of the fibonacci series


def fibonacci(a):                         # defining the function
    if a <= 1:                            # checking if a is 1 or 0
        return a
    else:
        fib = fibonacci(a - 1) + fibonacci(a - 2)                # calculating the fibonacci series
        return fib


fibonacci(a)                                  # calling the function
print("The fibonacci series is : ", end=" ")
for i in range(a):
    print(fibonacci(i), end=" ")              # printing each term of the series instead of only the last term

'''
OUTPUT:

Enter value of N to calculate factorial : 5
Factorial is  120
Enter number of terms of fibonacci series :6
The fibonacci series is :  0 1 1 2 3 5 
Process finished with exit code 0

'''
