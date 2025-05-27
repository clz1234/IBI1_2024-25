#define an function called find_restriction_sites(dna_sequence, enzyme_sequence)
#check the sequence, if they all in ACGT
#use ValueError to ouput error
#set an array for cut site
#to check the dna genes individually, it needs to check them len(dna_sequence) - len(enzyme_sequence) + 1 times
#if the dna sequence from i to i+len(enzyme_sequence) is the same as the enzyme_sequence
#add it to cut_sites and stop the function 
#an example call the code

#define the function
def find_restriction_sites(dna_sequence, enzyme_sequence):
    if not all(nucleotide in "ACGT" for nucleotide in dna_sequence) or not all(nucleotide in "ACGT" for nucleotide in enzyme_sequence):
        raise ValueError("the DNA sequence and the enzyme recognition sequence must contain only ACGT nucleotides")
    #find cut site
    cut_site = []
    for i in range(len(dna_sequence) - len(enzyme_sequence) + 1):
        if dna_sequence[i:i+len(enzyme_sequence)] == enzyme_sequence:
            cut_site.append(i)
    return cut_site
#an example
dna = "ACGTACATACGT"
enzyme = "GTAC"
site = find_restriction_sites(dna, enzyme)
print(f"DNA sequence: {dna}，enzyme sequence: {enzyme}，cut site: {site}")