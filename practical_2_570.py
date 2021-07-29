"""
Practical 2
Roll no. : 570
Name : Sarthak Turkar
Batch : E3
Problem statement : Write a Python program for following conditions.
                   • If n is single digit print square of it.
                   • If n is two digit print square root of it.
                   • If n is three digit print cube root of it
                   . if n is greater than three digit or less than zero print "invalid number".
Date : 2/6/21
"""
# Input:

a = int(input("Enter the number : "))  # taking the input from user
if 0 <= a < 10:  # checking if the input is single digit
    b = a ** 2  # calculating the square of the number
    print("Square of {0} is = {1} ".format(a, b))  # printing the square
elif 10 <= a < 100:  # checking if the input is double digit
    c = a ** 1 / 2  # calculating the square root of the number
    print("Square root of {0} is = {1} ".format(a, c))  # printing the square root
elif 100 <= a < 1000:  # checking if the input is triple digit
    d = a ** 1 / 3  # calculating the cube root of the number
    print("Cube root of {0} is = {1} ".format(a, d))  # printing the cube root
else:
    print("Invalid number")  # if the number is less than 0 or greater than 1000 than give invalid input

"""
Output :
Enter the number : 7
Square of 7 is = 49 

Process finished with exit code 0

Enter the number : 45
Square root of 45 is = 22.5 

Process finished with exit code 0

Enter the number : 555
Cube root of 555 is = 185.0 

Process finished with exit code 0
"""