"""
Practical 9
Roll no. : 570
Name : Sarthak Turkar
Batch : E3
Problem statement : Select the number from the entered list and find its position in Python (use Linear Search).
Date : 1/7/21
"""
# Input:

marks = []
d = int(input("Enter the number of elements : "))
for l in range(0, d):
    elements = int(input())

    marks.append(elements)
print(marks)

a = 0
i = 0
while i < len(marks):
    a = a + marks[i]
    i = i + 1
print("Sum of the marks is : ", a)


a = int(input("Enter the number to check existence in the list : "))
if a in marks:
    print(a, "exists in the list.", "It is on position", marks.index(a) + 1)
else:
    print(a, "does not exist in the list.")


def maxi(b):
    maximum = b[0]
    for j in b:
        if j > maximum:
            maximum = j
    return maximum


def mini(c):
    minimum = c[0]
    for k in c:
        if k < minimum:
            minimum = k
    return minimum


print("Maximum marks are : ", maxi(marks))
print("Minimum marks are : ", mini(marks))



'''
OUTPUT:

Enter the number of elements : 10
45
67
87
65
54
343
56
78
98
76
[45, 67, 87, 65, 54, 343, 56, 78, 98, 76]
Sum of the marks is :  969
Enter the number to check existence in the list : 45
45 exists in the list. It is on position 1
Maximum marks are :  343
Minimum marks are :  45

Process finished with exit code 0

'''