#   Naveen Maghbouleh
#   ​CSCI 101 – Section I
#   Python Lab 5
#   References: Zybooks list chapter, Ben Burghardt
#   Time: 3h 30 mins
rows = int(input('ROWS> ')) #inputs rows and columns
columns = int(input('COLUMNS> '))
teslaopolis = [] #two lists one to be saved and one to edit
teslaopolis2 = []
broken = [] #later list for unlit lights

for cell in range(rows): #adding the inputs as cells to the matrix of both
    teslaopolis.append([])
    teslaopolis2.append([])
    actual_row = (input(f'ROW{cell+1}> '))
    teslaopolis[cell] = actual_row.split( )
    teslaopolis2[cell] = actual_row.split( )


for cell in range(rows):
    for ceel in range(columns):
        if teslaopolis2[cell][ceel] == 'T' or teslaopolis2[cell][ceel] == 'S': #first ring around S and T
            if teslaopolis2[cell][max(ceel-1,0)] == 'b': #setting left and right to x if it was b
                teslaopolis2[cell][max(ceel-1,0)] = 'x'
            if teslaopolis2[cell][min(ceel+1,columns-1)] == 'b':
                teslaopolis2[cell][min(ceel+1,columns-1)] = 'x'
            
            if teslaopolis2[min(cell+1,rows-1)][ceel] == 'b': #setting the above to x if b 
                teslaopolis2[min(cell+1,rows-1)][ceel] = 'x'
            if teslaopolis2[min(cell+1,rows-1)][min(ceel+1,columns-1)] == 'b':
                teslaopolis2[min(cell+1,rows-1)][min(ceel+1,columns-1)] = 'x'
            if teslaopolis2[min(cell+1,rows-1)][max(ceel-1,0)] == 'b':
                teslaopolis2[min(cell+1,rows-1)][max(ceel-1,0)] = 'x'

            if teslaopolis2[max(cell-1,0)][ceel] == 'b': #setting below to x if b
                teslaopolis2[max(cell-1,0)][ceel] = 'x'
            if teslaopolis2[max(cell-1,0)][min(ceel+1,columns-1)] == 'b':
                teslaopolis2[max(cell-1,0)][min(ceel+1,columns-1)] = 'x'
            if teslaopolis2[max(cell-1,0)][max(ceel-1,0)] == 'b':
                teslaopolis2[max(cell-1,0)][max(ceel-1,0)] = 'x'
        
        if teslaopolis2[cell][ceel] == 'S': #second ring of S
            if teslaopolis2[min(cell+2,rows-1)][max(ceel-2,0)] == 'b': #2 up that entire row changing b to x
                teslaopolis2[min(cell+2,rows-1)][max(ceel-2,0)] = 'x'
            if teslaopolis2[min(cell+2,rows-1)][max(ceel-1,0)] == 'b':
                teslaopolis2[min(cell+2,rows-1)][max(ceel-1,0)] = 'x'
            if teslaopolis2[min(cell+2,rows-1)][ceel] == 'b':
                teslaopolis2[min(cell+2,rows-1)][ceel] = 'x'
            if teslaopolis2[min(cell+2,rows-1)][min(ceel+1,columns-1)] == 'b':
                teslaopolis2[min(cell+2,rows-1)][min(ceel+1,columns-1)] = 'x'
            if teslaopolis2[min(cell+2,rows-1)][min(ceel+2,columns-1)] == 'b':
                teslaopolis2[min(cell+2,rows-1)][min(ceel+2,columns-1)] = 'x'
            
            if teslaopolis2[max(cell-2,0)][max(ceel-2,0)] == 'b': #2 down that entire row changing b to x
                teslaopolis2[max(cell-2,0)][max(ceel-2,0)] = 'x'
            if teslaopolis2[max(cell-2,0)][max(ceel-1,0)] == 'b':
                teslaopolis2[max(cell-2,0)][max(ceel-1,0)] = 'x'
            if teslaopolis2[max(cell-2,0)][ceel] == 'b':
                teslaopolis2[max(cell-2,0)][ceel] = 'x'
            if teslaopolis2[max(cell-2,0)][min(ceel+1,columns-1)] == 'b':
                teslaopolis2[max(cell-2,0)][min(ceel+1,columns-1)] = 'x'
            if teslaopolis2[max(cell-2,0)][min(ceel+2,columns-1)] == 'b':
                teslaopolis2[max(cell-2,0)][min(ceel+2,columns-1)] = 'x'

            if teslaopolis2[max(cell-1,0)][max(ceel-2,0)] == 'b': #1 down the edge 2
                teslaopolis2[max(cell-1,0)][max(ceel-2,0)] = 'x'
            if teslaopolis2[max(cell-1,0)][min(ceel+2,columns-1)] == 'b':
                teslaopolis2[max(cell-1,0)][min(ceel+2,columns-1)] = 'x'

            if teslaopolis2[min(cell+1,rows-1)][max(ceel-2,0)] == 'b': #1 up the edge 2
                teslaopolis2[min(cell+1,rows-1)][max(ceel-2,0)] = 'x'
            if teslaopolis2[min(cell+1,rows-1)][min(ceel+2,columns-1)] == 'b':
                teslaopolis2[min(cell+1,rows-1)][min(ceel+2,columns-1)] = 'x'

            if teslaopolis2[cell][max(ceel-2,0)] == 'b': #the edge 2 on same level
                teslaopolis2[cell][max(ceel-2,0)] = 'x'
            if teslaopolis2[cell][min(ceel+2,columns-1)] == 'b':
                teslaopolis2[cell][min(ceel+2,columns-1)] = 'x'
for cell in range(rows):
    for ceel in range(columns): #record the unlit bulbs to broken list
        if teslaopolis2[cell][ceel] == 'b':
            broken.append([ cell, ceel])
broken.reverse 
if broken != []: #now if its broken print false and the broken list otherwise print true!
    print('OUTPUT False')
    print('OUTPUT', broken)
else:
    print('OUTPUT True')
