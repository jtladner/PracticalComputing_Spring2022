#! /usr/bin/env python

# --------- Start Importing modules --------- 
from __future__ import division
import optparse
# --------- Done Importing modules --------- 


# --------- Start of main() -------------------
def main():

    p = optparse.OptionParser()
    
    p.add_option('-f', '--fasta', help='input fasta file [None]')
    opts, args = p.parse_args()
                        
    phylip = write_relaxed_phylip_from_fasta(opts.fasta)
# --------- End of main() -------------------


# --------- Start of Funtions -------------------
def read_fasta_lists_simple(file):
fin = open(file, 'r')
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
    fout = open(phy_name, 'w')
    fout.write('%d %d\n' % (len(seqs), len(seqs[0])))
    for index in range(len(seqs)):
        fout.write('%s %s\n' % (names[index], seqs[index]))
    fout.close()
    return phy_name
# --------- End of Funtions -------------------


if __name__ == '__main__':
    main()
