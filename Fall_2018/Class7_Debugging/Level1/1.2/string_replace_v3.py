#! /usr/bin/env python

# By Jason Ladner

#Simple script to create a new version of a file with a set of strings replaced
#Provide script with the file in which you want the strings replaced and with a second file that contains two columns:
#   1. The string to be replaced
#   2. The string to that should go in it's place
#There should be one row for each string to replace

# --------- Start Importing modules --------- 
from __future__ import division
import optparse
# --------- Done Importing modules --------- 


# --------- Start of main() -------------------
def main():

    #To parse command line
    usage = "usage: %prog [options]"
    p = optparse.OptionParser(usage)
    
    p.add_option('-i', '--input', help='Input file [None, REQ]')
    p.add_option('-o', '--output', help='Output filename [None, REQ]')
    p.add_option('-s', '--strings', help='Strings to replace [None, REQ]')
    opts, args = p.parse_args()

    fin = open(opts.strings, 'r')
    string_dict = {}
    for line in fin:
        cols = line.strip().split('\t')
        string_dict[cols[0]]=cols[1]

    # Closing read mode file object
    fin.close()

    fout=open(opts.output)

    for line in open(opts.input, 'r'):
        for key, value in string_dict.iteritems():
            line = line.replace(key, value)
        fout.write(line)
    
    # Closing write mode file object
    fout.close()
# --------- End of main() -------------------


if __name__ == "__main__":
    main()  
