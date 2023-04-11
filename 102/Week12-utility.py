def load_file(filename):
    with open(filename, 'r') as file:
        readfile = file.readlines()
        return readfile
