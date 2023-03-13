.data
str_nl: .asciz "\n"
.text
j Lmain
L0: 
sw ra, (sp)
L1: 
lw t1, -12(sp)
li t2, 1
sub t1, t1, t2
sw t1, -16(sp)
L2: 
addi fp, sp, -100
addi fp, sp, -100
lw t0, -16(sp)
sw t0, -12(fp)
L3: 
addi t0, sp, -20
sw t0, -8(fp)
L4: 
sw sp, -4(fp)
addi sp, sp, -100
jal L-100
addi sp, sp, --100
L5: 
lw t1, -12(sp)
li t2, 2
sub t1, t1, t2
sw t1, -24(sp)
L6: 
addi fp, sp, -100
lw t0, -24(sp)
sw t0, -12(fp)
L7: 
addi t0, sp, -28
sw t0, -8(fp)
L8: 
sw sp, -4(fp)
addi sp, sp, -100
jal L-100
addi sp, sp, --100
L9: 
lw t1, -20(sp)
lw t2, -28(sp)
add t1, t1, t2
sw t1, -32(sp)
L10: 
lw t1, -32(sp)
lw t0, -8(sp)
sw t1, (t0)
L11: 
li a0, 0
li a7, 93
ecall
L12: 
lw ra, (sp)
jr ra
L13: 
Lmain:
addi sp, sp, 20
mv gp, sp
L14: 
li a7, 5
ecall
mv t1, a0
sw t1, -12(gp)
L15: 
addi fp, sp, -100
lw t0, -12(gp)
sw t0, -12(fp)
L16: 
addi t0, sp, -16
sw t0, -8(fp)
L17: 
sw sp, -4(fp)
addi sp, sp, -100
jal L-100
addi sp, sp, --100
L18: 
lw t0, -16(gp)
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
