sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
#counts total of letters of string to be used to divide
total = len(sequence)
#counts number of c in string to calculate the percantages
numberC = sequence.count("C")
#counts number of g in string to calculate the percantages
numberG = sequence.count("G")

#finds the percentage of C in the DNA
percentageC = ((numberC/total) * 100)

#finds the percentage of G in the DNA
percentageG = ((numberG/total) * 100)

#Adds both percentage together to get the total avergage of GC
GCpercentage = (percentageG+percentageC)

#prints and rounds it to ",2" 2 decimal places using the "round" funtion
print(round(GCpercentage,2))
