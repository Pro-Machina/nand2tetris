// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

    @i
    M = 1 // i = 1
    @R0
    D = M // D contains RAM[0] value
    @n
    M = D // n = RAM[0]
    @mult
    M = 0 // mult = 0

(LOOP)
    @i
    D = M // D contains value of i
    @n
    D = D - M // D contains (n - i)
    @STOP
    D;JGT // if (n - i) < 0 goto STOP

    @mult
    D = M // D has value of mult
    @R1
    D = D + M // RAM[1] has the value of succesive addition of mult
    @mult
    M = D // RAM[mult] = sum of values of mult
    @i
    M = M + 1 // i += 1
    @LOOP
    0;JMP

(STOP)
    @mult
    D = M 
    @R2
    M = D // RAM[2] has the value of multiplication

(END)
    @END
    0;JMP
