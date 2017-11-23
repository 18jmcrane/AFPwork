#The DNA sequence being split up for the fragmenting
DNAseq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
#This find what position the lettering is at, to count the size of the firstfragment
# (adding 1 because the index starts at 0)
DNAlength1 = DNAseq.find("GAATTC") + 1
#Finding size of the whole Seqeunce then minusing the first length to get the second fragment length
DNAlength2 = len(DNAseq) - DNAlength1
#Prints the sequences lengths to user
print("The Length of the first fragment is", DNAlength1)
print("The Length of the second being", DNAlength2)
