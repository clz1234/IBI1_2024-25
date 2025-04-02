#import library 
#set the variable which from the IBI
#re.findall the sequene use greedy matching to find largest intron
#set the largest_intron's first element in largest_intron_length to get the intron's length
# print the intron's sequence
# print the length 

#import library
import re
#create a string variable seq
sequence = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
#I use the greedy matching to find the largest intron
largest_intron = re.findall(r'GT.+AG', sequence)
#to get the length
largest_intron_length = largest_intron[0]
#print result
print(largest_intron)
print(len(largest_intron_length))