#MIPS ASSEMBLY TO APPLICATION CODE

""" addi r2 r0 0
    addi r1 r0 5
Loop beq r2 r1 exit
    add r6 r6 r2
    addi r2 r2 1
    j loop
exit

    """
r0 = 45
r2 = 45 + 0
r1 = 45 + 5
# a loop to check if variables r2 and r1 are not equal
while r2 != r1:
    # if the condition is met the following operations are completed
    r6 = 30
    r6 += r2
    # increment r2
    r2 += 1
    # show the new output for r2
print(r2)