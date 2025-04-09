
#import necessary libraries
import re

#def input file to read and output file to write
input_file="D:\IBI1\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file="D:\IBI1\IBI1_2024-25\Practical7\Tata_genes.fa"

#write regular expression
consensus_seq=r"TATA[AT]A[AT]"

#store gene name and sequence
gene_name=""
gene_seq=""

#open input file to read and output file to write
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile: #line-by-line read input file 
            if line.startswith('>'): #find ">" in current line
                if gene_name and gene_seq: #chek whether store gene name and sequence
                    if re.search(consensus_seq,gene_seq): #search specific regular expression
                        outfile.write(f">{gene_name}\n{gene_seq}") #write gene name and gene sequence in output file and change line
                gene_name=line[line.find("gene:")+5:line.find("gene_biotype:")-1]
                gene_seq=""         
            
            else:
                gene_seq+=line #add current content to gene sequence if this line don not contain ">"
        
        #process the last gene
        if gene_name and gene_seq:
           if re.search(consensus_seq, gene_seq):
               outfile.write(f">{gene_name}\n{gene_seq}")
               