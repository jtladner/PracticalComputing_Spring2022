#!/usr/bin/env python

import argparse

def compare_lists(opts):

    first_list=file_list(opts.file1)
    second_list=file_list(opts.file2)
    
    print ("Length of first list: %d" % (len(first_list)))
    print ("Length of second list: %d" % (len(second_list)))
    
    matched = set(first_list).intersection(set(second_list))
    print ("# in both lists: %d" % (len(matched)))

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


parser = argparse.ArgumentParser()
parser.add_argument("-o", "--out", help="Name of output file, if output is desired")

# Here, I've added a new argument group to make it clear that these arguments are required, even though they're provided with flags
reqArgs = parser.add_argument_group('required arguments')
# Note that these arguments are added directly to the new argument group "reqArgs", not "parser" 
reqArgs.add_argument('-1', '--file1', help='First file', required=True)
reqArgs.add_argument('-2', '--file2', help='Second file', required=True)

args = parser.parse_args()


compare_lists(args)

