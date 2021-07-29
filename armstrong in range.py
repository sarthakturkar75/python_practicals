a = input("Enter the starting range for armstrong number : ")
b = input("Enter the ending range for armstrong number : ")
f = len(a)
g = len(b)
a = int(a)
b = int(b)
for i in range(a, b+1):
    e = 0
    if f == g:
        for j in range(f):
            c = i // 10 ** j
            d = c % 10
            e = d ** f + e
            if i == e:
                print(i, "is an Armstrong number.")
    else:
        for j in range(g):
            c = i // 10 ** j
            d = c % 10
            e = d ** g + e
            if i == e:
                print(i, "is an Armstrong number.")




