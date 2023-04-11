# Naveen Maghbouleh, Jeremy Cefus, Whitney Hulse
# CSCI 102 - Section E
# Assessment 09
# References:
# Time: 20 min
import random
wordlist = open('dictionary.txt', 'r') #open file

randseed = input("Enter a random seed: ") #get input from user for random seed and word length
wordlen = int(input("Enter a word length: "))

random.seed(randseed) #set random seed

words = wordlist.read().split() #create list of words from file

listlen = len(words) #get length of list

tally = 0 #initialize tally variable and list of words that match the wordlen
letterwords = []

for l in range(listlen): #loop through list of words for the correct wordlen. If correct wordlen, add to tally variable and list
    if len(words[l]) == wordlen:
        tally += 1
        letterwords.append(words[l])
    else:
        continue

if len(letterwords) == 0: #if list is empty
    print(f'There are no words of length {wordlen} in the dictionary')
    print('OUTPUT None')
else:
    print('OUTPUT', letterwords[random.randint(0,len(letterwords)-1)]) #print output of random word from correct list and tally
    print(f'A random word of length {wordlen} is {letterwords[random.randint(0,len(letterwords)-1)]}')
print('The number of words of length', wordlen, 'is', tally)
print('OUTPUT', tally)

wordlist.close() #close file