
#import necessary libraries
import re

#fecth splice donor/acceptor combinations
splice_combination=input("Please input one of three possible splice donor/acceptor combinations (GTAG, GCAG or ATAC): ")
while splice_combination not in ["GTAG","GCAG","ATAC"]:
    splice_combination=input("WRONG! Please reinput one of three possible splice donor/acceptor combinations (GTAG, GCAG or ATAC): ")

#def input file and output file
input_file="D:\IBI1\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file=f"D:\IBI1\IBI1_2024-25\Practical7\{splice_combination}_spliced_genes.fa"

#store gene sequence data
gene_sequence=[]
gene_name=""
gene_seq=""

with open(input_file, 'r') as infile: #open and read input file
    for line in infile: #line-by-line read input file
        line=line.strip() #remove whitespace of two end of gene
        if re.findall(r">",line): #find ">" in current line
            if gene_name and gene_seq:gene_sequence.append((gene_name,gene_seq)) #
            gene_name=line[1:8] ##extract the gene name only the first seven characters
            gene_seq=""
        else:
            gene_seq+=line
    
    #process the last gene
    if gene_name and gene_seq:
        gene_sequence.append((gene_name,gene_seq))

#store eligible gene sequence
spliced_genes=[]

for gene_name,gene_seq in gene_sequence: #travel gene sequence
    if splice_combination in gene_seq: #check whether contains inputed splice combination
        tata_box_count=len(re.findall(r"TATA[AT]A[AT]",gene_seq)) #calculate the count of tata box
        if tata_box_count>0:
            gene_seq=gene_seq.replace("\n","") #remove line break
            new_gene_name=f"{gene_name} tata_count: {tata_box_count}" #establish new gene sequence name
            spliced_genes.append((new_gene_name,gene_seq))

#write result in output file
with open(output_file, 'w')as outfile:
    for gene_name,gene_seq in spliced_genes:
        outfile.write(f">{gene_name}\n{gene_seq}\n")

#print count of eligible gene sequence and inputed splice combination
print(f"Found {len(spliced_genes)} genes with '{splice_combination}' splice signal and TATA boxes.") 