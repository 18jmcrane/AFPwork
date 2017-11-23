seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1 = seq[0:63]
intron = seq[63:90]
exon2 = seq[90:]
#

#calculates the length of the string
seqindex = len(exon1+exon2)
#calculates the length of the string
exonindex = len(seq)
#takes the data and converts it into a percentage
percentage = (seqindex/exonindex) * 100
#rounds the data to two decimal places
final = (round(percentage,2))
#prints the final percentage
print("The percentage of extrons is",final,"%")
print()
lowercaseDNA = (exon1+intron.lower()+exon2)
print(lowercaseDNA)








