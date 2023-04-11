# Naveen Maghbouleh
# CSCI 102 - Section E
# Assessment 01B
# References: Jasper Taylor from Sec F helped me with the round function
# Time: 10 minutes
print('What is the total length of fencing available? (In yards).')
print('LENGTH> ', end='')
variable_length = int(input())
variable_ft = variable_length*3
print('The maximum rectangular area for my uncles farm (in ft^2) is:')
answer = (variable_ft/4) ** 2
print('OUTPUT' ,round(answer,1))