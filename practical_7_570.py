"""
Practical 7
Roll no. : 570
Name : Sarthak Turkar
Batch : E3
Problem statement : Write a program in Python to enter two unequal nos.
if first no. is greater than display square of the smaller no. and cube of the greater no. otherwise vice-versa.
If no. are equal display the message
both no. are equal find square, square root and cube root of a number.
Date : 24/6/21
"""
# Input:

a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))

if a > b:
    print(a, "is greater than", b)
    c = a ** 3
    d = b ** 2
    print("Cube of greater number", a, "is : ", c)
    print("Square of smaller number", b, "is : ", d)
elif b > a:
    print(b, "is greater than", a)
    c = b ** 3
    d = a ** 2
    print("Square of smaller number", a, "is : ", d)
    print("Cube of greater number", b, "is : ", c)
elif a == b:
    print("Both the numbers are equal.")
    c = a ** 2
    d = a ** 1 / 2
    e = a ** 1 / 2
    print("Square of the equal numbers is : ", c)
    print("Square root of the equal numbers is : ", d)
    print("Cube root of the equal numbers is : ", e)


'''
OUTPUT:

Enter the first number : 5
Enter the second number : 3
5.0 is greater than 3.0
Cube of greater number 5.0 is :  125.0
Square of smaller number 3.0 is :  9.0

Process finished with exit code 0


Enter the first number : 7
Enter the second number : 9
9.0 is greater than 7.0
Square of smaller number 7.0 is :  49.0
Cube of greater number 9.0 is :  729.0

Process finished with exit code 0


Enter the first number : 14.4
Enter the second number : 14.4
Both the numbers are equal.
Square of the equal numbers is :  207.36
Square root of the equal numbers is :  7.2
Cube root of the equal numbers is :  7.2

Process finished with exit code 0

'''