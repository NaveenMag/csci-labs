
def load_file(filename):
    with open(filename, 'r') as file:
        readfile = file.read().splitlines()
        return readfile
def update_string(string1,string2,integer):
    return f'{string1[0:integer]}{string2}{string1[integer + 1:]}'
def find_word_count(list,wordsearch):
    numword = 0
    for search in list:
        search = search.split()
        numword += search.count(wordsearch)
    return numword
def score_finder(listplayer,listscore,playername):
    if playername.title() in listplayer:
        playername = playername.title()
        playerloc = listplayer.index(playername)
        print(f'OUTPUT {listplayer[playerloc]} got a score of {listscore[playerloc]}')
    else:
        print(f'OUTPUT player not found')
def union(listuno,listdos):
    listuno = listuno + listdos
    return listuno
def intersect(list1,list2):
    goodlist = []
    for name in list1:
        if name in list2:
            goodlist.append(name)
    return goodlist
