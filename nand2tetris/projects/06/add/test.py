import numpy as np

def checkInt(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

dest = ''
comp = ''
jump = ''
# with open('Add_noBS.asm', 'r') as f:
#     # f_contents = f.read()
#     # print(f_contents)
#
#     for lines in f:
#         for words in lines:

# bin_dig = np.zeros(15)
# n = bin(3004)
# n = np.array(list(n[2:]), dtype=int)
# size_bin = int(np.shape(n)[0])
#
# print(size_bin)
#
# for b in reversed(range(size_bin)):
#     bin_dig[b] = n[b]

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

# for symbols in symbTable:
#     if symbols[0] == 'R1':
#         print (symbols[:][1])
# print (np.vstack((symbTable, ['symbol', 16])))
# symbTable = np.vstack((symbTable, ['symbol', 16]))
# print(symbTable)

# print(symbTable[1:-3])

# with open('Add_noBS.asm', 'w') as fo:
#     with open('Add.asm', 'r') as f:
#         for lines in f:
#             if (not lines[0] == '/') and (not lines.isspace()):
#                 fo.write(lines)
#

