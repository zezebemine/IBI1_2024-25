
seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

#import necessary libraries
import re

#find the maximum intron sequence
max_intron=re.findall(r"GT.+AG",seq)

#print the maximum intron
print('max_inclusions:', max_intron)

#initlise max_length to store length
max_length=0 

if max_intron:
    for intron in max_intron: 
        length=len(intron) #calculate length of every matched string
        if length>max_length: #compare current length to max length
            max_length=length #update max length if current length longer than max length

#print the length of maximum intron
print('max length: ',max_length)