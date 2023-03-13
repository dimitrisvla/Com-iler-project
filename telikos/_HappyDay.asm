.data
str_nl: .asciz "\n"
.text
j Lmain
L0: 
Lmain:
addi sp, sp, 28
mv gp, sp
L1: 
li a0, 0
li a7, 93
ecall
L2: 
