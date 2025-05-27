'''
import necessary library
Library and matrix import: Load the matrix through biopython.
The FASTA read logic skips the title line (starting with >) and merges the sequence content
Consistency calculation: Compare amino acids bit by bit, calculate the same proportion and retain two decimal places
Compare the score logic, verify that the sequence lengths are consistent (no blank alignment requirements), and use the BLOSUM62 matrix to accumulate the scores
Output
'''
# import necessary library
# import the BLOSUM62 matrix
from Bio.Align import substitution_matrices
blosum62 = substitution_matrices.load("BLOSUM62")

# read the .fasta file
def read(filename):
    sequence=''
    with open(filename,'r') as f:
        for line in f:
            if line[0]!='>':
                sequence+=line.strip()
    return sequence

# calculate the percentage of identical amino acid
def identity(seq1, seq2):
    distance = sum(c1 == c2 for c1, c2 in zip(seq1, seq2))
    percent = distance / len(seq1) * 100
    return round(percent, 2)

# calculate the alignment score based on BLOSUM62
def score(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be of equal length.")
    return sum(blosum62[s1][s2] for s1,s2 in zip(seq1, seq2))

# get the input
human=read('P04179.fasta.txt')
mouse=read('P09671.fasta.txt')
random=read('random_seq.fasta')

# print out the results
print(f"Human sequence length: {len(human)}")
print(f"Mouse sequence length: {len(mouse)}")
print(f'For human and mouse, the alignment score is {score(human,mouse)}, the percentage of identical amino acids is {identity(human,mouse)}')
print(f'For human and random, the alignment score is {score(human,random)}, the percentage of identical amino acids is {identity(human,random)}')
print(f'For random and mouse, the alignment score is {score(random,mouse)}, the percentage of identical amino acids is {identity(random,mouse)}')