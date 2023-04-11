# Naveen Maghbouleh
# CSCI 102 - Section E
# Assessment 03
# References: 
# Time: 30min
operand_one = 0.0
operand_two = 0.0 #these are the vairables
sum = 0.0
difference = 0.0
product = 0.0
quotient = 0.0
remainder = 0.0
operand_one = float(input('Input first operand here> '))
operand_two = float(input('Input second operand here> '))
print ('Choose one of the following operations:\n1 - addition\n2 - subtraction\n3 - multiplication\n4 - division')
todo = int(input('> '))
if todo == 1:
    sum = operand_one + operand_two
    print(f'The result of the subtraction is: {sum:.6}')
    print(f'OUTPUT {sum:.6f}')
elif todo == 2:
    difference = operand_one - operand_two
    print(f'The result of the subtraction is: {difference:.6f}')
    print(f'OUTPUT {difference:.6f}')
elif todo == 3:
    product = operand_one * operand_two
    print(f'The result of the multiplication is: {product:.6f}')
    print(f'OUTPUT {product:.6f}')
elif todo == 4:
    quotient = operand_one // operand_two
    remainder = operand_one % operand_two
    print(f'The result of the division is: {quotient:.0f} (quotient) and {remainder:.0f} (remainder)')
    print(f'OUTPUT {quotient:.0f}')
    print(f'OUTPUT {remainder:.0f}')
else:
    print('ERROR')
print('Thanks for using this calculator.')