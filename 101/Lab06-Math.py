#Jasper Taylor, Naveen Maghbouleh
#CSCI 101 Section C, Section I
#references - Samvat Dangol Sec C suggested use of for loops and file i/o
#Time 2 hrs


import csv

original_file = input("MATHFILE> ") #inputs file names
new_file = input("OUTPUTFILE> ")

left_side = [] #initialize use lists
right_side = []

left_total = []
right_total = []


#Opening original file and creating the new_file
with open(original_file, mode = 'r') as file: 
    reader = csv.reader(file)
    with open(new_file, mode = 'w') as second_file:
        writer = csv.writer(second_file, delimiter = ',')

        for line in reader: #reset left and right sides list and split depending on == index
            left_side = []
            right_side = []
            index = line.index("==")
            for i in line[:index]:
                left_side.append(i)
            for i in line[index + 1 :]: 
                right_side.append(i)
            total = int(left_side[0])
            
            
            for i in range(len(left_side)): # left side calculation depending on operation
                if left_side[i] == "*":
                    total = total * int(left_side[i+1])
                if left_side[i] == "/":
                    total = total / int(left_side[i+1])
                if left_side[i] == "-":
                    total = total - int(left_side[i+1])
                if left_side[i] == "+":
                    total = total + int(left_side[i+1])
                if left_side[i] == "%":
                    total = total % int(left_side[i+1])
                if left_side[i] == "**":
                    total = total ** int(left_side[i+1])
            total = round(total)
            left_total.append(total) #set value for left side of equation
            new_total = int(right_side[0])

            for i in range(len(right_side)): #right side calculation
                if right_side[i] == "*":
                    new_total = new_total * int(right_side[i+1])
                if right_side[i] == "/":
                    new_total = new_total / int(right_side[i+1])
                if right_side[i] == "-":
                    new_total = new_total - int(right_side[i+1])
                if right_side[i] == "+":
                    new_total = new_total + int(right_side[i+1])
                if right_side[i] == "%":
                    new_total = new_total % int(right_side[i+1])
                if right_side[i] == "**":
                    new_total = new_total ** int(right_side[i+1])
            new_total = round(new_total)
            right_total.append(new_total) #add right side total to list
            total_list = []
            
            for i in range(len(left_total)): #create a list with the right and left side value with the boolean if they are the same
                total_list.append(left_total[i])
                total_list.append(right_total[i])
                total_list.append(left_total[i] == right_total[i],)
                
                writer.writerow(total_list) #write the list to the new csv file and reset used lists
                print(total_list)
                total_list = []
                left_total = []
                right_total = []

