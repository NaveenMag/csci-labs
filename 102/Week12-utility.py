
def load_file(filename):
    with open(filename, 'r') as file:
        readfile = file.read().splitlines()
        return readfile
def update_string(string1,string2,integer):
    return f'{string1[0:integer]}{string2}{string1[integer + 1:]}'
