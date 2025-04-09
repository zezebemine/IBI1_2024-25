
#define a function to find restriction site
def find_restriction_sites(dna_seq,recognition_seq):
    
    #check whther sequences only contain "ACGT"
    valid_nucleotides=set('ACGT')
    if not all(nucleotide in valid_nucleotides for nucleotide in dna_seq):
        return("dna_seq should only contain nucleotides 'ACGT")
    if not all(nucleotide in valid_nucleotides for nucleotide in recognition_seq):
        return("recognition_seq should only contain nucleotides 'ACGT'")
    
    #creat a empty list to store restriction location
    cut_sites=[]

    #travel DNA sequence
    for i in range(len(dna_seq)-len(recognition_seq)+1):

        #check recognition sequence
        if dna_seq[i:i+len(recognition_seq)]==recognition_seq:
            
            #store restriction sites
            cut_sites.append(i+1)
            
    #
    if not cut_sites:
        return("There is not restriction sequence in the DNA sequence.")
    
    return(f"Restriction enzyme cut sites in the DNA sequence: {cut_sites}")
    
#example of function calls
test_dna_seq="ACGTCGATATTGCCGATGCTAGCA"
test_recognition_seq="CGAT"
test_result=find_restriction_sites(test_dna_seq,test_recognition_seq)
print(test_result)

#enter else DNA sequence and recognition sequence
dna_seq=input("Please enter DNA sequence:")
recognition_seq=input("Please enter restriction sequence:")
result=find_restriction_sites(dna_seq,recognition_seq)
print(result)