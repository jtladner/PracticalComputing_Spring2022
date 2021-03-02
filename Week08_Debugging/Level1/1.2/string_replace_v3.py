#! /usr/bin/env python

# By Jason Ladner

#Simple script to create a new version of a file with a set of strings replaced
#Provide script with the file in which you want the strings replaced and with a second file that contains two columns:
#   1. The string to be replaced
#   2. The string to that should go in it's place
#There should be one row for each string to replace

import argparse

parser = argparse.ArgumentParser()

# Here, I've added a new argument group to make it clear that these arguments are required, even though they're provided with flags
reqArgs = parser.add_argument_group('required arguments')
# Note that these arguments are added directly to the new argument group "reqArgs", not "parser" 
reqArgs.add_argument("-i", "--input", help="Input file name", required=True)
reqArgs.add_argument("-o", "--output", help="Output file name", required=True)
reqArgs.add_argument("-s", "--strings", help="Strings to replace", required=True)
args = parser.parse_args()

# Read info for replacing strings
with open(args.strings, 'r') as fin:
    string_dict = {}
    for line in fin:
        cols = line.strip().split('\t')
        string_dict[cols[0]]=cols[1]


# Generate new version of input file
with open(args.output, 'w') as fout:
    with open(args.input, 'r') as fout:
        for line in fin:
            for key, value in string_dict.items():
                line = line.replace(key, value)
            fout.write(line)

