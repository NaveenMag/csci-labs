#   Naveen Maghbouleh
#   ​CSCI 101 – Section I
#   Python Assesment 3
#   References: 
#   Time: 1 hr 30 mins

import string
prideopen = open('Pride&Prejudice_Ch1&2.txt', 'r')
words = prideopen.read() #open and read the file

punctuations = string.punctuation #gatther possible punctuations

fixedlist = [] #Lists to store future words
uniquelist = []

tally = 0 #tally for the number of specific words in the file

for char in words: #remove punctuation from the word
    if char in punctuations:
        words = words.replace(char, '')

words = words.replace('-', ' ') #remove hyphens make everything lowercase and split into list
words = words.lower()        
words = words.split()

choice = int(input('Please choose between 1 or 2: ')) #input choice to choose between 1 or 2

if choice == 1: #if choice is 1
    searchword = input('Input search word> ').lower()
    for word in words: #look for input word in word list and add to tally
        if searchword == word:
            tally += 1
    print('OUTPUT', tally) #ouput tally

if choice == 2:
    wordlen = int(input('Input searched word length> ')) #for choice 2 it gathers words of input length and adds to list and tally
    for word in words:
        if wordlen == len(word) and word.isalpha(): 
            tally += 1
            fixedlist.append(word)
    print('OUTPUT', tally)
    
    for word in fixedlist:
        if word not in uniquelist: #filters list for unique words
            uniquelist.append(word)
    print('OUTPUT',len(uniquelist)) #output number of unique words
  

prideopen.close()  #close the file