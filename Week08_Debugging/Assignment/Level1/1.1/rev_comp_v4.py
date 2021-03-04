#!/usr/bin/env python

import argparse

def print_rev_comp(seq):
    revseq = seq[::-1].upper()
    intab = "ACTG"
    outtab = "TGAC"
    trantab = str.maketrans(intab, outtab)
    print (revseq.translate(trantab))

parser = argparse.ArgumentParser()
# "nargs='*'" used to specify that multiple values can be provided for seq, in the same command.
parser.add_argument("seq", help="A DNA sequence to be reverse complemented. Can provide multiple sequences separated by spaces", nargs='*')
args = parser.parse_args()


for seq in args.seq:
print_rev_comp(seq)



