.data
str_nl: .asciz "\n"
.text
j Lmain
L0: 
Lmain:
addi sp, sp, 28
mv gp, sp
L1: 
li a7, 5
ecall
mv t1, a0
sw t1, -12(gp)
L2: 
li t1, 0
sw t1, -16(gp)
L3: 
lw t1, -12(gp)
li t2, 0
bgt t1, t2, L5
L4: 
j L10
L5: 
lw t1, -12(gp)
li t2, 10
div t1, t1, t2
sw t1, -20(gp)
L6: 
lw t1, -20(gp)
sw t1, -12(gp)
L7: 
lw t1, -16(gp)
li t2, 1
add t1, t1, t2
sw t1, -24(gp)
L8: 
lw t1, -24(gp)
sw t1, -16(gp)
L9: 
j L3
L10: 
lw t0, -16(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L11: 
li a0, 0
li a7, 93
ecall
L12: 

