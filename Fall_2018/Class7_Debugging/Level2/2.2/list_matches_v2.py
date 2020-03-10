#!/usr/bin/env python

# --------- Start Importing modules --------- 
from __future__ import division
import optparse
# --------- Done Importing modules --------- 


# --------- Start of main() -------------------
def main():

    #To parse command line
    usage = "usage: %prog [options]"
    p = optparse.OptionParser(usage)
    
    p.add_option('-1', '--file1', help='First file [None, REQ]')
    p.add_option('-2', '--file2', help='Second file [None, REQ]')
    p.add_option('-o', '--out', help='Name of output file, if output is desired [None, OPT]')

    opts, args = p.parse_args()

    compare_lists(opts)
# --------- End of main() -------------------


# --------- Start of Funtions -------------------
def compare_lists(opts):

    first_list=file_list(opts.file1)
    second_list=file_list(opts.file2)
    
    print "Length of first list: %d" % (len(first_list))
    print "Length of second list: %d" % (len(second_list))
    
    matched = set(first_list).intersection(set(second_list))
    print "# in both lists: %d" % (len(matched))

    if opts.out:
        fout=open(opts.out, 'w')
        fout.write("%s" % ("\n".join(sorted(list(matched)))))
        fout.close()

def file_list(file, index=0):
    fin = open(file, 'r')       # open input file
    l=[]
    for line in fin:
        cols=line.split("\t")
        l.append(cols[index])
    fin.close()
    return l

# --------- End of Funtions -------------------

if __name__ == '__main__':
    main()