.data
str_nl: .asciz "\n"
.text
j Lmain
L0: 
sw ra, (sp)
L1: 
li t0, 99999
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L2: 
lw t0, -12(sp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L3: 
lw t0, -16(sp)
lw t0, (t0)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L4: 
lw t1, -12(sp)
li t2, 10
mul t1, t1, t2
sw t1, -20(sp)
L5: 
lw t1, -20(sp)
sw t1, -12(sp)
L6: 
li t1, 11
lw t0, -16(sp)
lw t2, (t0)
mul t1, t1, t2
sw t1, -24(sp)
L7: 
lw t1, -24(sp)
lw t0, -16(sp)
sw t1, (t0)
L8: 
lw t0, -12(sp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L9: 
lw t0, -16(sp)
lw t0, (t0)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L10: 
lw t1, -12(sp)
lw t0, -8(sp)
sw t1, (t0)
L11: 
lw ra, (sp)
jr ra

L12: 
Lmain:
addi sp, sp, 28
mv gp, sp
L13: 
li t1, 9
sw t1, -12(gp)
L14: 
li t1, 10
sw t1, -16(gp)
L15: 
lw t0, -12(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L16: 
lw t0, -16(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L17: 
addi fp, sp, 28
lw t0, -12(gp)
sw t0, -12(fp)
L18: 
lw t0, -16(gp)
addi t0, sp, -16
sw t0, -16(fp)
sw t0, -20(fp)
L19: 
addi t0, sp, -24
sw t0, -8(fp)
L20: 
sw sp, -4(fp)
addi sp, sp, 28
jal L0
addi sp, sp, -28
L21: 
lw t1, -24(gp)
sw t1, -20(gp)
L22: 
lw t0, -12(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L23: 
lw t0, -20(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L24: 
lw t0, -16(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl 
li a7, 4
ecall
L25: 
li a0, 0
li a7, 93
ecall
L26: 

