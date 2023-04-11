# Naveen Maghbouleh
# CSCI 102 - Section E
# Assessment 07
# References:ZYBOOKS ch 19
# Time: 1 hr


checkerboard = [] #initialize list get inputs
collumns = int(input())
rows = int(input())
firstnum = input()
secondnum = input()
num = 0

for i in range(rows): #create the necessary ammt of rows
    checkerboard.append([])

if collumns % 2 == 0: #if collums are even 
    for l in range(rows):
        while num <= (collumns - 1 + l):
            if num % 2 == 0: 
                checkerboard[l].append(firstnum) #add first num then second num
                num += 1
            else:
                checkerboard[l].append(secondnum)
                num += 1
        num = l + 1

else: #for odd collumns
    for l in range(rows):
        while num <= (collumns - 1 + l):
            if num % 2 == 0: 
                checkerboard[l].append(firstnum)
                num += 1
            else:
                checkerboard[l].append(secondnum)
                num += 1
        num = l + 1

for n in range(rows): #print each row individually
    print('OUTPUT', checkerboard[n])

print('OUTPUT', checkerboard)