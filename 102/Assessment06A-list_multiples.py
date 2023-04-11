# Naveen Maghbouleh
# CSCI 102 - Section E
# Assessment 06
# References:
# Time: 15 minutes
multiple = int(input('NUMBER> ')) #two inputs for number and max int + 1
max_int = int(input('INDEX> ')) + 1
finlist = [] #first list
for i in range(max_int):
    finlist.append(i*multiple + multiple ) #adds each next multiple to the list
print('OUTPUT', finlist)
print('OUTPUT', multiple) #ouputs everything

