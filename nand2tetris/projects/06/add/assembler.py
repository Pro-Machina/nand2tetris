import numpy as np

bin_15 = np.zeros(15)
bin_16 = np.zeros(16)

symbTable = np.zeros((23, 2), dtype='object')
for r in range(7, 23):
    symbTable[r][0] = 'R' + str(r-7)
    symbTable[r][1] = r-7
symbTable[0][0] = 'SCREEN'
symbTable[0][1] = 16384
symbTable[1][0] = 'KBD'
symbTable[1][1] = 24576
symbTable[2][0] = 'SP'
symbTable[2][1] = 0
symbTable[3][0] = 'LCL'
symbTable[3][1] = 1
symbTable[4][0] = 'ARG'
symbTable[4][1] = 2
symbTable[5][0] = 'THIS'
symbTable[5][1] = 3
symbTable[6][0] = 'THAT'
symbTable[6][1] = 4


def int2bin (n, bin_dig):
    """ Inputs a number and outputs binary number with bin_dig numbers """

    bin_dig = np.zeros(bin_dig)
    n = bin(n)
    n = np.array(list(n), dtype=int)
    size_bin = int(np.shape(n)[0])

    for b in reversed(range(size_bin)):
        bin_dig[b] = n[b]
    return bin_dig[::-1]

def checkInt(n):
    """ To check if the string can be converted to int type """

    try:
        int(n)
        return True
    except ValueError:
        return False

def Ainstruction (bin_num):
    """ Returns 16 bit array with A instruction syntax """

    bin_num = bin_num[::-1]
    np.append(bin_num, 0)
    return bin_num[::-1]

def addSym (symbol, type = '@', line_num = 0, table = symbTable):
    """ Adds the symbol to the table if not already added """

    symbol = symbol.strip('\n')
    size = np.shape(table)
    table_row = int(size[0])
    table_col = int(size[1])

    flag_exist = 0
    for row in range(table_row):
        if table[row][0] == symbol:
            flag_exist = 1

    if not flag_exist:
        if type == '@':
            address_nxt = int(table[table_row-1][1]) + 1
            stack_symb = np.array([str(symbol), int(address_nxt)], dtype='object')
            table = np.vstack((table, stack_symb))
            return table
        elif type == '(':
            address_nxt = line_num + 1
            stack_symb = np.array([str(symbol), int(address_nxt)], dtype='object')
            table = np.vstack((table, stack_symb))
            return table
    else:
        return table


with open('Add_noBS.asm', 'w') as fo:
    """ Removing comment lines and writing in fo """
    with open('Add.asm', 'r') as f:
        for lines in f:
            lines = lines.strip("   ")
            if (not lines[0] == '/') and (not lines.isspace()):
                fo.write(lines)

with open('Add_noBS.asm', 'r') as f:
    # f_contents = f.read()
    # print(f_contents)

    table_new = symbTable

    num = 0
    for lines in f:
        num += 1
        if lines[0] == '@':
            if not checkInt(lines[1:]):
                table_new = addSym(lines[1:], type = '@', line_num = 0, table = table_new)
        elif lines[0] == '(':
            table_new = addSym(lines[1:-2], type='(', line_num=num, table=table_new)

print(table_new)