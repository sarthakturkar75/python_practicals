i = int(input("Enter the 1st number : "))
end = int(input("Enter the 2nd number : "))
while i <= end:
    a = 0
    b = 2

    while b <= i / 2:
        if i % b == 0:
            a = a + 1
            break
        b = b + 1

    if a == 0:
        print(i, end=" ")
    i = i + 1
