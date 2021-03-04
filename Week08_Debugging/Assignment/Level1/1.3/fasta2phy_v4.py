#! /usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
# Here, I've added a new argument group to make it clear that these arguments are required, even though they're provided with flags
reqArgs = parser.add_argument_group('required arguments')
# Note that these arguments are added directly to the new argument group "reqArgs", not "parser" 
reqArgs.add_argument("-f", "--fasta", help="Input fasta file name", required=True)
args = parser.parse_args()

def read_fasta_lists_simple(file):
    with open(file, 'r') as fin:
        count=0
    
        names=[]
        seqs=[]
        seq=''

        for line in fin:
            line=line.strip()
            if line and line[0] == '>':                #indicates the name of the sequence
                count+=1
                names.append(line.split()[0][1:])
                if count>1:
                    seqs.append(seq)
                seq=''
            else: seq +=line
        seqs.append(seq)
    
    return names, seqs

def write_relaxed_phylip_from_fasta(fasta):
    names, seqs = read_fasta_lists_simple(fasta)
    phy_name = '%s.phy' % ".".join(fasta.split('/')[-1].split('.')[0:-1])
    with open(phy_name, 'w') as fout:
        fout.write('%d %d\n' % (len(seqs), len(seqs[0])))
        for index in range(len(seqs)):
            fout.write('%s %s\n' % (names[index], seqs[index]))


write_relaxed_phylip_from_fasta(args.fastafile)
