a = int(input("Enter the number for factorial : "))


def factorial(a):
    if a == 0 or a == 1:
        return 1

    count = 1
    i = 1
    while i <= a:
        count = count * i
        i = i + 1
    return count


b = factorial(a)
print("factorial is : ", b)
