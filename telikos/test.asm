.data
str_nl: .asciz "\n"
.text
j Lmain
L0: 
sw ra, (sp)
L1: 
li a7, 5
ecall
mv t1, a0
lw $0, -4(sp)
lw t0, -4(t0)
addi t0, t0, -12sw t1, (t0)
L2: 
lw $0, -4(sp)
lw t0, -4(t0)
addi t0, t0, -12lw t1, (t0)
li t2, 590
blt t1, t2, L4
L3: 
j L6
L4: 
lw $0, -4(sp)
lw t0, -4(t0)
addi t0, t0, -12lw t1, (t0)
lw t0, -8(sp)
sw t1, (t0)
L5: 
j L9
L6: 
lw $0, -4(sp)
lw t0, -4(t0)
addi t0, t0, -12lw t1, (t0)
li t2, 3
add t1, t1, t2
sw t1, -12(sp)
L7: 
lw t1, -12(sp)
li t2, 4
sub t1, t1, t2
sw t1, -16(sp)
L8: 
lw t1, -16(sp)
lw t0, -8(sp)
sw t1, (t0)
L9: 
lw ra, (sp)
jr ra

L10: 
sw ra, (sp)
L11: 
lw $0, -4(sp)
addi t0, t0, -12lw t1, (t0)
li t2, 1
add t1, t1, t2
sw t1, -20(sp)
L12: 
addi fp, sp, -100
addi fp, sp, -100
addi fp, sp, -100
lw t0, -20(sp)
sw t0, -12(fp)
L13: 
