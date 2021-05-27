// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(ITERATE)  
    @SCREEN
    D = A
    @R0
    M = D // RAM[0] = SCREEN {adresss of where to start}

(CHECK)
    @KBD
    D = M
    @FILLWHITE
    D;JEQ
    @FILLBLACK
    D;JGT

    @CHECK
    0;JMP // Infinite loop that keeps on checking

(FILLWHITE)
    @R1
    M = 0 // What to print is stored in RAM[1]
    @PRINTSCREEN
    0;JMP

(FILLBLACK)
    @R1
    M = -1 // What to print is stored in RAM[1]
    @PRINTSCREEN
    0;JMP

(PRINTSCREEN)
    @R1
    D = M // D Contains Black or White
    
    @R0
    A = M // A has address where to fill
    M = D // Fill at address

    @R0
    D = M + 1 // Increase pixel by 1
    @KBD
    D = A - D // Till we reach KBD

    @R0
    M = M + 1
    A = M

    @PRINTSCREEN
    D;JGT // If current pixel is KBD whole screen is black

    @ITERATE
    0;JMP