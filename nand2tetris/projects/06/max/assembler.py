import numpy as np
import pandas as pa

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

def bin2string (arr):
    """ Converts the binary number array 'arr' to string format """

    bin_string = ''
    for bits in arr:
        bin_string += str(int(bits))
    return bin_string

def int2bin (n, bin_dig):
    """ Inputs a number and outputs binary number with bin_dig numbers """

    req_size_arr = np.zeros(bin_dig)
    n = bin(n)
    n = np.array(list(n[2:]), dtype=int)
    size_bin = int(np.shape(n)[0])

    # for b in reversed(range(size_bin)):
    #     bin_dig[b] = n[b]
    #     print(bin_dig, n)

    while size_bin > 0:
        size_bin -= 1
        bin_dig -= 1
        req_size_arr[bin_dig] = n[size_bin]
    return req_size_arr

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
    bin_num = np.append(bin_num, 0)
    return bin_num[::-1]

# def Cinstruction (bin_str):
#     """ Returns string of binary numbers for C instructions """
#
#     c_str = '111'
#     c_str += bin_str
#     return c_str

def addSym (symbol, type_start = '@', line_num = 0, table = symbTable):
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



## First iteration to remove comments, blank lines and indentations
with open('Add_noBS.asm', 'w') as fo:
    """ Removing comment lines and writing in fo """
    with open('Add.asm', 'r') as f:
        for lines in f:
            # lines = lines.strip("   ")
            lines = lines.replace(" ", "")
            if (not lines[0] == '/') and (not lines.isspace()):
                fo.write(lines)

## Second iteration to add symbols to symbol-table
with open('Add_noBS.asm', 'r') as f:

    symbol_table = symbTable

    num = 0
    for lines in f:
        num += 1
        if lines[0] == '@':
            if not checkInt(lines[1:]):
                symbol_table = addSym(lines[1:], type_start = '@', line_num = 0, table = symbol_table)
        elif lines[0] == '(':
            symbol_table = addSym(lines[1:-2], type_start='(', line_num=num, table=symbol_table)

with open('Add_noBS.asm', 'r') as f:

    # Opening Instruction to Binary conversion table using pandas
    conversion = pa.read_excel('Instructions.xlsx')
    conversion = np.array(conversion)
    conv_row = int(np.shape(conversion)[0])
    conv_col = int(np.shape(conversion)[1])
    # print(conversion)

    num = 0
    str_arr = np.empty(9999999, dtype='object')
    for lines in f:
        num += 1
        dest = ''
        comp = ''
        jump = ''
        if lines[0] == '@': # A Instruction
            if checkInt(lines[1:]):
                bit = int2bin(int(lines[1:]), 15)
                bit = Ainstruction(bit)
                str_arr[num-1] = bin2string(bit)
            else:
                for symbols in symbol_table:
                    if lines[1:].strip('\n') == symbols[0].strip('\n'):
                        bit = int2bin(int(symbols[:][1]), 15)
                        bit = Ainstruction(bit)
                        str_arr[num-1] = bin2string(bit)

        elif lines[0] == '(': # A Instruction
            if checkInt(lines[1:-2]):
                bit = int2bin(int(lines[1:-2]), 15)
                bit = Ainstruction(bit)
                str_arr[num-1] = bin2string(bit)
            else:
                for symbols in symbol_table:
                    if lines[1:-2].strip('\n') == symbols[0].strip('\n'):
                        bit = int2bin(int(symbols[:][1]), 15)
                        bit = Ainstruction(bit)
                        str_arr[num-1] = bin2string(bit)

        else:
            lines.strip('\n')
            eq = 0
            semico = 0
            line_size = len(lines)
            w = 0
            while w < line_size:
                if not lines[w] == '=':
                    dest += lines[w]
                else:
                    eq = w + 1
                    break
                w += 1
            while (eq < line_size) and (eq > 0):
                if not lines[eq] == ';':
                    comp += lines[eq]
                else:
                    semico = eq + 1
                    break
                eq += 1
            while (semico < line_size) and (semico > 0):
                jump += lines[semico]
                semico += 1
            dest = dest.strip('\n')
            comp = comp.strip('\n')
            jump = jump.strip('\n')

            # For comp instructions
            str_arr[num - 1] = '111'
            comp_col = 0
            for cc in range(conv_col):
                if conversion[0][cc] == 'comp':
                    comp_col = cc

            a = '0'
            if not comp == '':
                for rc in range(conv_row):
                    if comp == conversion[rc][comp_col]:
                        str_arr[num-1] += a
                        str_arr[num-1] += conversion[rc][comp_col+2]
                    elif comp == conversion[rc][comp_col+1]:
                        a = '1'
                        str_arr[num-1] += a
                        str_arr[num-1] += conversion[rc][comp_col + 2]
            else:
                str_arr[num-1] += '000'

            # For dest instructions
            dest_col = 0
            for cd in range(conv_col):
                if conversion[0][cd] == 'dest':
                    dest_col = cd
            for rd in range(conv_row):
                if conversion[rd][dest_col] == dest:
                    str_arr[num-1] += conversion[rd][dest_col+1]


            # For jump instructions
            jump_col = 0
            for cj in range(conv_col):
                if conversion[0][cj] == 'jump':
                    jump_col = cj
            if not jump == '':
                for rj in range(conv_row):
                    if jump == conversion[rj][jump_col]:
                        str_arr[num-1] += conversion[rj][jump_col+1]
            else:
                str_arr[num-1] += '000'


    out_arr = str_arr[:num]
    with open('Add.hack', 'w') as write:
        for binary in out_arr:
            print(binary)
            write.write(binary + '\n')


