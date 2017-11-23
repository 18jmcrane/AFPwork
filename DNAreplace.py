#The DNA sequence being replaced
sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
#Replaced Sequence Letters, "T with A" and "G with C" and "A with T" and "C with G"
newseq = sequence.replace("T","a").replace("G","c").replace("A","t").replace("C","g")
#Prints it in upper case
print(newseq.upper())


