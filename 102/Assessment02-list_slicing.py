# Naveen Maghbouleh
# CSCI 102 - Section E
# Assessment 02
# References: 
# Time: 15min
print('Enter your string:') 
fred = (input('STRING> ')) #User inputs string to be sliced
print('Enter four numbers to slice the string')
first = int(input('A> ')) + 1 #Inputs start of first slice
second = int(input('B> ')) #Inputs the end of first slice
third = int(input('C> ')) + 1 #inputs the start of second slice
fourth = int(input('D> ')) #inputs the end of second slice
print('OUTPUT',fred[first:second], fred[third:fourth]) #uses an f string to slice the string to the required output