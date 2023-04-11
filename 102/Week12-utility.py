def load_file(filename):
    with open(filename, 'r') as file:
        readfile = file.read().splitlines()
        return readfile
lines = load_file('mother.txt')
print(lines)