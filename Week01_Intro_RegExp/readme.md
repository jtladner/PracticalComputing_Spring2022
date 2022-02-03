# Class 1 - Jan. 14th 2022
- In this first class we will:
    - Discuss the syllabus and course organization/expectations
    - Troubleshoot computer setup problems
    - Learn to use regular expressions to edit text files

### Required Reading (**Must be completed ahead of time**)
Practical Computing for Biologists, Chapters 1-3

### Prep for next class

1. Open your command line interface and type this command followed by 'Enter':
```echo $SHELL```

If the reponse is not "/bin/bash" or "/bin/zsh", let me know. 

### Assignment

1. Go to [RegexOne](https://regexone.com/) and complete the 15 lesson tutorial. This website provides a nice interactive interface for playing with regular expressions.
    - Although the interface will allow you to only match a portion of each line, when possible, I encourage you to write expressions that match the entirety of each line. 
    - **Keep track of your solutions in the table provided in the Assignment Answer Sheet.**

2. We will now start using the text editor on your computer to use regular expressions to edit text files. 
    1. Open "EBOV.phy" in your text editor.
    2. Use a series of find/replace queries to convert this [phylip formatted](http://scikit-bio.org/docs/0.2.3/generated/skbio.io.phylip.html#:~:text=PHYLIP%20format%20is%20a%20plain,the%20multiple%20sequence%20alignment%20itself.) sequence alignment into a [fasta formatted](https://en.wikipedia.org/wiki/FASTA_format) file. **Record find/replace queries in Assignment Answer Sheet.**
    
    Fasta format example:
     ```
     >name1
     seq1
     >name2
     seq2
     ```
    
    3. Revert back to the original "EBOV.phy" file and now edit your regular expression(s) to also change the sequence names. New names should only include the characters prior to the first underscore ('_'). **Record find/replace queries in Assignment answer sheet.**
    4. Revert back to the original "EBOV.phy" file and now edit your regular expression(s) to remove all 'N' characters from the beginning and end of each sequence. **Record find/replace queries in the Assignment answer sheet.**
    5. **Upload final fasta-formatted file to Bb Learn along with Assignment Answer Sheet.**

3. Open "HastingsBirdList\_2007.txt" in your text editor. This file contains tab-delimited information about bird species cited in the Hastings Park Conservancy in Vancouver, BC.
    1. Design a single search and replace query that utilizes regular expressions to reformat **every** line to the following format:
    ```Genus\tspecies\tG. species\tCommon Name\tStatus```
    "Status" is the column with a categorical variable including "Casual", "Rare Visitor", etc. Make sure to remove the "*" character from the beginning of the Status category, if present. **Record the find/replace query in the Assignment answer sheet.** (**Tip: Copy and paste reformatted text into Excel to double check**)
    2. Upload re-formatted file to Bb Learn along with Assignment Answer Sheet.
    
## Extra fun

Explore for "extra credit" or in the event that you finish all of the other exercises.

[RegexOne Problems](https://regexone.com/problem/matching_decimal_numbers)

[Regex Crossword](https://regexcrossword.com/)

Copyright (C) 2021  Jason Ladner

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



