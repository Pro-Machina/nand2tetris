import el_gates as ga
import numpy as np

zero16 = np.zeros(16)

def Not16 (in1 = zero16):
    output = zero16
    # for bits in range(in1):
    #     output[bits] = ga.Not(in1[bits])
    output[0] = ga.Not(in1[0])
    output[1] = ga.Not(in1[1])
    output[2] = ga.Not(in1[2])
    output[3] = ga.Not(in1[3])
    output[4] = ga.Not(in1[4])
    output[5] = ga.Not(in1[5])
    output[6] = ga.Not(in1[6])
    output[7] = ga.Not(in1[7])
    output[8] = ga.Not(in1[8])
    output[9] = ga.Not(in1[9])
    output[10] = ga.Not(in1[10])
    output[11] = ga.Not(in1[11])
    output[12] = ga.Not(in1[12])
    output[13] = ga.Not(in1[13])
    output[14] = ga.Not(in1[14])
    output[15] = ga.Not(in1[15])
    return output

def And16 (in1 = zero16, in2 = zero16):
    output = zero16
    # for bits in range(in1):
    #     output[bits] = ga.And(in1[bits], in2[bits])
    output[0] = ga.And(in1[0], in2[0])
    output[1] = ga.And(in1[0], in2[1])
    output[2] = ga.And(in1[2], in2[2])
    output[3] = ga.And(in1[3], in2[3])
    output[4] = ga.And(in1[4], in2[4])
    output[5] = ga.And(in1[5], in2[5])
    output[6] = ga.And(in1[6], in2[6])
    output[7] = ga.And(in1[7], in2[7])
    output[8] = ga.And(in1[8], in2[8])
    output[9] = ga.And(in1[9], in2[9])
    output[10] = ga.And(in1[10], in2[10])
    output[11] = ga.And(in1[11], in2[11])
    output[12] = ga.And(in1[12], in2[12])
    output[13] = ga.And(in1[13], in2[13])
    output[14] = ga.And(in1[14], in2[14])
    output[15] = ga.And(in1[15], in2[15])
    return output

def Or16 (in1 = zero16, in2 = zero16):
    output = zero16
    # for bits in range(in1):
    #     output[bits] = ga.Or(in1[bits], in2[bits])
    output[0] = ga.Or(in1[0], in2[0])
    output[1] = ga.Or(in1[1], in2[1])
    output[2] = ga.Or(in1[2], in2[2])
    output[3] = ga.Or(in1[3], in2[3])
    output[4] = ga.Or(in1[4], in2[4])
    output[5] = ga.Or(in1[5], in2[5])
    output[6] = ga.Or(in1[6], in2[6])
    output[7] = ga.Or(in1[7], in2[7])
    output[8] = ga.Or(in1[8], in2[8])
    output[9] = ga.Or(in1[9], in2[9])
    output[10] = ga.Or(in1[10], in2[10])
    output[11] = ga.Or(in1[11], in2[11])
    output[12] = ga.Or(in1[12], in2[12])
    output[13] = ga.Or(in1[13], in2[13])
    output[14] = ga.Or(in1[14], in2[14])
    output[15] = ga.Or(in1[15], in2[15])
    return output

def Mux16 (in1 = zero16, in2 = zero16, sel = 0):
    output = zero16
    # for bits in range(in1):
    #     output[bits] = ga.Mux(in1[bits], in2[bits], sel)
    output[0] = ga.Mux(in1[0], in2[0], sel)
    output[1] = ga.Mux(in1[1], in2[1], sel)
    output[2] = ga.Mux(in1[2], in2[2], sel)
    output[3] = ga.Mux(in1[3], in2[3], sel)
    output[4] = ga.Mux(in1[4], in2[4], sel)
    output[5] = ga.Mux(in1[5], in2[5], sel)
    output[6] = ga.Mux(in1[6], in2[6], sel)
    output[7] = ga.Mux(in1[7], in2[7], sel)
    output[8] = ga.Mux(in1[8], in2[8], sel)
    output[9] = ga.Mux(in1[9], in2[9], sel)
    output[10] = ga.Mux(in1[10], in2[10], sel)
    output[11] = ga.Mux(in1[11], in2[11], sel)
    output[12] = ga.Mux(in1[12], in2[12], sel)
    output[13] = ga.Mux(in1[13], in2[13], sel)
    output[14] = ga.Mux(in1[14], in2[14], sel)
    output[15] = ga.Mux(in1[15], in2[15], sel)
    return output
