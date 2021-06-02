def symbolTable(file):
    for lines in file:
        if 


with open('Add.asm', 'r') as f:
    # f_contents = f.read()
    # print(f_contents)

    for line in f:
        if line[0] == '@':
            char = line
            print(line, end='')

print(char[1:])