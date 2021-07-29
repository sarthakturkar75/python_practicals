a = int(input("Enter the number for fibonacci : "))


def fibonacci(a):
    count = 0
    i = 0
    j = 1
    while i <= a:
        count = i + j
        return count
        i = j
        j = count


print("Fibonacci series : ", end=" ")
k = 1
while k < a:
    print(fibonacci(a), end=" ")
    k = k + 1

