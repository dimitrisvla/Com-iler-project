.data
str_nl: .asciz "\n"
.text
j Lmain
L0: 
sw ra, (sp)
L1: 
li t1, 4
sw t1, -12(sp)
L2: 
lw t1, -16(gp)
sw t1, -12(gp)
L3: 
lw $0, -4(sp)
addi t0, t0, -12lw t1, (t0)
lw $0, -4(sp)
addi t0, t0, -16lw t0, (t0)
sw t1, (t0)
L4: 
lw $0, -4(sp)
addi t0, t0, -20lw t1, (t0)
lw t2, -12(sp)
add t1, t1, t2
sw t1, -16(sp)
L5: 
lw t1, -16(sp)
lw t0, -8(sp)
sw t1, (t0)
L6: 
lw ra, (sp)
jr ra
}
L7: 
sw ra, (sp)
L8: 
li t1, 3
sw t1, -20(sp)
L9: 
lw t0, -12(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L10: 
lw t0, -16(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L11: 
addi fp, sp, 20
addi t0, sp, -24
sw t0, -8(fp)
L12: 
sw sp, -4(fp)
addi sp, sp, 20
jal L0
addi sp, sp, -20
L13: 
lw t1, -24(sp)
sw t1, -16(gp)
L14: 
lw t0, -12(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L15: 
lw t0, -16(gp)
mv a0, t0
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L16: 
lw ra, (sp)
jr ra
}
L17: 
Lmain:
addi sp, sp, 20
mv gp, sp
L18: 
li t1, 1
sw t1, -12(gp)
L19: 
li t1, 2
sw t1, -16(gp)
L20: 
addi fp, sp, 28
lw t0, -12(gp)
sw t0, -12(fp)
L21: 
lw t0, -16(gp)
addi t0, sp, -16
sw t0, -16(fp)
sw t0, -20(fp)
L22: 
sw sp, -4(fp)
addi sp, sp, 28
jal L7
addi sp, sp, -28
L23: 
lw t0, -12(gp)
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
}
