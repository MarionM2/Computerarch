#MIPS ASSEMBLY TO APPLICATION CODE

""" addi r2 r0 0
    addi r1 r0 5
Loop beq r2 r1 exit
    add r6 r6 r2
    addi r2 r2 1
    j loop
exit

    """

r2 = 45 + 0
r1 = 45 + 5
while r2 != r1:
    r6 = 30
    r6 += r2
    r2 += 1
print(r2)