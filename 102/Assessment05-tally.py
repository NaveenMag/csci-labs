# Naveen Maghbouleh
# CSCI 102 - Section E
# Assessment 05
# References:
# Time: 15 minutes
in_num  =str(input('NUMBER> ')) #input first number and initialize the sum and ammount of nums
sum_num = 0
i = 0
while in_num != 'quit': #checks for quit
    sum_num = sum_num + int(in_num) #converts the string to int and adds a tally to the numbers added while requesting new input
    i += 1
    in_num  =str(input('NUMBER> '))
print('The addition of the 4 numbers entered is:')
print('OUTPUT', i, 'numbers')
print('OUTPUT', sum_num, 'total')