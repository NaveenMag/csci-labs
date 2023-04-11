
#   Naveen Maghbouleh
        #   CSCI 101 – Section I
        #   Python Assessment 2
        #   References: Reccomended Zybooks
        #   Time: 60 minutes 

operation = int(input('Please enter either 1 or two. 1 for Bin to Dec and 2 for Dec to Bin'))
if operation == 1:
    binarynum = []
    binstr = str(input())
    bin_len = len(binstr)
    value = 0
    sumd = 0
    while value < bin_len:
        if binstr[bin_len-1-value] == '1':
            sumd = sumd + 2**value
            value = value + 1
        else:
            value = value + 1    
    if ('2' in binstr or '3' in binstr or '4' in binstr or '5' in binstr or '6' in binstr or '7' in binstr or '8' in binstr or '9' in binstr or '-' in binstr or 'A' in binstr):
            print('ERROR: Input is not a binary number.')
            print('OUTPUT ERROR')
    else:
        print('OUTPUT', sumd)
elif operation == 2:
    decimal = input()
    binarynum = 0
    binlist = []
    if decimal.isdigit() == False:
        print('OUTPUT ERROR')
    else:
        decint = int(decimal)
        if decint == 0:
            print('OUTPUT 0')
        else:
            print('OUTPUT', end=' ')
            while decint >= 1:
                
                binlist.append(str(decint % 2))
                #print(decint % 2, end='')
                decint = decint // 2
            
            binlist.reverse()
            binlist = ''.join(binlist)
            print(binlist)
                

