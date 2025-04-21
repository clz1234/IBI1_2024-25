#import library
#open the file which downloaded from the bb
#set blank variable for the gene in selecting, and a array for genes which will be selected
#read the file, loop every line, when meet <, it means that this is a new gene
#if variable is not blank, check the gene's sequence, if there is a sequence contains "TATAWAW"
#if it has, add this gene into the array
#select the gene's name from the orginal file
#empty the sequence variable for next loop
#deal with the last sequence
#set the gene in sevral lines and write the output file

#import library
import re
#open the file
with open('/Users/cuilizi/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as input_file:
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
                tata_matches = re.findall(r'TATA[AT]A[AT]', sequence)
                #if the gene matches, add it in output_sequence
                if tata_matches:
                    output_sequences.append((gene_name, sequence))
            #get the gene name. In orginal file, the gene's name at the fourth part, separated by space, select the gene name
            gene_name = line.split(' ')[3].lstrip('gene:')
            #empty variable
            sequence = ""
        #if the current line does not begin with a >, it is part of the gene sequence and is appended to the variable after the whitespace is removed
        else:
            sequence += line.strip()
    #deal with last data
    if sequence:
        tata_matches = re.findall(r'TATA[AT]A[AT]', sequence)
        if tata_matches:
            output_sequences.append((gene_name, sequence))
#set the line length
line_length = 60
#open the output file and write every loops' result in it
with open('tata_genes.fa', 'w') as output_file:
    for name, seq in output_sequences:
        output_file.write(f">{name}\n")
        #loop it as the line_legth has setted
        for i in range(0, len(seq), line_length):
            output_file.write(seq[i:i + line_length] + '\n')