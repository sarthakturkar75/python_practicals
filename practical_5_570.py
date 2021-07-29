"""
Practical 5
Roll no. : 570
Name : Sarthak Turkar
Batch : E3
Problem statement : To accept students five courses marks and compute his/her result. Student is passing if he/she scores
marks equal to and above 40 in each course. If student scores aggregate greater than 75%, then the grade is distinction.
If aggregate is 60>= and<75 then the grade if first division. If aggregate is50>= and<60, then the grade is second division.
If aggregate is 40>= and<50, then the grade is third division.

Date : 23/6/21
"""
# Input:

a = int(input("Enter the marks of Maths : "))                 # taking
b = int(input("Enter the marks of Physics : "))                # the
c = int(input("Enter the marks of Chemistry : "))               # input
d = int(input("Enter the marks of Biology : "))                  # from
e = int(input("Enter the marks of English : "))                   # user
if 0 <= (a or b or c or d or e) < 40:                       # checking if the student has failed
    print("The student has failed.")
elif (a or b or c or d or e) < 0:                           # checking if the input is appropriate
    print("Enter appropriate marks.")
elif (a or b or c or d or e) > 100:                         # checking if the input is appropriate
    print("Enter appropriate marks.")
else:
    agg = (a + b + c + d + e) / 5                   # calculating the aggregate
    if 75 < agg:                                           # checking for distinction
        print("Distinction")
    elif 60 <= agg < 75:                                   # checking for first rank
        print("First division")
    elif 50 <= agg < 60:                                   # checking for second rank
        print("Second division")
    elif 40 <= agg < 50:                                   # checking for third rank
        print("Third division")


'''
OUTPUT:

Enter the marks of Maths : -1
Enter the marks of Physics : 55
Enter the marks of Chemistry : 66
Enter the marks of Biology : 77
Enter the marks of English : 88
Enter appropriate marks.

Process finished with exit code 0

Enter the marks of Maths : 101
Enter the marks of Physics : 55
Enter the marks of Chemistry : 66
Enter the marks of Biology : 77
Enter the marks of English : 88
Enter appropriate marks.

Process finished with exit code 0

Enter the marks of Maths : 22
Enter the marks of Physics : 55
Enter the marks of Chemistry : 66
Enter the marks of Biology : 77
Enter the marks of English : 88
The student has failed.

Process finished with exit code 0

Enter the marks of Maths : 44
Enter the marks of Physics : 44
Enter the marks of Chemistry : 44
Enter the marks of Biology : 44
Enter the marks of English : 44
Third division

Process finished with exit code 0

Enter the marks of Maths : 55
Enter the marks of Physics : 55
Enter the marks of Chemistry : 55
Enter the marks of Biology : 55
Enter the marks of English : 55
Second division

Process finished with exit code 0

Enter the marks of Maths : 66
Enter the marks of Physics : 66
Enter the marks of Chemistry : 66
Enter the marks of Biology : 66
Enter the marks of English : 66
First division

Process finished with exit code 0

Enter the marks of Maths : 77
Enter the marks of Physics : 77
Enter the marks of Chemistry : 77
Enter the marks of Biology : 77
Enter the marks of English : 77
Distinction

Process finished with exit code 0

'''