"""
Practical 3
Roll no. : 570
Name : Sarthak Turkar
Batch : E3
Problem statement : Write a Python program to print different patterns.
Date : 14/6/21
"""
# Input:

row = int(input("Enter the number of rows: "))                 # taking input from user for number of rows

# complex diamond

for o in range(3 * row + 2):
    print(" ", end='')
print("* ", end='')
print()
for i in range(row):                         # for the upper part of diamond
    for k in range(-3 * row, -3 * i):
        print(" ", end='')
    for j in range(i + 1):
        print("* ", end='')
    for j in range(i + 1):
        print("# ", end='')
    for j in range(i + 1):
        print("* ", end='')
    print()
for l in range(row - 1):                     # for the lower part of diamond
    for n in range(-6, 3 * l):
        print(" ", end='')
    for m in range(row - 1 - l):
        print("* ", end='')
    for m in range(row - 1 - l):
        print("# ", end='')
    for m in range(row - 1 - l):
        print("* ", end='')
    print()
for o in range(3 * row + 2):
    print(" ", end='')
print("* ", end='')
print()

# diamond

for i in range(row):                           # for the upper part of diamond
    for k in range(-row, -i):
        print(" ", end='')
    for j in range(i + 1):
        print("# ", end='')
    print()
for l in range(row - 1):                       # for the lower part of diamond
    for n in range(-2, l):
        print(" ", end='')
    for m in range(row - 1 - l):
        print("# ", end='')
    print()

# numbers pyramid

for i in range(row):                            # for the upper part of pyramid
    for k in range(-row, -i):
        print(" ", end='')
    for j in range(i + 1):
        print(j + 1, " ", end='')
    print()
for l in range(row - 1):                        # for the lower part of pyramid
    for n in range(-2, l):
        print(" ", end='')
    for m in range(row - 1 - l):
        print(m + 1, " ", end='')
    print()

# new number pyramid

for i in range(row):                            # for the upper part of pyramid
    for k in range(-row, -i):
        print(" ", end='')
    for j in range(i + 1):
        print(i + 1, " ", end='')
    print()
for l in range(row - 1):                          # for the lower part of pyramid
    for n in range(-2, l):
        print(" ", end='')
    for m in range(row - 1 - l):
        print(row - l - 1, " ", end='')
    print()

'''
OUTPUT:

Enter the number of rows: 5
                 * 
               * # * 
            * * # # * * 
         * * * # # # * * * 
      * * * * # # # # * * * * 
   * * * * * # # # # # * * * * * 
      * * * * # # # # * * * * 
         * * * # # # * * * 
            * * # # * * 
               * # * 
                 * 
     # 
    # # 
   # # # 
  # # # # 
 # # # # # 
  # # # # 
   # # # 
    # # 
     # 
     1  
    1  2  
   1  2  3  
  1  2  3  4  
 1  2  3  4  5  
  1  2  3  4  
   1  2  3  
    1  2  
     1  
     1  
    2  2  
   3  3  3  
  4  4  4  4  
 5  5  5  5  5  
  4  4  4  4  
   3  3  3  
    2  2  
     1  

Process finished with exit code 0
'''