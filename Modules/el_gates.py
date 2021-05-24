import Nand as na

def Not(in1 = 0):
    return na.Nand(in1, in1)

def And(in1 = 0, in2 = 0):
    return Not(na.Nand(in1, in2))

def Or(in1 = 0, in2 = 0):
    return na.Nand(Not(in1), Not(in2))

def Xor(in1 = 0, in2 = 0):
    return And(na.Nand(in1, in2), Or(in1, in2))

def Mux(in1 = 0, in2 = 0, sel = 0):
    nsel = Not(sel)
    sub1 = And(in1, nsel)
    sub2 = And(in2, sel)
    return Or(sub1, sub2)

"""
def DMux(in1 = 0, in2 = 0, sel = 0):
    sub1 = And(in1, in2)
    sub2 = Or(in1, in2)
    return Mux(sub1, sub2, sel)
"""

def DMux(in1 = 0, sel = 0):
    a = And(in1, Not(sel))
    b = And(in1, sel)
    return [a, b]