# Naveen Maghbouleh
# CSCI 102 - Section E
# Assessment 11
# References: 
# Time: 1hr 10 mins

import math
def print_output(print_input): #print function
    print('OUTPUT', print_input)

def cylinder_vol(radius,height): #Calculate volume of cylinder using pi*r^2 * height
    volume = 3.1415 * radius ** 2 * height
    print_output(f'{volume:.2f}')

def lbs_to_kg(lbs): #use conversion facyor .4536 lbs/kg to convert lbs to kg
    kgs = lbs * .4536
    print_output(f'{kgs:.4f}')

def polar_coords(xval,yval): #use a^2 + b^2 = c ^2 to get radius and arctan(xval,yval) to get angle
    radius = (xval ** 2 + yval ** 2) ** (1/2)
    theta = math.degrees((math.atan(yval/xval)))
    print_output(f'r: {radius:.2f}')
    print_output(f'theta: {theta:.2f}')

def yen_to_dollars(yen): #convert yen to usd using cocnversion factor .0068 usd / yen
    dollars =yen * .0068
    print_output(f'{dollars:.2f}')

def quad_form(aval,bval,cval): #use the quadratic formula to find the solution.
    pos1 = (-bval - math.sqrt(bval **2 - 4 * aval*cval))/2
    pos2 = (-bval + math.sqrt(bval **2 - 4 * aval*cval))/2
    print_output(f'{pos1:.0f}')
    print_output(f'{pos2:.0f}')
