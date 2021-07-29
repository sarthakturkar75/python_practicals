"""
Practical 6
Roll no. : 570
Name : Sarthak Turkar
Batch : E3
Problem statement : To check whether input number is Armstrong number or not. An Armstrong number is an integer with three
digits such that the sum of the cubes of its digits is equal to the number itself. Ex. 371.

Date : 23/6/21
"""
# Input:

a = input("Enter the number to check for Armstrong number : ")
e = len(a)
d = 0
a = int(a)
for i in range(e):
    b = a // 10 ** i
    c = b % 10
    d = c ** e + d
if a == d:
    print(a, "is an Armstrong number.")
else:
    print(a, "is not an Armstrong number.")

'''
# OUTPUT:
Enter the number to check for armstrong number : 371
371 is an Armstrong number.

Process finished with exit code 0

Enter the number to check for armstrong number : 657
657 is not an Armstrong number.

Process finished with exit code 0

Enter the number to check for armstrong number : 1634
1634 is an Armstrong number.

Process finished with exit code 0

'''