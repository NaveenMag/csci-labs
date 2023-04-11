#   Naveen Maghbouleh
#   ​CSCI 101 – Section I
#   Python Lab 3 
#   References: 
#   Time: 1hr 15 mins
row1 = str(input('ROW1> '))
row2 = str(input('ROW2> '))
row3 = str(input('ROW3> '))
size1 = len(row1)
size2 = len(row2)
size3 = len(row3)
if row1[0] != 'X' and row1[0] != 'O' and row1[0] != 'E' and row1[1] != 'X' and row1[1] != 'O' and row1[1] != 'E' and row1[2] != 'X' and row1[2] != 'O' and row1[2] != 'E':
    print('OUTPUT ERROR')
elif row2[0] != 'X' and row2[0] != 'O' and row2[0] != 'E' and row2[1] != 'X' and row2[1] != 'O' and row2[1] != 'E' and row2[2] != 'X' and row2[2] != 'O' and row2[2] != 'E':
    print('OUTPUT ERROR')
elif row3[0] != 'X' and row3[0] != 'O' and row3[0] != 'E' and row3[1] != 'X' and row3[1] != 'O' and row3[1] != 'E' and row3[2] != 'X' and row3[2] != 'O' and row3[2] != 'E':
    print('OUTPUT ERROR')
elif size1 != 3:
    print('OUTPUT ERROR')
elif size2 != 3:
    print('OUTPUT ERROR')
elif size3 != 3:
    print('OUTPUT ERROR')
else:
    if row1 == 'XXX':
        print('OUTPUT X')
    elif row2 == 'XXX':
        print('OUTPUT X')
    elif row3 == 'XXX':
        print('OUTPUT X')
    elif row1 == 'OOO':
        print('OUTPUT O')
    elif row2 == 'OOO':
        print('OUTPUT O')
    elif row3 == 'OOO':
        print('OUTPUT O')
    elif row1[0] == 'X' and row2[1] == 'X' and row3[2] == 'X':
        print('OUTPUT X')
    elif row1[2] == 'X' and row2[1] == 'X' and row3[0] == 'X':
        print('OUTPUT X')
    elif row1[0] == 'O' and row2[1] == 'O' and row3[2] == 'O':
        print('OUTPUT O')
    elif row1[2] == 'O' and row2[1] == 'O' and row3[0] == 'O':
        print('OUTPUT O')
    elif row1[0] == 'X' and row2[0] == 'X' and row3[0] == 'X':
        print('OUTPUT X')
    elif row1[2] == 'X' and row2[2] == 'X' and row3[2] == 'X':
        print('OUTPUT X')
    elif row1[0] == 'O' and row2[0] == 'O' and row3[0] == 'O':
        print('OUTPUT O')
    elif row1[2] == 'O' and row2[2] == 'O' and row3[2] == 'O':
        print('OUTPUT O')
    elif row1[1] == 'O' and row2[1] == 'O' and row3[1] == 'O':
        print('OUTPUT O')
    else:
        print('OUTPUT T')
