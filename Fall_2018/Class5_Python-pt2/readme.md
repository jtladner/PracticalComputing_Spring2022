# Class 5 - Sept. 28th 2018
- In this first class we will:
    - Learn how to use lists, dictionaries and list comprehension
    - Learn about for loops and if/else statements
    - Learn about using indentation to define blocks of code

### Required Reading (**Must be completed ahead of time**)
Practical Computing for Biologists, Chapters 9-10

### Exercises

1. Use Jupyter Notebook to open "PythonPt2-Class5.ipynb". This notebook will introduce you to the Python syntax for lists, dictionaries, for loops and if/else statements. Read through each cell of the notebook and execute the contained code using "control+enter" or by pressing the play button at the top of the Notebook. Five of the cells contain exercises to complete. Enter your code for each exercise directly within the notebook cells describing the exercises. However, feel free to also make changes to the code contained in the other cells to further explore Python's syntax. 

2. For this exercise we will be revisiting the "HastingsBirdList\_2007.txt" dataset that we rearranged with regular expressions during our first class. Use your newly acquired Python coding skills to write a stand-alone script that will accomplish all of the formatting originally done with a (very complicated) regular expression. See [Class 1 Exercise 3](https://github.com/jtladner/Courses/tree/master/PracticalComputing/Fall_2018/Class1_Intro_RegExp) for a refresher. 

This script should: 
    
    1. Read in the existing file
    2. Parse the file, line by line 
    3. Write out a new file (with a different name) with the data reformatted

3. The file "MACVCarvallo68\_R1\_Q20\_cutadapt\_paired\_bwamem\_3.5_dels.txt" contains information about defective interferining genomes of Machupo virus. With the exception of the header, each line contains information about a particular deletion mutatant. Write a python script that reads through this file line by line and:

    1. Creates a dictionary containing 1 key for each unique mutant (i.e., same "RefName", "DelLeft" and "DelRight") and with the values indicating the number of occurences of the corresponding mutant.
    2. Creates an output file that includes the total count of unique mutants on each genome segment ("RefName") and information about all mutants that occur more than once within the dataset. You can format the output however you like. 

## Extra fun

Coming soon!

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



