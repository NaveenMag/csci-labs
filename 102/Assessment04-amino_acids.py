# Naveen Maghbouleh
# CSCI 102 - Section E
# Assessment 03
# References:
# Time: 15 minutes
carbon = int(input('CARBON> ')) #Asks for integer input of every variable for amino acids
hydrogen = int(input('HYDROGEN> '))
nitrogen = int(input('NITROGEN> '))
oxygen = int(input('OXYGEN> '))
sulfur = int(input('SULFER> '))
if carbon == 3 and hydrogen == 7 and nitrogen == 1 and oxygen == 2 and sulfur == 0: #Alanine
    print(f'OUTPUT {carbon}C--{hydrogen}H--{nitrogen}N--{oxygen}O--{sulfur}S')
    print('OUTPUT Alanine')
elif carbon == 6 and hydrogen == 14 and nitrogen == 4 and oxygen == 2 and sulfur == 0: #Arginine
    print(f'OUTPUT {carbon}C--{hydrogen}H--{nitrogen}N--{oxygen}O--{sulfur}S')
    print('OUTPUT Arginine')
elif carbon == 4 and hydrogen == 8 and nitrogen == 2 and oxygen == 3 and sulfur == 0: #Asparagine
    print(f'OUTPUT {carbon}C--{hydrogen}H--{nitrogen}N--{oxygen}O--{sulfur}S')
    print('OUTPUT Asparagine')
elif carbon == 3 and hydrogen == 7 and nitrogen == 1 and oxygen == 2 and sulfur == 1: #Cysteine
    print(f'OUTPUT {carbon}C--{hydrogen}H--{nitrogen}N--{oxygen}O--{sulfur}S')
    print('OUTPUT Cysteine')
elif carbon == 6 and hydrogen == 9 and nitrogen == 3 and oxygen == 2 and sulfur == 0: #Histidine
    print(f'OUTPUT {carbon}C--{hydrogen}H--{nitrogen}N--{oxygen}O--{sulfur}S')
    print('OUTPUT Histidine')
elif carbon == 5 and hydrogen == 10 and nitrogen == 2 and oxygen == 3 and sulfur == 0: #Glutamine
    print(f'OUTPUT {carbon}C--{hydrogen}H--{nitrogen}N--{oxygen}O--{sulfur}S')
    print('OUTPUT Glutamine')
else:
    print('Error the values you inputted do not resemble any amino acid')