#   Naveen Maghbouleh
#   ​CSCI 101 – Section I
#   Python Lab 2 
#   References: ZYBOOKS  20.1
#   Time: 45 minutes
string1 = input('LIST1> ')
string2 = input('LIST2> ')
string3 = input('LIST3> ')
string4 = input('LIST4> ')
string5 = input('LIST5> ')
string_1_fix = len(string1) -2
string_1_fix2 = len(string1)
string2_fix = len(string2) -2
string3_fix = int((len(string3)) /2)
string3_fix2 = len(string3)
string4_fix = string4[2]
string4_fix2 = string4[4]
string5_fix = string5[0:2]
string5_fix2 = string5[2:]
#print(string3[string3_fix:])
#print(f'{string1[string_1_fix:string_1_fix2]}{string1[0:string_1_fix]}')
#print(string2[0:string2_fix])
#print(string3[string3_fix:string3_fix2])
#print(f'{string4[0:2]}{string4_fix2}{string4[3:4]}{string4_fix}{string4[5:]}')
print('The encrypted message is:')
print(f'OUTPUT {string5_fix} {string1[string_1_fix:string_1_fix2]}{string1[0:string_1_fix]}{string2[0:string2_fix]}{string3[string3_fix:]}{string4[0:2]}{string4_fix2}{string4[3:4]}{string4_fix}{string4[5:]} {string5_fix2}')