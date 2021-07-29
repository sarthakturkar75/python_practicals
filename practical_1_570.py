# Practical 1
# Roll no.: 570
# Name : Sarthak Turkar
# Batch : E3
# Problem statements : To accept an object mass in kilograms and velocity in meters per second and display its momentum. Momentum is calculated as e=mc2 where m is the mass of the object and c is its velocity.
# Date : 27/05/2021

# Code :

m = int(input("Enter the mass of object in kg = "))  # taking input of mass
c = int(input("Enter the velocity of object in m/s = "))  # taking input of velocity
print("Mass of object in kg = {0} \nVelocity of object in m/s = {1}".format(m,c))  # printing the values of mass and velocity taken by the user
e = m * c * c  # calculating momentum
print("The momentum of object in kg.m^2/s^2 is =", e)  # printing the value of momentum calculated
# Output :

# Enter the mass of object in kg = 34
# Enter the velocity of object in m/s = 5
# Mass of object in kg = 34
# Velocity of object in m/s = 5
# The momentum of object in kg.m^2/s^2 is = 850

# Process finished with exit code 0
