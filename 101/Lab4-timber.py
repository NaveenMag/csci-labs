#   Naveen Maghbouleh
#   ​CSCI 101 – Section I
#   Python Lab 4 
#   References: 
#   Time: 30 mins

years = int(input())
rate = float(input()) / 100 #input rate as raw number from percentage
acres = int(input())
acresmax = acres #used later
print(f'OUTPUT {0}, {acres:.1f}, {acres / 200:.2f}%') #initial value
for i in range(years):
    acres = (acres * (1+rate)) #for loop that gives every value we need
    print(f'OUTPUT {i+1}, {acres:.1f}, {acres / 200:.2f}%')
j = 0
while j > -1:
    acresmax = acresmax * (1 + rate) #gives max time
    j += 1
    if acresmax >= 20000:
        print(f'OUTPUT', j)
        break