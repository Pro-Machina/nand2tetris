import el_gates as ga
import bit16_gates as ga16
import numpy as np

zero8 = np.zeros(8)
zero16 = np.zeros(16)

def Or8Way (in1 = zero8):
    # out = in1[0]
    # bit_no = np.shape(in1)[0]
    # for bits in range(bit_no-1):
    #     out = ga.Or(out, in1[bits+1])
    t0 = ga.Or(in1[0], in1[1])
    t1 = ga.Or(in1[2], t0)
    t2 = ga.Or(in1[3], t1)
    t3 = ga.Or(in1[4], t2)
    t4 = ga.Or(in1[5], t3)
    t5 = ga.Or(in1[6], t4)
    out = ga.Or(in1[7], t5)
    return out

def Mux4Way16 (in1 = zero16, in2 = zero16, in3 = zero16, in4 = zero16, sel = np.zeros(2)):
    o1 = ga16.Mux16(in1, in2, sel[1])
    o2 = ga16.Mux16(in3, in4, sel[1])
    out = ga16.Mux16(o1, o2, sel[0])
    return out
    
def Mux8Way16 (in1 = zero16, in2 = zero16, in3 = zero16, in4 = zero16, in5 = zero16, in6 = zero16, in7 = zero16, in8 = zero16, sel = np.zeros(3)):
    s11 = ga16.Mux16(in1, in2, sel[2])
    s12 = ga16.Mux16(in3, in4, sel[2])
    s13 = ga16.Mux16(in5, in6, sel[2])
    s14 = ga16.Mux16(in7, in8, sel[2])
    s21 = ga16.Mux16(s11, s12, sel[1])
    s22 = ga16.Mux16(s13, s14, sel[1])
    out = ga16.Mux16(s21, s22, sel[0])
    return out

def DMux4Way (in1 = 0, sel = np.zeros(2)):
    [o1, o2] = ga.DMux(in1, sel[1])
    [a, c] = ga.DMux(o1, sel[0])
    [b, d] = ga.DMux(o2, sel[0])
    return [a, b, c, d]

def DMux8Way (in1 = 0, sel = np.zeros(3)):
    [o11, o12] = ga.DMux(in1, sel[0])
    [o21, o22] = ga.DMux(o11, sel[1])
    [o23, o24] = ga.DMux(o12, sel[1])
    [a, b] = ga.DMux(o21, sel[2])
    [c, d] = ga.DMux(o22, sel[2])
    [e, f] = ga.DMux(o23, sel[2])
    [g, h] = ga.DMux(o24, sel[2])
    return [a, b, c, d, e, f, g, h]