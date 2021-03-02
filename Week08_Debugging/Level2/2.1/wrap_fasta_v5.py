#! /usr/bin/env python

import argparse


# Extracts data from a fasta sequence file. Returns two lists, the first holds the names of the seqs (excluding the '>' symbol), and the second holds the sequences
def read_fasta_lists(file):
    with open(file, 'r') as fin:
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
    
    
def write_wrapped_fasta(names, seqs, new_filename, width):
    with open(new_filename, 'w') as fout:
        for i in range(len(names)):
            fout.write(">%s" % (names[i]))
            basecount=0
            for base in seqs[i]:
                basecount+=1
                fout.write("%s" % (base))
                if basecount==width:
                    fout.write("\n")
                    basecount=0
            fout.write("\n")


parser = argparse.ArgumentParser()
parser.add_argument("-w", "--width", type=int, default=1000, help="Desired width for each line containing sequence")

# Here, I've added a new argument group to make it clear that these arguments are required, even though they're provided with flags
reqArgs = parser.add_argument_group('required arguments')
# Note that these arguments are added directly to the new argument group "reqArgs", not "parser" 
reqArgs.add_argument('-f', '--fasta', help='Input fasta file', required=True)
reqArgs.add_argument("-o", "--out", help="Output file name", required=True)

args = parser.parse_args()


names, seqs = read_fasta_lists(args.fasta)
write_wrapped_fasta(names, seqs, args.out, args.width)
