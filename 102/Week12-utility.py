import math
# Naveen Maghbouleh
# CSCI 102 - Section E
# Assessment 12
# References: 
# Time: 1hr 15 mins

def load_file(filename): #opens file and reads each line and sets as list
    with open(filename, 'r') as file:
        readfile = file.read().splitlines()
        return readfile


def update_string(string1,string2,integer): #large f string that formats the string properly
    return f'{string1[0:integer]}{string2}{string1[integer + 1:]}'


def find_word_count(list2,wordsearch): #creates a list of split words and then tallys each match
    numword = 0
    for search in list2:
        search = search.split()
        numword += search.count(wordsearch)
    return numword

def score_finder(listplayer,listscore,playername): #Makes the input a name and then matches the index
    if playername.title() in listplayer:
        playername = playername.title()
        playerloc = listplayer.index(playername)
        print(f'OUTPUT {listplayer[playerloc]} got a score of {listscore[playerloc]}')
    else:
        print(f'OUTPUT player not found') #not found condition


def union(listuno,listdos): #simple list addition
    listuno = listuno + listdos
    return listuno


def intersect(list1,list2): #appends matching names and adds to the list
    goodlist = []
    for name in list1:
        if name in list2:
            goodlist.append(name)
    return goodlist


def not_in(list1,list2): #same thing but instead it checks if the name is not in the list
    goodlist = []
    for name in list1:
        if name not in list2:
            goodlist.append(name)
    return goodlist


def is_prime(number): #searches the prime numbers
    if number == 1:
        return False
    else:
        for num in range(2, int(math.sqrt(number))+1):
            if number%num == 0:
                return False
        return True

    