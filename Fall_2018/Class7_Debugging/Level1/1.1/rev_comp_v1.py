#!/usr/bin/env python

# --------- Start Importing modules --------- 
from __future__ import division
import optparse
from string import maketrans
# --------- Done Importing modules --------- 


# --------- Start of main() -------------------
def main():
    usage = '%prog [options] seq1 [seq2 ...]'
    p = optparse.OptionParser()
    opts, args = p.parse_args()
    
    for seq in args:
        print_rev_comp(seq)

# --------- End of main() -------------------


# --------- Start of Funtions -------------------
def print_rev_comp(seq):
    revseq = seq[::-1].upper()
    intab = "ACTG"
    outtab = "TGAC"
    trantab = maketrans((intab, outtab)
    print revseq.translate(trantab)
# --------- End of Funtions -------------------

if __name__ == "__main__":
    main()

