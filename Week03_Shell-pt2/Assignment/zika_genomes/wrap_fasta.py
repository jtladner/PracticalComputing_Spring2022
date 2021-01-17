#! /usr/bin/env python

import sys

#Will take a fasta of whatever type and rewrite it so that all the sequences are wrapped at the same width, default=60
#First argument should be input fasta and the second should be the name for he new fasta

def main():
    names, seqs = read_fasta_lists(sys.argv[1])
    write_wrapped_fasta(names, seqs, sys.argv[2], int(sys.argv[3]))


# Extracts data from a fasta sequence file. Returns two lists, the first holds the names of the seqs (excluding the '>' symbol), and the second holds the sequences
def read_fasta_lists(file):
    fin = open(file, 'r')
    count=0
    
    names=[]
    seqs=[]
    seq=''
    for line in fin:
        line=line.strip()
        if line and line[0] == '>':                #indicates the name of the sequence
            count+=1
            names.append(line[1:])
            if count>1:
                seqs.append(seq)
            seq=''
        else: seq +=line
    seqs.append(seq)
    
    return names, seqs
    
    
def write_wrapped_fasta(names, seqs, new_filename, width=60):
    fout=open(new_filename, 'w')
    for i in range(len(names)):
        fout.write(">%s\n" % (names[i]))
        basecount=0
        for base in seqs[i]:
            basecount+=1
            fout.write("%s" % (base))
            if basecount==width:
                fout.write("\n")
                basecount=0
        fout.write("\n")
    fout.close()
                                            
    
###-------------->>>
if __name__ == '__main__':
    if len(sys.argv) != 4: print ('Usage:  wrap_fasta.py  input_fasta  output_name line_width')
    else: main()