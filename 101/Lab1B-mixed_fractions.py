#   Naveen Maghbouleh
#   CSCI 101 – Section I
#   Python Lab 1A
#   References: 
#   Time: 3:22 start
print('Input the numerator of the improper fraction.')
print('NUMERATOR> ', end='')
numerator = int(input())
print('Input the denominator of the improper fraction.')
print('DENOMINATOR> ', end='')
denominator = int(input())
total_num = numerator // denominator
extra_num = numerator % denominator
print(f'{numerator}/{denominator} as a mixed fraction is:')
print(f'OUTPUT {total_num} {extra_num}/{denominator}')
