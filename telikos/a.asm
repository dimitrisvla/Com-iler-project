.data
str_nl: .asciz "\n"
.text
j Lmain
L0: 
Lmain:
addi sp, sp, 28
mv gp, sp
L1: 
li t1, 200
sw t1, -12(gp)
L2: 
li t1, 7
sw t1, -16(gp)
L3: 
lw t1, -12(gp)
lw t2, -16(gp)
mul t1, t1, t2
sw t1, -24(gp)
L4: 
lw t1, -24(gp)
sw t1, -20(gp)
L5: 
li a0, 0
li a7, 93
ecall
L6: 

