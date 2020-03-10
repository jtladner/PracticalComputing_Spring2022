# Class 7 - Oct. 12th 2018
- In this first class we will:
    - Practice debugging Python scripts

### Required Reading (**Must be completed ahead of time**)
Practical Computing for Biologists, Chapters 13,16


### Exercises

For today's exercises, I've provided a set of Python scripts, all containing bugs that either prevent execution or result in unintended results. The buggy scripts have been organized into levels depending on the nature of the bugs. 

#### Level 1: each script containins a single bug that will prevent the script from running

1. Exercise 1.1: rev_comp.py is a script that accepts one or more DNA sequences as arguments on the command line. The reverse complement versions of these sequences will be printed to the screen. Here is an example command:
    
    ```rev_comp.py ACTGTAGACACACCATAG```

    There are three versions of this script. Each contains a single bug. Attempt to run the example command with both versions and track down the bug based on the error messages. 
    
2. Exercise 1.2: string\_replace.py replaces a list of strings within a file, each with a specified replacement string. The target and replacement strings are provided as a tab-delimited file (e.g., "names\_to_replace.txt"). You also need to provide the input file and a name for the output file. Here is an example command:
    
    ```string_replace.py -i infile.txt -o outfile.txt -s names_to_replace.txt```

    There are three versions of this script. Each contains a single bug. Attempt to run the example command with both versions and track down the bug based on the error messages. 

3. Exercise 1.3: fasta2phy.py is a script that converts a fasta formatted alignment file to a relaxed phylip formatted file. Here is an example command:
    
    ```fasta2phy.py -f lassa_seqs.fasta```

    There are three versions of this script. Each contains a single bug. Attempt to run the example command with both versions and track down the bug based on the error messages. 

3. Exercise 1.4: In this exercise, you will revisit wrap\_fasta.py, the Python script we used in Class 3 Exercise 4. As a reminder, this script changes the length of the sequence lines within a fasta file. Here is an example command:

    ```wrap_fasta.py -f zika_1_1.fasta -o zika_1_1_1000.fasta -w 1000```

    There are two versions of this script. Each contains a single bug. Attempt to run the example command with both versions and track down the bug based on the error messages. 


#### Level 2: each script contains a single bug. The bug will not prevent the script from running, but will prevent generation of the expected output. 

1. Exercise 2.1: Again, you'll be focusing on wrap\_fasta.py. There are two versions of this script. Each contains a single bug. There is also a file called ExpectedOutput.fasta, which contains the expected output of the bug free script. Attempt to run the example command with both versions, check the output and track down the bugs. 

2. Exercise 2.2: list_matches.py is a script that compares two lists of items (read in from text files). It prints three pieces of information to the screen: 1) the length of the first list, 2) the length of the second list and 3) the number of shared elements. It also creates a new text file containing only the shared elements. Here is an example command:  

    ```./list_matches.py -1 list1.txt -2 list2.txt -o output.txt```

There are two versions of this script. Attempt to run the example command with both versions, check the output and track down the bugs.


## Extra fun

[pdb module](https://docs.python.org/2/library/pdb.html)

[other tools](https://wiki.python.org/moin/PythonDebuggingTools)

Copyright (C) 2017  Jason Ladner

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.



