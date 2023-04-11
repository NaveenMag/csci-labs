# Naveen Maghbouleh
# CSCI 102 - Section E
# Assessment 08
# References:
# Time: 15 min

import random #this program will generate a random dice roll based on the number of sides and a seed and output how many of each value was hit

seedno = int(input('Enter the seed: ')) #inputting the sides, rolls and seed
rolls = int(input("How many rolls do you want? "))
sides = int(input("How many sides do you want? "))

history = []

random.seed(seedno) #seet the seed

for i in range(rolls): #create a list of the rolls

    roll = random.randint(1,sides)
    history.append(roll)

for l in range(sides): #search the list for each side and output how many times it was hit
    print('OUTPUT', l+1, 'occurred', history.count(l+1), 'times')
