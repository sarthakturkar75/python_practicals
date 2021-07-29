marks = []
d = int(input("Enter the number of elements : "))
for l in range(0, d):
    element = int(input())

    marks.append(element)
print(marks)


def convert(marks):
    return tuple(marks)


a = 0
i = 0
while i < len(marks):
    a = a + marks[i]
    i = i + 1
print("Sum of the marks is : ", a)

tuple1 = (1, 4, 7, 8, 5, 34, 80, 6, 9, 0)
a = int(input("Enter the number to check existence in the list : "))
if a in tuple1:
    print(a, "exists in the tuple.", "It is on position", tuple1.index(a) + 1)
else:
    print(a, "does not exist in the tuple.")


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
