.data
str_nl: .asciz "\n"
.text
j Lmain
L0: 
sw ra, (sp)
L1: 
lw t1, -16(sp)
lw t2, -12(sp)
div t1, t1, t2
sw t1, -20(sp)
L2: 
lw t1, -20(sp)
lw t2, -12(sp)
mul t1, t1, t2
sw t1, -24(sp)
L3: 
lw t1, -16(sp)
lw t2, -24(sp)
beq t1, t2, L5
L4: 
j L7L5: 
li t1, 1
lw t0, -8(sp)
sw t1, (t0)
L6: 
j L8L7: 
li t1, 0
lw t0, -8(sp)
sw t1, (t0)
L8: 
lw ra, (sp)
jr ra
L9: 
sw ra, (sp)
L10: 
li t1, 2
sw t1, -16(sp)
L11: 
lw t1, -16(sp)
lw t2, -12(sp)
blt t1, t2, L13
L12: 
j L24L13: 
addi fp, sp, 28
lw t0, -16(sp)
sw t0, -12(fp)
L14: 
lw t0, -12(sp)
sw t0, -16(fp)
L15: 
addi t0, sp, -20
sw t0, -8(fp)
L16: 
sw sp, -4(fp)
addi sp, sp, 28
jal L0
addi sp, sp, -28
L17: 
lw t1, -20(sp)
li t2, 1
beq t1, t2, L19
L18: 
j L21L19: 
li t1, 0
lw t0, -8(sp)
sw t1, (t0)
L20: 
j L21L21: 
lw t1, -16(sp)
li t2, 1
add t1, t1, t2
sw t1, -24(sp)
L22: 
lw t1, -24(sp)
sw t1, -16(sp)
L23: 
j L11L24: 
li t1, 1
lw t0, -8(sp)
sw t1, (t0)
L25: 
lw ra, (sp)
jr ra
L26: 
Lmain:
addi sp, sp, 20
mv gp, sp
L27: 
li t1, 2
sw t1, -12(gp)
L28: 
lw t1, -12(gp)
li t2, 30
ble t1, t2, L30
L29: 
j L38L30: 
addi fp, sp, 28
lw t0, -12(gp)
sw t0, -12(fp)
L31: 
addi t0, sp, -16
sw t0, -8(fp)
L32: 
sw sp, -4(fp)
addi sp, sp, 28
jal L9
addi sp, sp, -28
L33: 
lw t1, -16(gp)
li t2, 1
beq t1, t2, L35
L34: 
j L37L35: 
lw t0, -12(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L36: 
j L37L37: 
j L28L38: 
li a0, 0
li a7, 93
ecall
L39: 
