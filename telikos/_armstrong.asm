.data
str_nl: .asciz "\n"
.text
j Lmain
L0: 
Lmain:
addi sp, sp, 56
mv gp, sp
L1: 
li a7, 5
ecall
mv t1, a0
sw t1, -12(gp)
L2: 
lw t1, -12(gp)
sw t1, -20(gp)
L3: 
lw t1, -20(gp)
li t2, 0
bgt t1, t2, L5
L4: 
j L14
L5: 
lw t1, -20(gp)
li t2, 10
div t1, t1, t2
sw t1, -36(gp)
L6: 
lw t1, -36(gp)
sw t1, -24(gp)
L7: 
lw t1, -24(gp)
lw t2, -24(gp)
mul t1, t1, t2
sw t1, -40(gp)
L8: 
lw t1, -40(gp)
lw t2, -24(gp)
mul t1, t1, t2
sw t1, -44(gp)
L9: 
lw t1, -16(gp)
lw t2, -44(gp)
add t1, t1, t2
sw t1, -48(gp)
L10: 
lw t1, -48(gp)
sw t1, -16(gp)
L11: 
lw t1, -20(gp)
li t2, 10
div t1, t1, t2
sw t1, -52(gp)
L12: 
lw t1, -52(gp)
sw t1, -20(gp)
L13: 
j L3
L14: 
lw t1, -12(gp)
li t2, 0
beq t1, t2, L16
L15: 
j L18
L16: 
lw t0, -12(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L17: 
j L19
L18: 
lw t0, -12(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L19: 
li a0, 0
li a7, 93
ecall
L20: 

