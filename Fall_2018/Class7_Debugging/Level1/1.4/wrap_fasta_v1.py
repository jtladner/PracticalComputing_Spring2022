#! /usr/bin/env python

# --------- Start Importing modules --------- 
import optparse
# --------- Done Importing modules --------- 


# --------- Start of main() -------------------
def main():
    #To parse command line
    usage = "usage: %prog [options]"
    p = optparse.OptionParser(usage)
    
    p.add_option('-f', '--fasta', help='Input fasta file [None, REQ]')
    p.add_option('-o', '--out', help='Name of output file [None, REQ]')
    p.add_option('-w', '--width', type='int', default=1000, help='Desired width for each line containing sequence [1000]')

    opts, args = p.parse_args()

    names, seqs = read_fasta_lists(opts.fasta)
    write_wrapped_fasta(names, seqs, opts.out, opts.width)
# --------- End of main() -------------------


# --------- Start of Funtions -------------------
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
    
    
def write_wrapped_fasta(names, seqs, new_filename, width):
    fout=open(new_filename, 'w')
    for i in range(len(names)):
        fout.write(">%s\n" % (names[i]))
        basecount=0
        for base in seqs[i]:
            basecount+=1
            fout.write("%s" % (base))
            if basecount=width:
                fout.write("\n")
                basecount=0
        fout.write("\n")
    fout.close()
# --------- End of Funtions -------------------

if __name__ == '__main__':
    main()