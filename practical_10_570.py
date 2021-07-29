"""
Practical 10
Roll no. : 570
Name : Sarthak Turkar
Batch : E3
Problem statement : Choose cricket team of eleven players find the captain of the team (consider tallest person as a
captain) using dictionary)
        1. declare dict (read the dict values from the user)
        2. add elements - players key:value playername: height
        3. print complete list of players
        4. select captain based on heights
        5. print name of the captain
Date : 22/7/21
"""
# Input:

players = {}
x = 0
for i in range(11):
    name = input(f"Enter the name of player {i + 1} : ")
    height = int(input(f"Enter the height of {name} : "))
    players[name] = height
for p, q in players.items():
    x = x + 1
    print(x, ")", p, q, "cm")

maxi = max(players, key=players.get)
print(maxi, "is the team captain.")

"""

OUTPUT:

Enter the name of player 1 : Sainath
Enter the height of Sainath : 158
Enter the name of player 2 : Dipanshu
Enter the height of Dipanshu : 169
Enter the name of player 3 : Parimal
Enter the height of Parimal : 155
Enter the name of player 4 : Arya
Enter the height of Arya : 160
Enter the name of player 5 : Omkar
Enter the height of Omkar : 161
Enter the name of player 6 : Onkar
Enter the height of Onkar : 163
Enter the name of player 7 : Anas
Enter the height of Anas : 162
Enter the name of player 8 : Swaraj
Enter the height of Swaraj : 163
Enter the name of player 9 : Sarthak
Enter the height of Sarthak : 160
Enter the name of player 10 : Sanket
Enter the height of Sanket : 164
Enter the name of player 11 : Osho
Enter the height of Osho : 163
1 ) Sainath 158 cm
2 ) Dipanshu 169 cm
3 ) Parimal 155 cm
4 ) Arya 160 cm
5 ) Omkar 161 cm
6 ) Onkar 163 cm
7 ) Anas 162 cm
8 ) Swaraj 163 cm
9 ) Sarthak 160 cm
10 ) Sanket 164 cm
11 ) Osho 163 cm
Dipanshu is the team captain.

"""
