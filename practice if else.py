a = int(input("Enter 1st number to compare : "))
b = int(input("Enter 2nd number to compare : "))
c = int(input("Enter 3rd number to compare : "))
if a > b and a > c:
    print("a is the greatest number")
elif b > a and b > c:
    print("b is the greatest number")
else:
    print("c is the greatest number")
