# Class 7 - Feb. 25th 2022
- In this class we will:
    - Learn how how to create and use stand-alone python scripts
    - Learn to use the argparse module to get user input
    - Learn how to create your own functions
    - Learn how to use sets

### Required Reading (**Must be completed ahead of time**)
Practical Computing for Biologists, Chapter 12

### Assignment

1. Starting from scratch, use your favorite text editor to write a stand-alone python script that, when run, will print "Hello, World!" to the screen. **Upload your completed script to BbLearn. Note: you will probably need to add ".txt" to the end of the script to get it to upload.**
2. Use Jupyter Notebook to open "PythonPt4-Class7.ipynb". This notebook contains examples of the python syntax asociated with writing your own functions and using sets, as well as part of today's assignment. Enter your code for each part of the assignment directly within the notebook cells. When you have finished all of the different parts of the assignment, **download your completed notebook as an .html file and upload to BbLearn.**
3. In this week's assignment directory, you will find two text files: 'list1.txt' and 'list2.txt'. Each of these files contains a list of IDs (e.g., PV1_064984), one per line. Write a stand-alone python script that will read in both of these lists and then create a new text file containing some combination or subset of IDs contained in these two files. This script should include the following:
    
    - Use of argparse module to handle input from the user. At least 4 arguments should be defined: one for each of the input files, one for the name of the output file and one for the **type** of output file to generate. The last argument should have the following options: union, difference, symmetric_difference, intersection.
    - Include a custom function that will take a single input file name as an argument and will return a **set** of all of the IDs contained within that file.
    - Use **set comparisons** to generate the collection of IDs to include in the output file.
    
4. Use your custom script to generate 2 new text files; one containing the intersection of the two initial lists and one containing the symmetric difference. **Upload your completed script and these two output files to BbLearn.**

## Extra fun

[Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)

[Argparse Manual](https://docs.python.org/3/library/argparse.html)

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



