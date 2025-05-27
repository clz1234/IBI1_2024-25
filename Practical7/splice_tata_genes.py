#import library
#user input the splice donor/acceptor combinations and the sequence in tata box
#open the file
#initialization variable:
#read the file line by line and find the target gene
#process the data of the last gene in the file
#write to the output file section

#import library
import re
import sys
#user input the splice donor/acceptor combinations
user_input = input("input one of three possible splice donor/acceptor combinations (GTAG, GCAG,ATAC)")
if user_input not in {'GTAG', 'GCAG', 'ATAC'}:
    sys.exit("error：please input just (GTAG、GCAG、ATAC)")
donor = user_input[:2]
acceptor = user_input[2:]
#the sequence in tata box
tata_pattern = r'TATA[AT]A[AT]'
#open the file
with open('/Users/cuilizi/Desktop/Lecture/IBI/IBI1/IBI1_2024-25/IBI1_2024-25/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as input_file:
    #set blank variable for the gene in selecting
    sequence = ""
    gene_name = ""
    #create a array for gene's seq after selecting
    output_sequences = []
    #read the file throw every lines
    for line in input_file:
        #if the line start by >, it means that this line begins a new gene
        if line.startswith('>'):
            if sequence:
                #check if it in the tata box
                tata_matches = re.findall(tata_pattern, sequence)
                tata_count = len(tata_matches)
                donor_index = sequence.find(donor)
                acceptor_index = sequence.find(acceptor)
                if tata_matches and donor_index != -1 and acceptor_index != -1 and donor_index < acceptor_index:
                    output_sequences.append((gene_name,tata_count,sequence))
            #get the gene name. In orginal file, the gene's name at the fourth part, separated by space, select the gene name
            gene_name = line.split(' ')[3].lstrip('gene:')
            #empty variable
            sequence = ""
        #if the current line does not begin with a >, it is part of the gene sequence and is appended to the variable after the whitespace is removed
        else:
            sequence += line.strip()
    #deal with last data
    if sequence:
        tata_matches = re.findall(tata_pattern, sequence)
        donor_index = sequence.find(donor)
        acceptor_index = sequence.find(acceptor)
        if tata_matches and donor_index != -1 and acceptor_index != -1 and donor_index < acceptor_index:
            output_sequences.append((gene_name,tata_count,sequence))
#name the file by using user's input, open the output file and write every loops' result in it
output_filename = f'{user_input}_spliced_genes.fa'
with open(output_filename, 'w') as output_file:
    for name,count,seq in output_sequences:
        output_file.write(f">{name}  TATA_count:{count}\n")
        output_file.write(f"{seq}\n")