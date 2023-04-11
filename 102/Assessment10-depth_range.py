# Naveen Maghbouleh
# CSCI 102 - Section E
# Assessment 09
# References: TA Nick Zybooks CSV
# Time: 1hr

import csv
with open('formations_parsed.csv', 'w',newline='') as parsed:
    csv_writer = csv.writer(parsed)
    with open('formations.csv', 'r') as formed:
        unimportant = next(formed)
        readformed = formed.readlines()
    
        csv_writer.writerow(['Depth','Start Depth','End Depth','Difference in Depth','Formation','Age of Formation'])
        for row in readformed:
            mountainlist = row.split(',')
            depth = mountainlist[0].split('-')
            depthchange = float(depth[1])-float(depth[0])
            mountainlist[1] = mountainlist[1].replace('\n','')
           
            
            if float(depth[0]) < 700:
                list_1 = [mountainlist[0],float(depth[0]),float(depth[1]),f'{depthchange:.2f}',mountainlist[1],'Paleocene']
                csv_writer.writerow(list_1)
            if float(depth[0]) >= 700:
                list_1 = [mountainlist[0],float(depth[0]),float(depth[1]),f'{depthchange:.2f}',mountainlist[1],'Cretaceous']
                csv_writer.writerow(list_1)
                