.data
str_nl: .asciz "\n"
.text
j Lmain
L0: 
Lmain:
addi sp, sp, 20
mv gp, sp
L1: 
li a7, 5
ecall
mv t1, a0
sw t1, -12(gp)
L2: 
li a7, 5
ecall
mv t1, a0
sw t1, -16(gp)
L3: 
lw t1, -12(gp)
lw t2, -16(gp)
bgt t1, t2, L5
L4: 
j L7
L5: 
lw t0, -12(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L6: 
j L7
L7: 
lw t0, -16(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L8: 
li a0, 0
li a7, 93
ecall
L9: 

