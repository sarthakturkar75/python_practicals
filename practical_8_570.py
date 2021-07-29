"""
Practical 8
Roll no. : 570
Name : Sarthak Turkar
Batch : E3
Problem statement :  Write a Python program to perform following string operations.
 a) String concatenation b) String Reverse c) String compare d) String length e) Palindrome f) Case change.
Date : 15/7/21
"""
# INPUT:


str0 = "tHe trUTh Is tHat "
str1 = "i Am IrOnMan"

# 1)String concatenation
print(str0 + str1)
print("".join([str0, str1]))

# 2)String Reverse
str2 = "yUo KnoW me"[::-1]
print(str2)

# 3)String compare
print("you" == "me")
print("you" < "me")
print("you" > "me")
print("you" != "me")

# 4)String length

print(len(str0))


# 5)Palindrome
def isPalindrome(str3):
    return str3 == str3[::-1]


str3 = "malayalam"
ans = isPalindrome(str3)

if ans:
    print("Yes")
else:
    print("No")

# 6)Case change
print(str0.lower())
print(str1.lower())
print(str2.lower())
print(str0.upper())
print(str1.upper())
print(str2.upper())


"""
# OUTPUT:

tHe trUTh Is tHat i Am IrOnMan
tHe trUTh Is tHat i Am IrOnMan
em WonK oUy
False
False
True
True
18
Yes
the truth is that 
i am ironman
em wonk ouy
THE TRUTH IS THAT 
I AM IRONMAN
EM WONK OUY

"""